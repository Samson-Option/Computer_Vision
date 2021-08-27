This is a self-driving car project. I used a self-driving simulator provided by Udacity(https://github.com/udacity/self-driving-car-sim). I first trained my car by using the simulator and then used Convolution neural networks CNN to train the model.

Here are the steps that I took.

Used the simulator to drive a car for about 10 laps on a map. This generated about 30,000 images (3 types for each, left, center, right, only center images were used) and 10,000 rows of data.
imported the data and image into python. Created utlis.py file to store all of my modules. packages used: import pandas as pd import numpy as np import os import matplotlib.pyplot as plt from sklearn.utils import shuffle
balanced the data. Because most routes were straight lines. Used matplotlib to draw a histogram. Set one bin size max=700. from Removed Images: 7793 and Remaining Images: 3026
Split the data into training and validation data set.
Deep learning use data augmentation so that we don't need a huge data set. Because the data have images, so I used imgaug package. Pan, zoom, brightness, and flip were used.
preprocessed the data and used OpenCV. Cropped the images and got out of the trees. Changed color space, so that the path is more clearer. Resized the images and normalized the images
Generated batches, 100 images/batch
Used Convolution neural network CNN to create a model. Used sequential model Adam optimizer. Used activation function elu rather than relu. There is a total of 5 convolutional layers, 1 Flaten layer, and 4 dense layers. Learning rate=0.0001. Loss function=mse
Saved the model. to h5
Tested the model by using the code provided by Udacity. Set the Max speed 10 mph and imported the model. Because the data was preprocessed in the training and validation parts, I also had to preprocess the data in the testing. Used the model to predict the steering angle.
