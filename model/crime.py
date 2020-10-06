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
    


class CrimeModel:
    def __init__(self):
        print(f'baseurl #### {basedir}')
        self.reader = FileReader()

    def hook_process(self):
        print('----------- CRIME & POLICE ----------')
        crime = self.get_crime()
        print(f'{crime.head()}')
        self.get_station(crime)


    def get_crime(self):
        reader = self.reader
        reader.context = os.path.join(basedir,'data')
        reader.fname = 'crime_in_seoul.csv'
        reader.new_file()
        crime = reader.csv_to_dframe()
        return crime

    def get_station(self, crime):
        reader = self.reader
        station_names = []
        for name in crime['관서명']:
            station_names.append('서울'+str(name[:-1]+'경찰서'))
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
            print(name+'----->' + t[0].get('formatted_address'))
        gu_names = []

        for name in station_addrs:
            t = name.split()
            gu_name = [gu for gu in t if gu[-1] == '구'][0]
            gu_names.append(gu_name)
        crime['구별'] = gu_names
        print('+++++++++++++++++++++')
        

        crime.loc[crime['관서명'] == '혜화서', ['구별']] == '종로구'
        crime.loc[crime['관서명'] == '서부서', ['구별']] == '은평구'
        crime.loc[crime['관서명'] == '강서서', ['구별']] == '양천구'
        crime.loc[crime['관서명'] == '종암서', ['구별']] == '성북구'
        crime.loc[crime['관서명'] == '방배서', ['구별']] == '서초구'
        crime.loc[crime['관서명'] == '수서서', ['구별']] == '강남구'

        print(crime.head())
        reader = self.reader
        reader.context = os.path.join(basedir,'saved_data')
        reader.fname = 'crime_police.csv'
        crime.to_csv(reader.new_file())


    


if __name__ == '__main__':
    crime = CrimeModel()
    crime.hook_process()
    