import pickle

#Mode numbers 
#1 - Gradient Boosted Trees
#2 - ARIMA
#3 - ANN
from Model.GradientBoostedTrees import GBTPredict,GBTRegressor,GBTTrain
from Model.ARIMA import ARIMAPredict,ARIMARegressor,ARIMATrain
from os.path import isfile
# from Model.ANN import *

#TODO create a method to access different types of classifier 

def customName(mode):
    if(mode == 1):
        name = "GBT"
    elif(mode == 2):
        name = "ARIMA"
    elif(mode == 3): 
        name = "ANN"
    return name

def createModel(path,mode):

    name = customName(mode)
    if(mode == 1):
        clf = GBTRegressor()
    elif(mode == 2):
        clf = ARIMARegressor()
    # elif(mode == 3):
    #     clf = ANNRegressor()
    if not (isfile(path+"/"+name+"regressor.p")):
        with open(path+"/"+name+"regressor.p",'wb') as file:
            pickle.dump(clf,file)
    

def trainModel(path,mode,X_train,y_train):
    name = customName(mode)
    if (isfile(path+"/"+name+"regressor.p")):
        with open(path+"/"+name+"regressor.p",'rb') as file:
            clf = pickle.load(file)
    else:
        print("Regressor not found")
        return
    if(mode == 1):
        #Code for GBT
        GBTTrain(clf,X_train,y_train)
    elif(mode == 2):
        #Code for ARIMA
        ARIMATrain(clf,X_train)
    # elif(mode == 3):
    #     #code for ANN
    #     ANNTrain(clf,X_train,y_train) 

    with open(path+"/"+name+"regressor.p",'wb') as file:
        pickle.dump(clf,file)
    pass


def predictValues(path,mode,X_test):
    name = customName(mode)
    if (isfile(path+"/"+name+"regressor.p")):
        with open(path+"/"+name+"regressor.p",'rb') as file:
            clf = pickle.load(file)
    else: 
        print("Regressor not found")
        return
    #TODO predict values and return it
    if(mode == 1):
        #Code for GBT
        val = GBTPredict(clf,X_test)
    elif(mode == 2):
        #Code for ARIMA
        ARIMAPredict(clf)
    # elif(mode == 3):
    #     #code for ANN
    #     ANNPredict(clf,X_test)
    #TODO create and save pickle from graphs

    #TODO calculate accuracy metrics and save it





    return val


def predictRealTime(path,mode,daysLength):
    #TODO load Classifier and data
    #TODO create prediction day by day , create a function for it
    pass
