import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from util.file_helper import FileReader
basedir = os.path.dirname(os.path.abspath(__file__))
from model.police import Police

class CrimeMap():
    
    def __init__(self):
        print(f'baseurl #### {basedir}')
        self.reader = FileReader()

        
    def hook__process(self):
        police = Police()
        police_norm = police.get_police_norm()