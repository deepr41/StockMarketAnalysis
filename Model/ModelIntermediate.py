import pickle

#Mode numbers 
#1 - Gradient Boosted Trees
#2 - ARIMA
#3 - ANN
from Model.GradientBoostedTrees import *
from Model.ARIMA import *
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
    pickle.dump(clf,open(path+"/"+name+"regressor.p",'wb'))
    pass

def trainModel(path,mode,X_train,y_train):
    name = customName(mode)
    clf = pickle.load(open(path+"/"+name+"regressor.pickle",'rb'))
    #TODO train logic
    if(mode == 1):
        #Code for GBT
        GBTTrain(clf,X_train,y_train)
        pickle.dump(xgb.plot_importance(clf),open(path+'/XGBimptGraph.p','wb'))
    elif(mode == 2):
        #Code for ARIMA
        ARIMATrain(clf,X_train)
    # elif(mode == 3):
    #     #code for ANN
    #     ANNTrain(clf,X_train,y_train)

    #TODO save it as a pickle file
    pickle.dump(clf,open(path+"/"+name+"regressor.pickle",'wb'))
    pass


def predictValues(path,mode,X_test):
    name = customName(mode)
    clf = pickle.load(open(path+"/"+name+"regressor.pickle",'rb'))
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
