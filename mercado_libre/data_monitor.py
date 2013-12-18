# coding:utf-8

# Lib imports
from api_connection import public_api_connection as api_conn
from datetime import datetime, date

# ------------------------------------------------------------------------------
def prod_status(product_id):
    # This function verifies if a product is still active or listed and returns 
    # last updated date or a tuple with the error and its description
    
    api = api_conn()
    item_api_url = api.connect_resource('items', product_id)
    json_file = api.read(item_api_url)
    
    # APi only returns error key if there's an error, ex.: the product is not 
    # listed anymore
    try:
        if json_file['error'] == 'not_found':
            return ("error: " + json_file['error'], "cause: " + ", ".join(json_file['cause']))
    except KeyError: 
        last_updated = datetime.strptime(json_file['last_updated'],"%Y-%m-%dT%H:%M:%S.%fZ")
        last_updated = last_updated.strftime("%Y-%m-%d %H:%M")
        return last_updated
    

# ------------------------------------------------------------------------------
class price():
    # This class is used to monitor the product prices, it's used to trigger
    # events as email marketing, recommendations or buy orders.
    
    def last(self, product_id):
        # This function retrieves the last product price
        api = api_conn()
        item_api_url = api.connect_resource('items', product_id)
        json_file = api.read(item_api_url)
        return json_file['price']
        
        
    def compare(self, last, target_price):
        # This function compares the last price with the target price and
        # returns the ratio to target price
        return (float(last)/float(target_price)) - 1.00
# ------------------------------------------------------------------------------    
