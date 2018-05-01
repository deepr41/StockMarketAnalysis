from Model.ModelIntermediate import *
import os
# import pickle
# from os.path import isfile
# import numpy as np
# import pandas as pd
# import csv
# from Model.GradientBoostedTrees import GBTPredict, GBTRegressor, GBTTrain
# from Model.preprocessing import prepareData
# from Model.Regularizer import regularize
# from Model.formatScript import findRSI,findMFI,findEMA,findMACD,findSO
from Model.Regularizer import *

def main():
    args = os.listdir("./Data/")
    for i in args:
        print(i)
        df = pd.read_csv("./Data/"+i+"/Data.csv")
        df.dropna(inplace=True)
        # df.reset_index(inplace=True)
        df.reset_index(inplace=True)
        try:
            df.drop(columns=['Unnamed: 0'],inplace=True)
            df.drop(columns=['index'],inplace=True)
        except:
            pass
	
        y = df['Diff']
        df = prepareData(df,1)
        initRegularize("./Data/"+i,df)
        df1 = regularize('./Data/'+i,df)
        trainModel("./Data/"+i,1,df1,y)


        predictRealTime("./Data/"+i,1,7)
        

if __name__ == '__main__':
    main()

