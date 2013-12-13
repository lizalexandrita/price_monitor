# coding:utf-8

# Lib imports
import pycurl
import StringIO
import json
import string

# ------------------------------------------------------------------------------
class public_api_connection(object):
    # This class retrieves information from a given url
    def __init__(self, url_string):
        # This function initiates the class attributes used to connect to 
        # mercado libre api and use the public api resources
        self.base_api = 'https://api.mercadolibre.com/'
        self.item_url = url_string
        self.item_id = self.product_id(url_string)
        self.site = self.item_id[:3]
        self.public_resources = ['users','sites','categories','countries','states',
            'cities','currencies','currency_conversions','items','pictures']
        self.item_api_url = self.base_api + 'items/' + self.item_id
        
    def product_id(self, url_string):
        # This function returns the product id from a url
        init = string.rfind(url_string,'/')
        mid = string.find(url_string,'-',init)
        end = string.find(url_string,'-',mid+1)
        product_id = url_string[init+1:mid]+url_string[mid+1:end]
        return product_id
        
    def read(self, public_api_url):
        # This function returns a dictionary from the json file.
        # It only works with public api functions. All transactions and payments 
        # are handled with access tokens
        output = StringIO.StringIO()
        curl = pycurl.Curl()
        curl.setopt(curl.URL, public_api_url)
        curl.setopt(curl.WRITEFUNCTION, output.write)
        curl.perform()
        curl.close()
        json_dict = json.loads(output.getvalue())
        return json_dict
        
    def connect_resource(self, resource):
        if not self.is_valid_resource(resource):
            raise NameError('Not a public resource: ' + resource)
        else:
            resource_id = self.resource_id(resource)
            return self.base_api + resource + '/' + resource_id
        
    def resource_id(self, resource):
        pass
        
    def is_valid_resource(self, resource):
        if resource in self.public_resources:
            return True
        else:
            return False
    
    
    