from dataclasses import dataclass
import pandas as pd
import os

"""
context: /Users/youngseonkim/Documents/SbaProjects/
fname: /titanic/data
"""
@dataclass
class FileReader:
    
    context : str = ''
    fname: str = ''
    train: object = None
    test: object = None
    id: str = ''
    label: str = ''
    
    def new_file(self) -> str:
        return os.path.join(self.context, self.fname)
    
    def csv_to_dframe(self) -> object:
        file = self.new_file()
        return pd.read_csv(file, encoding='utf-8', thousands=',')
    
    