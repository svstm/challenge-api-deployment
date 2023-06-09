
import pandas as pd

def preprocess(df):
    df["property_type"] = df["property_type"].replace('APARTMENT',1,regex=True)
    df["property_type"] = df["property_type"].replace('HOUSE',2,regex=True)
    df["property_type"] = df["property_type"].replace('OTHERS',3,regex=True)
    return df