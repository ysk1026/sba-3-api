import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from util.file_helper import FileReader
basedir = os.path.dirname(os.path.abspath(__file__))
import pandas as pd

# class Crime:
#     def __init__(self):
#         pass
    
#     def read_file(self):
#         cctv_seoul = pd.read_csv(os.path.join(basedir,'data','cctv_in_seoul.csv'))
#         print(cctv_seoul.head())
#         print('#' * 50)
        
        
#         print(cctv_seoul.sort_values(by='소계', ascending=True))

#         print('#' * 50)
        
#         crime_seoul = pd.read_csv(os.path.join(basedir,'data','crime_in_seoul.csv'))
#         print(crime_seoul.head())
        
# if __name__ == '__main__':
#     t = Crime()
#     t.read_file()
    


class Crime:
    def __init__(self):
        print(f'basedir ####{basedir}')
        self.reader = FileReader()
    
    def get_crime(self):
        reader = self.reader
        reader.context = os.path.join(basedir,'data')
        reader.fname = 'crime_in_seoul.csv'
        # reader.new_file()
        crime = reader.csv_to_dframe()
        print(f'{crime.head()}')
        return crime
    
    def hook_process(self):
        print('---------- CRIME & POLICE ----------')
        crime = self.get_crime()
        self.get_station(crime)
        
    
    def get_station(self, crime):
        reader = self.reader
        station_names = []
        for name in crime['관서명']:
            station_names.append('서울' + str(name[:-1] + '경찰서'))
        station_addrs = []
        station_lats = [] # 위도
        station_lngs = [] # 경도
        gmaps = reader.create_gmaps()
        for name in station_names:
            t = gmaps.geocode(name, language='ko')
            station_addrs.append(t[0].get('formatted_address'))
            t_loc = t[0].get('geometry')
            station_lats.append(t_loc['location']['lat'])
            station_lngs.append(t_loc['location']['lng'])
            print(name+'-------->' + t[0].get('formatted_address'))
            
    
if __name__ == '__main__':
    crime = Crime()
    crime.hook_process()