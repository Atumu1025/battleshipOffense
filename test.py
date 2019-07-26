from sklearn.neural_network import MLPClassifier
import pandas as pd
import numpy as np
import joblib

def test_neuralnet(clf,X_test,y_test):
    print(clf.score(X_test,y_test))


if __name__ =='__main__':
    data = pd.read_csv("data_set.csv") 
    msk = np.random.rand(len(data)) < 0.6
    train = data[msk]
    test = data[~msk]
    
    test_y = test.pop('hit')
    test_x = test

    clf_load = joblib.load('saved_model.pkl') 
    test_neuralnet(clf_load,test_x,test_y)