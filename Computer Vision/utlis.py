#Step 1 import the data

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.utils import shuffle

#first step
# import data
def getName(filePath):
    return filePath.split('\\')[-1]

def importDataInfo(path):
    columns = ['Center', 'Left', 'Right', 'Steering', 'Throttle', 'Brake', 'Speed']
    data = pd.read_csv('D:\Computer Vision Files\driving_log.csv', names = columns)
    #### REMOVE FILE PATH AND GET ONLY FILE NAME
    #print(getName(data['center'][0]))
    data['Center']=data['Center'].apply(getName)
    print(data.head())
    print('Total Images Imported',data.shape[0])
    return data
path = 'myData'
data = importDataInfo(path)

print(data.head())
#second step
#balance the data and create data visualization
def balanceData(data,display=True):
    nBin = 31
    samplesPerBin = 1000
    hist, bins = np.histogram(data['Steering'], nBin)
    if display:
            center = (bins[:-1] + bins[1:]) * 0.5
            plt.bar(center, hist, width=0.06)
            plt.plot((np.min(data['Steering']), np.max(data['Steering'])), (samplesPerBin, samplesPerBin))
            plt.show()

#set a cutoff value then remove redundent data

    removeindexList = []
    for j in range(nBin):
        binDataList = []
        for i in range(len(data['Steering'])):
            if data['Steering'][i] >= bins[j] and data['Steering'][i] <= bins[j + 1]:
                binDataList.append(i)
        binDataList = shuffle(binDataList)
        binDataList = binDataList[samplesPerBin:]
        removeindexList.extend(binDataList)

    print('Removed Images:', len(removeindexList))
    data.drop(data.index[removeindexList], inplace=True)
    print('Remaining Images:', len(data))
    if display:
        hist, _ = np.histogram(data['Steering'], (nBin))
        plt.bar(center, hist, width=0.06)
        plt.plot((np.min(data['Steering']), np.max(data['Steering'])), (samplesPerBin, samplesPerBin))
        plt.show()

data = balanceData(data, display=True)


