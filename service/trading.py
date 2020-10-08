import numpy as np
import math
import pandas_datareader as data_reader

class Trading:
    @staticmethod
    def sigmoid(x):
        return 1 / (1 + math.exp(-x))
    @staticmethod
    def stocks_price_format(n):
        if n < 0:
            return "- $ {0:2f}".format(abs(n))
        else:
            return "$ {0:2f}".format(abs(n))
    @staticmethod
    def dataset_loader(stock_name):
        dataset = data_reader.DataReader(stock_name, data_source="yahoo")
        start_date = str(dataset.index[0]).split()[0]
        end_date = str(dataset.index[-1]).split()[0]
        close = dataset['Close']
        return close
    def state_creator(self,data, timestep, window_size):
        starting_id = timestep - window_size + 1
        if starting_id >= 0:
            windowed_data = data[starting_id: timestep + 1]
        else:
            windowed_data =- starting_id * [data[0]] + list(data[0:timestep + 1])
        state = []
        for i in range(window_size - 1):
            state.append(self.sigmoid(windowed_data[i + 1] - windowed_data[i]))
        return np.array([state])
        
        
    
        