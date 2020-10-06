import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
 
import pandas as pd
import numpy as np

basedir = os.path.dirname(os.path.abspath(__file__))

class Crime:
    def __init__(self):
        pass
    
    def read_file(self):
        cctv_seoul = pd.read_csv(os.path.join(basedir,'data','cctv_in_seoul.csv'))
        print(cctv_seoul.head())
        print('#' * 50)
        print(cctv_seoul.tail)
        print('#' * 50)
        print(cctv_seoul.sort_values(by='소계', ascending=True))

        print('#' * 50)
        
        crime_seoul = pd.read_csv(os.path.join(basedir,'data','crime_in_seoul.csv'))
        print(crime_seoul.head())
        
if __name__ == '__main__':
    t = Crime()
    t.read_file()
    