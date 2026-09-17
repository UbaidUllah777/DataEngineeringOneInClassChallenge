import pandas as pd
import numpy as np


class LoadSales:

    def __init__(self):
        print("Load Sales class created")

    def getSales(self):
        salesData = pd.read_csv('Data/retail_sales_ontario_synthetic.csv', low_memory=False)
        return salesData


    