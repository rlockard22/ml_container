from sklearn import datasets
from joblib import load
import numpy as np
import json

#load the model

my_model = load('my_model.pkl')


labels = np.array(['Alive', 'Dead'])

def predict(features):
    feats = np.array(features)
    feats = feats.reshape(1,-1)
    prediction = my_model.predict(feats)
    prediction = prediction.astype(int)
    name = labels[prediction]
    
    
    return name[0]

#test_prediction = [0,0,0,0,0,0,0,0,0,0,0,0]
#living_prediciton = [60,1,156,1,25,1,318000,1.2,137,0,0,85]
#x = predict(test_prediction)
#y = predict(living_prediciton)

#print(x)
#print(y)
