from mlmodel import *
import numpy as np
import pandas as pd
import os
# from _thread import start_new_thread	
import matplotlib.pyplot as plt
from sklearn import preprocessing

# import seaborn as sns

from runScripts import GetData
# GetData()
# sns.set_style("whitegrid")
# blue, = sns.color_palette("muted", 1)

predictRange = 200

def drawPredict(predictRange,fileName):
	print(predictRange,fileName)
	df = pd.read_csv("./Data/Formatted/"+fileName)
	df.dropna(inplace=True)
	df.drop(columns=['Unnamed: 0'],inplace=True)
	myindex = df.columns
	X = df[['RSI',"MFI",'EMA','SO','MACD']]
	y = df['Diff']

	preprocessing.normalize(X)

	X_train = np.array(X[:-predictRange])
	y_train = np.array(y[:-predictRange])
	X_test = np.array(X[-predictRange:])
	y_test = np.array(y[-predictRange:])
	#Normalize data



	#Training
	cls = myClassifer()
	myTrain(cls,X_train,y_train)
	yPredicted = mypredict(cls,X_test)
	#Finds the Correct ClosePrices
	print(X_test)
	print(yPredicted)
	acutalClose = [np.NAN]
	predictedClose = [np.NAN]
	pro = len(df)-predictRange
	for i in range(1,len(df)):
	    tempAcutal = df[myindex[-1]][i-1]+df['Diff'][i]
	    acutalClose.append(tempAcutal)
	    if(i>=pro):
	        
	        tempPre = predictedClose[i-1]+yPredicted[i-pro]
	    else:
	        tempPre = df[myindex[-1]][i-1]+df['Diff'][i]
	    predictedClose.append(tempPre)

	# for i in range(0,predictRange):
	#     print((df['Diff'][len(df)-predictRange+i]),yPredicted[i])  
	
	    
	#plot Data
	plt.plot(df['Date'][-predictRange*2:], acutalClose[-predictRange*2:], color='navy', label='Actual')

	plt.plot(df['Date'][-predictRange*2:], predictedClose[-predictRange*2:], color='darkorange',  label='Predicted')
	# ax.fill_between(df['Date'][-predictRange*2:], predictedClose[-predictRange*2:], alpha=.3)

	plt.xlabel('Date')
	plt.ylabel('Close')
	plt.title(fileName[:-17])
	plt.legend()
	plt.show()

def main():
	args = os.listdir("./Data/Formatted")
	for i in args:
		drawPredict(predictRange,i)


main()