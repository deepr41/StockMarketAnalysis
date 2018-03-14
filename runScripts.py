import os

def runFetchData():
	os.system('Rscript GetCleanData.R')


def cleanFectedData():
	os.system('python formatScript.py')

def GetData():
	runFetchData()
	cleanFectedData()

# if __name__ == '__main__':
	

# main()