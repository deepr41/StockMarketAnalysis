from Model.BasicSVMModel import myClassifer,myTrain,mypredict
import numpy as np		
import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from Model.ModelIntermediate import createModel,predictValues,trainModel
from Model.Regularizer import regularize,initRegularize
from Model.preprocessing import prepareData


predictRange = 7

def sampleGBT(predictRange,companyName):
	print(predictRange,companyName)
	df = pd.read_csv("./Data/"+companyName+"/Data.csv")
	df.dropna(inplace=True)
	# df.reset_index(inplace=True)
	df.reset_index(inplace=True)
	try:
		df.drop(columns=['Unnamed: 0'],inplace=True)
		df.drop(columns=['index'],inplace=True)
	except:
		pass
	myindex = df.columns
	df1 = prepareData(df,1)
	y = df['Diff']


	initRegularize("./Data/"+companyName,df1)
	df2 = regularize("./Data/"+companyName,df1)



	X_train = np.array(df2[:-predictRange])
	y_train = np.array(y[:-predictRange])
	X_test = np.array(df2[-predictRange:])
	# y_test = np.array(y[-predictRange:])
	#Normalize data



	# Training
	createModel("./Data/"+companyName,1)
	trainModel("./Data/"+companyName,1,X_train,y_train)
	yPredicted = predictValues("./Data/"+companyName,1,X_test)
	#Finds the Correct ClosePrices

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
	
	# plt.clf
	#plot Data
	plt.close()
	plt.plot(df['Date'][-predictRange*2:], acutalClose[-predictRange*2:], color='navy', label='Actual')

	plt.plot(df['Date'][-predictRange*2:], predictedClose[-predictRange*2:], color='darkorange',  label='Predicted')
	# ax.fill_between(df['Date'][-predictRange*2:], predictedClose[-predictRange*2:], alpha=.3)

	plt.xlabel('Date')
	plt.ylabel('Close')
	plt.title(companyName[:-17])
	plt.legend()
	# fig.savefig("./Data/"+companyName+"/Figure.png")
	plt.savefig("./Data/"+companyName+"/Example.png")
	plt.close()
	

def main():
	args = os.listdir("./Data/")
	for i in args:
		sampleGBT(predictRange,i)
		# print("./Data/"+i+"/Data.csv")
		# print("lol")


main()