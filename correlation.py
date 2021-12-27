import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    size = []
    Avg_time = []
    with open(data_path) as f:
        df = csv.DictReader(f)
        for data in df:
            size.append(float(data["Size of TV"])) 
            Avg_time.append(float(data["\tAverage time spent watching TV in a week (hours)"]))    
        
        return {"x" : size , "y" : Avg_time}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print(correlation[0,1])

def setup():
    data_path = "./TV.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource) 

setup()









