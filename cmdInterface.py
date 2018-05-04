import os

def main():
    print('Menu')
    print("1. Fetch Data")
    print("2. Clean Data")
    print("3. Run sample GBTmodel")
    print("4. Run real time prediction")
    print("5. Exit")

    choice = int(input("Enter your choice:"))
    if(choice==1):
        os.system("python Scripts/createMeta.py")
    elif(choice==2):
        os.system("python Model/formatScript.py")
    elif(choice==3):
        os.system("python SampleRunModel.py")
    elif(choice==4):
        os.system("python RealTimePredict.py")
        os.system("python Model/PostPred.py")
    elif(choice==5):
        quit()
    elif(choice==10):
        os.system("python Scripts/createMeta.py")
        os.system("python Model/formatScript.py")
        os.system("python SampleRunModel.py")
        os.system("python RealTimePredict.py")
        os.system("python Model/PostPred.py")
    else:
        print("Invalid option")

if __name__ == '__main__':
    while(True):
        main()