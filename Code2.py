import csv
import plotly.express as px
import numpy as np

def getDataSource(data_path):
    size = []
    Avg_time = []
    with open(data_path) as f:
        df = csv.DictReader(f)
        for data in df:
            size.append(float(data["Marks In Percentage"])) 
            Avg_time.append(float(data["Days Present"]))    
        
        return {"x" : size , "y" : Avg_time}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source["y"])
    print(correlation[0,1])

def setup():
    data_path = "./Student Marks vs Days Present.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource) 

setup()