import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))
import numpy as np
import tensorflow as tf 
import tensorflow_datasets as tfds
import tensorflow_hub as hub
import util.version_checker

class Saveload():
    
    train_images : object = None
    train_labels : object = None
    test_images : object = None
    test_labels : object = None
    
    def __init__(self):
        util.version_checker.env_info()
        
    def hook(self):
        self.get_data()
        self.create_model()
        self.train_model()
        self.debug_model()
        self.eval_model()
    
    def get_data(self):
        pass
    
    def create_sample(self) -> object:
        pass
    
    def create_model(self):
        pass
    
    def train_model(self):
        pass
    
    def eval_model(self):
        pass
    
    def debug_model(self):
        

if __name__ == '__main__':
    api = Saveload()
    api.hook()
    
    
        