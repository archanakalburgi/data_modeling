def transform_users(data_dictionary):
    """
    This function takes in a json and returns a new dictionary, 
    with some key-value pairs renamed. 
    If an exception is raised, 
    the original dictionary and 
    the exception message are printed and the function returns None.
    """
    result = {}
    try:
        result = {
                    "id": data_dictionary["_id"]["$oid"]                               
                    ,"state": data_dictionary.get("state",None)
                    ,"createdDate": data_dictionary.get("createdDate", {}).get( "$date", None)             
                    ,"lastLogin": data_dictionary.get("lastLogin", {}).get( "$date", None)
                    ,"role": data_dictionary["role"]                                    
                    ,"active": data_dictionary["active"]  
                    ,"signUpSource": data_dictionary.get("signUpSource", None) 
                } 
        return result
    except Exception as e:
        print(data_dictionary, e)
        print('Failed to transform')
        return None

def transform_brands(data_dictionary):
    """
    This function takes in a json of data and returns a new dictionary, 
    with some key-value pairs renamed. 
    If an exception is raised, 
    the original dictionary and the 
    exception message are printed and the function returns None.
    """
    try:
        result = {
                    'id' : str(data_dictionary['_id']['$oid']) 
                    ,'barcode' : data_dictionary['barcode']
                    ,'brandCode' : data_dictionary.get('brandCode', None) 
                    ,'category' : data_dictionary.get('category', None) 
                    ,'categoryCode' : data_dictionary.get('categoryCode',None) 
                    ,'cpg_id' : str(data_dictionary.get('cpg',{}).get('$id',{}).get('$oid',{}))
                    ,'cpg_ref' : str(data_dictionary.get('cpg',{}).get('$ref',{})) 
                    ,'topBrand' : data_dictionary.get('topBrand', None) 
                    ,'name' : data_dictionary['name'] 
                }
        return result
    except Exception as e:
        print(data_dictionary, e)
        print('Failed to transform')
        return None

def transform_receipts(data_dictionary):
    """
    This function takes in a json dictionary with a subset of the data, 
    with some key-value pairs renamed. 
    It also processes a list of dictionaries nested within the input dictionary and 
    merges the resulting dictionaries into the output dictionary. 
    If an exception is raised, the original dictionary and 
    the exception message are printed and the function returns None.
    """
    try:
        receipts = {
                    "receipt_id" : data_dictionary["_id"]["$oid"]
                    ,"bonusPointsEarned" : int(data_dictionary.get("bonusPointsEarned", 0))
                    ,"bonusPointsEarnedReason" : data_dictionary.get("bonusPointsEarnedReason", None)
                    ,"createDate" : data_dictionary.get("createDate",{}).get("$date", None)
                    ,"dateScanned" : data_dictionary.get("dateScanned",{}).get("$date",None)
                    ,"finishedDate" : data_dictionary.get("finishedDate",{}).get("$date",None)
                    ,"modifyDate" : data_dictionary.get("modifyDate",{}).get("$date",None)
                    ,"pointsAwardedDate" : data_dictionary.get("pointsAwardedDate",{}).get("$date",None)
                    ,"purchaseDate" : data_dictionary.get("purchaseDate",{}).get("$date",None)
                    ,"pointsEarned" : float(data_dictionary.get("pointsEarned",0.0))
                    ,"purchasedItemCount" : int(data_dictionary.get("purchasedItemCount", 0))
                    ,"rewardsReceiptStatus" : data_dictionary.get("rewardsReceiptStatus", [])
                    ,"totalSpent" : float(data_dictionary.get("totalSpent", 0.0)) 
                    ,"userId" : data_dictionary.get("userId", None)
                }

        for item in data_dictionary.get("rewardsReceiptItemList", []):
            transformed_item = transform_receipts_item_list(item)
            receipts.update(transformed_item)
        return receipts

    except Exception as e:
        print(data_dictionary, e)
        print('Failed to transform')
        return None

def transform_receipts_item_list(item):
    """
    This function takes in a list and 
    returns a new dictionary with a subset of the data. 
    The keys and values in the output dictionary are renamed from the input dictionary.
    """
    item_dict = {
                'barcode': item.get('barcode', None)
                ,'brandCode': item.get('brandCode', None)
                ,'finalPrice': item.get('finalPrice', 0.0)
                ,'itemPrice': item.get('itemPrice', 0.0)
                ,'quantityPurchased': item.get('quantityPurchased', 0.0)
            }
    return item_dict

