import numpy as np
from sklearn import svm




def myClassifer():
	classifier = svm.SVR(kernel='rbf', C=1e3, gamma=0.1)
	return classifier


def myTrain(cls,X_train,y_train):

	cls.fit(X_train,y_train)


def mypredict(cls,X):
	y = cls.predict(X)
	return y


