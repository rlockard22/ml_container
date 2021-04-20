from os import name
from sklearn import datasets
from joblib import load
import numpy as np
import json


#load the model

my_model = load('my_model.pkl')

log_model = load('log_model.pkl')

e_model = load('ensemble.pkl')


labels = np.array(['Alive', 'Dead'])

def predict(features):
    feats = np.array(features)
    feats = feats.reshape(1,-1)
    log_pred = log_model.predict(feats)
    int_log_pred = log_pred.astype(int)
    out = labels[int_log_pred]
    prediction = my_model.predict(feats)
    prediction = prediction.astype(int)
    name = labels[prediction]
    e_pred = e_model.predict(feats)
    int_e_pred = e_pred.astype(int)
    yep = labels[int_e_pred]
    if yep[0] == 'Alive':
        return yep[0]
    elif out[0] == 'Alive':
       return out[0]
    elif name[0] == 'Alive':
       return name[0]
    else:
       return 'Dead'




#def stats():
    my_str = 'True Positives: 40\n' + 'False Positives: 9\n' + 'False Negatives: 3\n' 
    + 'True Negatives: 44\n' + 'Accuracy: 0.8537\n' + 'Precision: .8163\n' + 'Recall: .9302\n'
    'F1 Score: .8695\n'
    return(my_str)
    
    




#test_prediction = [0,0,0,0,0,0,0,0,0,0,0,0]
#living_prediciton = [60,1,156,1,25,1,318000,1.2,137,0,0,85]
#x = predict(test_prediction)
#y = predict(living_prediciton)

#print(x)
#print(y)
