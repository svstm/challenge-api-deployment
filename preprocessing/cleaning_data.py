
import pandas as pd

#preprocess()
# def preprocess(new_house :dict):
#     list_of_dict = new_house
#     df = pd.DataFrame.from_dict([list_of_dict])
#     df['area'] = df['new name of area']
#     return df
def preprocess(df):
    df["property_type"] = df["property_type"].replace('APARTMENT',1,regex=True)
    df["property_type"] = df["property_type"].replace('HOUSE',2,regex=True)
    df["property_type"] = df["property_type"].replace('OTHERS',3,regex=True)
    return df