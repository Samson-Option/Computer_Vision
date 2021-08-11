
from utlis import *
#First Step
# import the data

path = 'Driving Data'
data = importDataInfo(path)


#second step
#balance the data and create data visualization
data=balanceData(data,display=True)