import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from util.file_helper import FileReader
basedir = os.path.dirname(os.path.abspath(__file__))
import pandas as pd
import numpy as np

class UsUnemployment:
    
    def __init__(self):
        self.reader = FileReader()
            
    def show_map(self):
        reader = self.reader
        reader.context = os.path.join(basedir, 'data')
        reader.fname = 'usa_map.json'
        reader.new_file()
        usa_map = reader.json_load()
        # print(f"usa_map Null Checker: {usa_map['State'].isnull()}")
        reader.fname = 'us_unemployment.csv'
        reader.new_file()
        us_unemployment = reader.csv_to_dframe()
        print(f'{us_unemployment.head()}')
        # return usa_map
    
if __name__ == '__main__':
    us = UsUnemployment()
    us.show_map()
    