import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import datetime



def createGraphs(path,companyName):
    df = pd.read_csv(path+companyName +'/PredictedValues.csv')
    pred = df[-8:]
    real = df[:-7]
    real.index = real['Date']
    # print(real['Close'])
    plt.plot(real['Close'],label='Current')
    # plt.show()
    
    # Index dates correctly
    real[-1:]['Date'].iloc[0]
    startday = datetime.datetime.strptime(real[-1:]['Date'].iloc[0],"%Y-%m-%d")
    arr = []
    for i in range(0,8):
        
        for i in range(0,3):
            if (startday.isoweekday()==6 or startday.isoweekday()==7):
                startday =startday +  datetime.timedelta(days = 1)
            else:
                break
        arr.append([str(startday.date())])
        startday =startday +  datetime.timedelta(days = 1)
    datesFrame = (pd.DataFrame(arr,columns=['Date']))
    pred.index=datesFrame['Date']

    plt.plot(pred['Close'],label = 'Predicted')
    plt.ylabel('Close')
    plt.xlabel('Date')
    # plt.locator_params(numticks = 1)
    plt.title(companyName)
    plt.legend()

    plt.xticks([0,4,8,12,14])
    plt.savefig(path+companyName+'/Future.png')    
    # plt.show()
    plt.close()





def createPiChart():
    
    pass


def main():
    for i in os.listdir("./Data/"):
        print(i)
        createGraphs("./Data/",i)
        # break
        
    

if __name__ == '__main__':
    main()