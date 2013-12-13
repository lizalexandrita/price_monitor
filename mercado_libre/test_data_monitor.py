# coding:utf-8

# Lib imports
import unittest
import api_connection as api_conn
import data_monitor as data_monitor

# ------------------------------------------------------------------------------

class Test_data_monitor(unittest.TestCase):
    
    def setUp(self):
        self.price = data_monitor.price()
        
    def test_last(self):
        pass
    
    def test_target_comp(self):
        pass
    
    def test_db_comp(self):
        pass