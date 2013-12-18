# coding:utf-8

# Lib imports
import unittest
import api_connection as api_conn
import data_monitor as datam

# ------------------------------------------------------------------------------

class Test_prod_status(unittest.TestCase):
    def setUp(self):
        self.last_date = "2013-12-18 16:36"
        self.product_id = 'MLB520190799'
        self.product_id_not_found_test = 'MLB00000000'
        
    def test_prod_status(self):
        ret = datam.prod_status(self.product_id)
        ret2 = datam.prod_status(self.product_id_not_found_test)
        self.assertEqual(ret, self.last_date)
        self.assertEqual(ret2, ("error: not_found","cause: "+ ",".join([])))


class Test_data_monitor(unittest.TestCase):
    
    def setUp(self):
        self.price = datam.price()
        self.product_id = 'MLB520190799'
        
    def test_last(self):
        ret = self.price.last(self.product_id)
        self.assertEqual(ret,689.9)
    
    def test_compare(self):
        ret = self.price.compare(90,100)
        self.assertEqual(round(ret,1), round(-0.1,1))
        
        
if __name__ == '__main__':
	unittest.main()
'''
	suite = unittest.TestLoader().loadTestsFromTestCase(Test_api_connection)
	unittest.TextTestRunner(verbosity=2).run(suite)
#'''