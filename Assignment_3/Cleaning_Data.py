import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

walmart_path = 'Walmart.csv'

walmart_ori = pd.read_csv(walmart_path)
walmart = walmart_ori.copy()

walmart.head()

walmart.info()
