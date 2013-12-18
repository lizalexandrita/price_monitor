# coding:utf-8

# Lib imports
import unittest
import jsongen as jgen
import json

class Test_jsongen(unittest.TestCase):
    def setUp(self):
        self.json_test = {"items": [{"item_id": "MLB520190799","price": [{"2013-12-17": 689.9}]}]}
        
    def test_json_update(self):
        ret = jgen.json_update("MLB520190799", "2013-12-17", 689.9)
        with open('mercado_libre/items.json') as f:
            data = json.load(f)
        self.assertEqual(data, self.json_test)





if __name__ == '__main__':
	unittest.main()
'''
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_api_connection)
	unittest.TextTestRunner(verbosity=2).run(suite)
#'''