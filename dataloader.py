from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd

def __get_data():
    dataset= load_breast_cancer(as_frame=True)
    return dataset

def get_data_scaled():
    dataset= load_breast_cancer()
    scaler=StandardScaler()
    data=dataset.data
    data=scaler.fit_transform(data)
    print(data[:,0].std())
    return data,dataset.target



def test():
     
    data,t=get_data_scaled()

    print(data)
    print(t)




    

    
    
if __name__ == '__main__':
    test()