import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from model.perceptron import Perceptron

class IrisModel:
    def __init__(self):
        df = pd.read_csv('https://archive.ics.uci.edu/ml/'
        'machine-learning-databases/iris/iris.data', header=None)
        print(df.head())
        print('-' * 50)
        print(df.tail)   
        print('-' * 50)
        print(df.columns)
        '''
        [150 rows x 5 columns]>
        --------------------------------------------------
        Int64Index([0, 1, 2, 3, 4], dtype='int64')
        '''
        
        # Iris-setosa 와 versicolor 선택 (MCP 는 이진분류만 할 수 있다)
        t = self.iris.iloc[0:100, 4].values
        self.y = np.where(t == 'Iris-setosa', -1, 1)
        # 꽃받침 길이, 꽃잎 추출
        self.x = self.iris.iloc[0:100, [0,2]].values
        self.clf = Perceptron(eta = 0.1, n_iter=10)
    
    def get_iris(self):
        return self.iris
    
    def get_X(self):
        return self.X
    
    def get_y(self):
        return self.y
    
    def draw_scatter(self):
        X = self.X
        plt.scatter(X[:50, 0], X[:50, 1], color = 'red', marker='o', label = 'setosa')
        plt.scatter(X[50:100, 0], X[50:100, 1], color = 'blue', marker='x', label = 'versicolor')
        plt.xlabel('sepal length[cm]')
        plt.ylabel('petal length[cm]')
        plt.legend(loc = 'upper left')
        plt.show()
        
    def draw_errors(self):
        X = self.X
        y = self.y
        self.clf.fit(x, y)
        plt.plot(range(1, len(self.clf.errors_) + 1), self.clf.errors_, marker='o')
        plt.xlabel('Epoch')
        plt.ylabel('Number of Errors')
        plt.show() 