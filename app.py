
from typing import Union
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request, status
from pydantic import BaseModel
from typing import Optional
from predict.hello import say_hello
import pandas as pd
from predict.prediction import predict
from preprocessing.cleaning_data import preprocess

app = FastAPI() 

#uvicorn app:app --reload

@app.get("/")
def read_root():
    return {"Alive": "Alive"}

@app.get("/predict")
def read_root():
    return ("Put in json file ") 

# "APARTMENT" | "HOUSE" | "OTHERS"

class Item(BaseModel):
    area: int
    property_type: str
    rooms_number: int
    zip_code: int 
    land_area: Optional[int] 
    garden: Optional[bool] = None
    garden_area: Optional[int] = None
    equipped_kitchen: Optional[bool] = None
    full_address: Optional[str] = None
    swimming_pool: Optional[bool] = None
    furnished: Optional[bool] = None
    open_fire: Optional[bool] = None
    terrace: Optional[bool] = None
    terrace_area: Optional[int] = None
    facades_number: Optional[int] = None
    building_state: Optional[str] = None




@app.post("/post")
def create_item(item: Item):
    print('in')
    data = {"Living area (m²)":[item.area],
                #"property_type":[item.property_type],
                'Zip code':[item.zip_code], 
               'Terrace surface (m²)':[item.terrace_area]
               } 
    results = predict(data)
    print('res ', results)
    print('res ', type(results))
    results_dict = {"prediction": list(results)}
    print('res dict', results_dict)
    print('res dict', type(results_dict))
    return     results_dict

@app.post("/t2")
def some_name(varaibe: Item):
    return say_hello(varaibe)

@app.post("/testurl")
def some_name(varaibe: Item):
    return say_hello(varaibe)

@app.get("/t1")
def some_func(Name_of_var:Item):
    return preprocess(Name_of_var)

