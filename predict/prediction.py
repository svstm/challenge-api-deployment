import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle 
from preprocessing.cleaning_data import preprocess

with open("model/model.pkl", 'rb') as file: 
        pickle_model = pickle.load(file)


def predict(X, model=pickle_model):
    print(X)
    
    X1 = pd.DataFrame.from_dict(X)
    
    Y_hat = model.predict(X1) 
    return Y_hat