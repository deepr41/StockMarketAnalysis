#import libraries
import numpy as np
import pandas as pd
import sys
import os
#import data from csv fill



def formatData(fileName):
    def findEMA(TimeInterval,finalName,feature):
        emaMultiplier = 2/(TimeInterval+1)
        EMAlist = [np.NAN]*(TimeInterval-1)
        for i in range(TimeInterval-1,len(df)):
            initialEMA = np.sum(feature[i-TimeInterval+1:i+1])
            #print(initialEMA)

            #initialEMA = 0
            #for j in range(0,TimeInterval):
                #initialEMA = initialEMA + df[myIndexes[4]][i-j]
            EMA = [initialEMA]
            for j in range(0,TimeInterval):
                tempEMA = (feature[i-(TimeInterval-j)+1]-EMA[-1])*emaMultiplier + EMA[-1]
                EMA.append(tempEMA)
            EMAlist.append(EMA[-1])
            #print(EMA)
        df[finalName] = EMAlist
    df = pd.read_csv("Data/Raw/"+fileName)
    #try:
    #    df.drop(columns=["Unnamed: 0"],inplace=True)
    #except:
    #    print("No Unamed column")
    myIndexes = df.columns
    #df.dropna(inplace=True)+


    #myIndexes
    #0 - Date
    #1 - Open
    #2 - High
    #3 - Low
    #4 - Close
    #5 - Volume
    #6 - Adjusted

    #Feature 1 : RSI (Relative Strength Index)
    #RSI computes the relative strength index of a stock
    #Relative Strength (RS)= Avg of x up days/ Avg of x down days
    #RSI = 100-100/(1+RS)
    #Standard time period to calculate RSI is 14 days

    rsiInternalLength = 14

    df['Diff'] = df[myIndexes[4]] - df[myIndexes[4]].shift(+1)

    temp = [np.NAN]*rsiInternalLength
    for i in range(rsiInternalLength,len(df)):
        upcount = 0
        downcount = 0
        upsum = 0
        downsum = 0 
        for j in range(0,rsiInternalLength):
            if(df['Diff'][i-j]<0):
                downcount=downcount+1
                downsum = downsum + df[myIndexes[4]][i-j]
            else:
                upcount=upcount+1
                upsum = upsum + df[myIndexes[4]][i-j]
        try:
            rsUP = upsum/upcount
            rsDW = downsum/downcount
            
            rs = np.float64(100)-(np.float64(100)/(np.float64(1)+rsUP/rsDW))
            
            
            temp.append(rs)
        except:
            temp.append(np.NAN)
    #df.drop(columns='Diff',inplace=True)
    df['RSI'] = temp
    #Feature 2 : Money Flow Index (MFI)
    #The Money Flow Index (MFI) is an oscillator that uses both price and volume to measure buying and selling pressure. 
    #Typical Price = (High + Low + Close)/3
    #Raw Money Flow = Typical Price x Volume
    #Money Flow Ratio = (14-period Positive Money Flow)/(14-period Negative Money Flow)
    #Money Flow Index = 100 - 100/(1 + Money Flow Ratio)
    #1 - High, 2 - Low, 3 - Close

    mfiInternalLength = 14

    typicalPriceList = []
    rawMoneyFlowList = []

    for i in range(0,len(df)):
        tempTypical = (df[myIndexes[2]][i]+df[myIndexes[3]][i]+df[myIndexes[4]][i])/np.float64(3)
        typicalPriceList.append(tempTypical)
        rawMoneyFlowList.append(tempTypical * df[myIndexes[5]][i])
    df['Typical Price'] = typicalPriceList
    df['MF'] = rawMoneyFlowList


    mfiList = [np.NAN]*mfiInternalLength
    for i in range(mfiInternalLength,len(df)):
        pos = 0
        neg = 0
        possum = 0
        negsum = 0 
        for j in range(0,mfiInternalLength):
            if(df['Diff'][i-j]<0):
                neg=neg+1
                negsum = negsum + df['MF'][i-j]
            else:
                pos=pos+1
                possum = possum + df['MF'][i-j]
        try:
            mrUP = possum/pos
            mrDW = negsum/neg
            rs = np.float64(100)-(np.float64(100)/(np.float64(1)+mrUP/mrDW))
            mfiList.append(rs)
        except:
            mfiList.append(np.NAN)
    df['MFI'] = mfiList


    #Feature 3 : Exponential Moving Average (EMA)
    #Moving averages smooth the price data to form a trend following indicator.
    #Despite this lag, moving averages help smooth price action and filter out the noise.
    #Exponential moving averages (EMAs) reduce the lag by applying more weight to recent prices.
    #Initial SMA: 10-period sum / 10 
    #Multiplier: (2 / (Time periods + 1) ) = (2 / (10 + 1) ) = 0.1818 (18.18%)
    #EMA: {Close - EMA(previous day)} x multiplier + EMA(previous day). 

    emaTimeInterval = 10
    findEMA(emaTimeInterval,'EMA',df[myIndexes[4]])


    #Feature 4 : Stocastic oscillator
    #Stochastic Oscillator is a momentum indicator that shows the location of the close relative to the 
    #high-low range over a set number of periods.
    #Default time peroid is 14 days but 7 days is used here
    #SO = (Current Close - Lowest Low)/(Highest High - Lowest Low) * 100

    soTimeInterval = 7

    soList = [np.NAN]*6
    for i in range(soTimeInterval-1,len(df)):
        close = df[myIndexes[4]][i]
        high=[]
        low=[]
        #high = np.max(df[myIndexes[2]][i-soTimeInterval:i+1])
        #low = np.min(df[myIndexes[3]][i-soTimeInterval:i+1])
        
        for j in range(0,soTimeInterval):
            high.append(df[myIndexes[2]][i-(soTimeInterval-j)+1])
            low.append(df[myIndexes[3]][i-(soTimeInterval-j)+1])
        high = np.max(high)
        low = np.min(low)
        tempSO = (close-low)/(high-low)
        soList.append(tempSO)
    #print(len(soList),len(df))
    df['SO'] = soList

    #Feature 5 : Moving Average Convergence/ Divergence
    #MACD Line: (12-day EMA - 26-day EMA)

    #Signal Line: 9-day EMA of MACD Line

    #MACD Histogram: MACD Line - Signal Line
    findEMA(12,'EMA12',df[myIndexes[4]])
    findEMA(26,'EMA26',df[myIndexes[4]])


    df['MACD'] = df['EMA12']-df['EMA26']
    findEMA(9,'Signal Line',df['MACD'])

    #Reminder MACD, Signal line
    data = (df[['Date','RSI','MFI','EMA','SO','MACD','Diff',myIndexes[4]]])
    data = data.dropna()
    data = data.reset_index()
    data = data.drop(columns=['index'])

    data.to_csv("./Data/Formatted/"+fileName[:-7]+"formattedData.csv")
    # print(data)


def main():
    args = args = os.listdir("./Data/Raw")
    for i in args:
        formatData(i)
        print(i)
        # print("Data formattedData",args[i])


main()