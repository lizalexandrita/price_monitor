# coding:utf-8

# Lib imports
import api_connection as api_conn

# ------------------------------------------------------------------------------
class price():
    # This class is used to monitor the product prices, it's used to trigger
    # events as email marketing, recommendations or buy orders.
    
    def last(self, product_id):
        # This function retrieves the last product price
        pass
        
    def target_comp(self, last, target_price):
        # This function compares the last price with the user target price and
        # returns: IsGreater, IsLesser, IsEqual
        pass
    
    def db_comp(self, last, db_price):
        # This function compares the last price with the database price and
        # returns: IsGreater, IsLesser, IsEqual
        pass
    
def prod_status(product_id):
    # This function verifies if a product is still active or listed
    pass