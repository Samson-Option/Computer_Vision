This is a self-driving car project. I used a self-driving simulator provided by Udacity(https://github.com/udacity/self-driving-car-sim). I first trained my car by using the simulator and then used Convolution neural networks CNN to train the model. 

Here are the steps that I took.
1. Used the simulator to dirve a car for about 10 laps in a map. This generated about 30,000 images (3 types for each, left, center, right, only center images were used) and          10,000 rows of data. 
2. imported the data and image into python. Created utlis.py file to store all of my modules. 
   packages used:
   import pandas as pd
   import numpy as np
   import os
   import matplotlib.pyplot as plt
   from sklearn.utils import shuffle
 3. banlanced the data. Becuase most routes were straight lines. Used matplotlib to draw a histgram. Set one bin size max=700. from Removed Images: 7793 and Remaining Images: 3026
