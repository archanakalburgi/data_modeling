## Fetch Rewards Coding Exercise 

After cloning the directory into the local machine, to successfully execute code follow these steps.

On terminal execute the following commands

Create and activate python virtual environment 

```
python3 -m venv fetch_analytics
source fetch_analytics/bin/activate
```

Install required packages

```
pip install -r requirement.txt
```


To read the json file, process the data, transform into the pandas dataframe and insert the data into the database run [this](script.py) script. Type this command on the terminal 

```
python3 script.py
```

This will execute the script and perform the necessary operations to read the json file, process the data, and insert it into the database. 

The transformation of the raw data is done in [transformations.py](transformations.py). This acts like a transformation layer. 

Packages used in the assignments are given in [requirement.txt](requirement.txt)

[fetch_database.db](fetch_database.db) is a `sqlite` database generated in `script.py`. All the modeled datasets are stored in this database.

The data qualities issues are found by performing EDA on the dataset using python [notebook](eda.ipynb). Serves the third requirement of the assignment **Third: Evaluate Data Quality Issues in the Data Provided**. 

### Folder structure 

#### data folder

Tis directory contains the raw data in a json file 
1. [brands.json](data/brands.json)
2. [receipts.json](data/receipts.json)
3. [users.json](data/users.json)
 

#### sql folder

This folders has all the sql transformations done the datasets while solving the exercise. These SQl queries serves as the answers to the question asked in the **Second: Write a query that directly answers a predetermined question from a business stakeholder**

#### writeup 

1. [Entity Relation Diagram](writeup/ERD.png)

This is a simplified, structured, relational diagram to represent how I would model the data in a data warehouse and servers as solution for **First: Review Existing Unstructured Data and Diagram a New Structured Relational Data Model**

2. [email_stakeholders.md](writeup/email_stakeholders.md)

A short slack message composed for the business stakeholders. Servers as an answer for **Fourth: Communicate with Stakeholders**

3. [sql_queries.md](writeup/sql_queries.md)

Details of the SQL queried and more information on the queries 
