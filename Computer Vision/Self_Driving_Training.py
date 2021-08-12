
from utlis import *
#First Step
# import the data

path = 'Driving Data'
data = importDataInfo(path)


#second step
#balance the data and create data visualization


from sklearn.model_selection import train_test_split
xTrain, xVal, yTrain, yVal = train_test_split(imagesPath, steerings, test_size=0.2,random_state=10)
print('Total Training Images: ',len(xTrain))
print('Total Validation Images: ',len(xVal))