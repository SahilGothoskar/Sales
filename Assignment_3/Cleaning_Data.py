import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

walmart_path = 'D:\DMDD\Assignment 3\Walmart.csv'

walmart_ori = pd.read_csv(walmart_path)
walmart = walmart_ori.copy()

walmart.head()

walmart.info()