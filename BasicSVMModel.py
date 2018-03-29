import numpy as np
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.datasets import make_classification
# from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor





# def myClassifer():
# 	classifier = svm.SVR(kernel='rbf', C=1e3, gamma=0.1)
# 	return classifier


# def myTrain(cls,X_train,y_train):
	
# 	cls.fit(X_train,y_train)


# def mypredict(cls,X):
# 	y = cls.predict(X)
# 	return y


def myClassifer():
	clf = RandomForestRegressor(max_depth=2, random_state=0)
	# clf = SVR(kernel='rbf', C=1e3, gamma=0.1)
	return clf

def myTrain(cls,X,y):
	cls.fit(X,y)


def mypredict(cls,X):
	y = cls.predict(X)
	return y