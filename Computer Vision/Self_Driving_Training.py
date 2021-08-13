
from utlis import *
from sklearn.model_selection import train_test_split
#First Step
# import the data

path = 'Driving Data'
data = importDataInfo(path)

#second step
#balance the data and create data visualization
balanceData(data,display=False)


xTrain, xVal, yTrain, yVal = train_test_split(imagesPath, steerings, test_size=0.2,random_state=10)
print('Total Training Images: ',len(xTrain))
print('Total Validation Images: ',len(xVal))

#created CNN Model


model = createModel()
model.summary()

#fit the model
history = model.fit(batchGen(xTrain, yTrain, 10, 1),steps_per_epoch=30,epochs=10,
          validation_data=batchGen(xVal, yVal, 10, 0),validation_steps=20)

#save the model
model.save('model.h5')
print('Model Saved')
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.legend(['Training', 'Validation'])
plt.title('Loss')
plt.xlabel('Epoch')
plt.show()

