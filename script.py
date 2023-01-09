import json
import sqlite3
import pandas as pd
import transformations as transform

def get_name(path):
    """
    This function extracts the name of a table from a file path. 
    """
    components = path.split('/')
    file_name = components[-1].split('.')
    table_name = file_name[0]
    return table_name

def insert_to_database(conn, df, table_name):
    """
    This function inserts a Pandas DataFrame into a table 
    in a sqlite database using the given connection. 
    The table is created from the DataFrame, 
    replacing any existing table with the same name.
    """
    tuples = [tuple(x) for x in df.to_numpy()]
    col = list(df.columns)
    columns = ', '.join(col)

    drop_table_query = f"DROP TABLE IF EXISTS {table_name}"
    create_table_query = f"CREATE TABLE {table_name} ({columns})"
    values_str = "?,"*len(col)
    values_string = values_str[:-1] 
    insert_query = f"INSERT INTO {table_name} VALUES ({values_string})"

    cursor = conn.cursor()
    cursor.execute(drop_table_query)
    cursor.execute(create_table_query)
    cursor.executemany(insert_query, tuples) 
    conn.commit()
    cursor.close()

def json_to_database(path, conn):
    """
    This function reads and transforms data from a JSON file into a Pandas DataFrame, 
    which is then inserted into a table in a sqlite database.
    """
    result_list = []
    name = get_name(path)
    with open(path) as f:
        for line in f:
            if name == 'users':
                result_list.append(transform.transform_users(json.loads(line)))
            elif name == 'brands':
                result_list.append(transform.transform_brands(json.loads(line)))
            if name == 'receipts':
                result_list.append(transform.transform_receipts(json.loads(line)))
        df = pd.DataFrame(result_list)
        insert_to_database(conn, df, name)


def main():
    """
    This function creates a connection to a sqlite database and populates it with data from three JSON files: 
    users.json, 
    brands.json, and 
    receipts.json. 
    The data from each file is written to a separate table in the database.
    """
    conn = sqlite3.connect("fetch_database.db") # Creates sqlite database 

    json_to_database('data/users.json' , conn)
    print('Written to users table')
    json_to_database('data/brands.json' , conn)
    print('Written to brands table')
    json_to_database('data/receipts.json' , conn)
    print('Written to receipts table')
    conn.close()

if __name__ == "__main__":
    main()