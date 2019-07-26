from sklearn.neural_network import MLPClassifier
import pandas as pd
import numpy as np
import joblib



def train_neuralnet(X_train,y_train):
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 2), random_state=1)
    clf.fit(X_train,y_train)
    print(clf.score(X_train,y_train))
    return clf

def save_model(model):
    joblib.dump(model, 'saved_model.pkl') 
    
def test_neuralnet(clf,X_test,y_test):
    print(clf.score(X_test,y_test))


if __name__ =='__main__':
    data = pd.read_csv("data_set.csv") 
    msk = np.random.rand(len(data)) < 0.6
    train = data[msk]
    test = data[~msk]

    train_y = train.pop('hit')
    train_x = train
    
    test_y = test.pop('hit')
    test_x = test

    model = train_neuralnet(train_x,train_y)
    save_model(model)



