import pandas as pd
import numpy as np

#import matplotlib.pyplot as plt

walmart_path = 'D:\DMDD\Assignment 3\myCity.csv'

walmart_ori = pd.read_csv(walmart_path)
walmart = walmart_ori.copy()

walmart.head()

walmart.info()


def missing_cols(walmart):
    '''prints out columns with its amount of missing values'''
    total = 0
    for col in walmart.columns:
        missing_vals = walmart[col].isnull().sum()
        total += missing_vals
        if missing_vals != 0:
            print(f"{col} => {walmart[col].isnull().sum()}")
    
    if total == 0:
        print("no missing values left")
            
missing_cols(walmart)


import csv
import pandas as pd

csv.register_dialect('myDialect', delimiter=' ', doublequote=True, quoting=csv.QUOTE_NONE, skipinitialspace='True')

f = open("D:\DMDD\Assignment 3\myCity.csv", 'r')
f = f.read().replace('“', '').replace('”', '').splitlines()
normal = csv.reader(f, dialect='myDialect')

for data in normal:
    print(data, len(data))

df = pd.DataFrame(normal.data,
                  columns = normal.feature_names)

display(df)