
# from typing import Union
# from fastapi import FastAPI
# from fastapi import HTTPException
# from fastapi.responses import JSONResponse
# from fastapi import FastAPI, Request, status
# from pydantic import BaseModel
# from typing import Optional
# from predict.hello import say_hello
# import pandas as pd
# from predict.prediction import predict
# from preprocessing.cleaning_data import preprocess

# app = FastAPI()

# #uvicorn app:app --reload

# @app.get("/")
# def read_root():
#     return {"Alive": "Alive"}

# @app.get("/predict")
# def read_root():
#     return ("Put in json file ") 


# class Item(BaseModel):
#     area: int
#     #property_type: str 
#     # rooms_number: int
#     #zip_code: int 
#     # land_area: Optional[int] 
#     # garden: Optional[bool] = None
#     # garden_area: Optional[int] = None
#     # equipped_kitchen: Optional[bool] = None
#     # full_address: Optional[str] = None
#     # swimming_pool: Optional[bool] = None
#     # furnished: Optional[bool] = None
#     # open_fire: Optional[bool] = None
#     # terrace: Optional[bool] = None
#     # terrace_area: Optional[int] = None
#     # facades_number: Optional[int] = None
#     # building_state: Optional[str] = None




# @app.post("/predict")
# def create_item(item: Item):
#     results = {"res":item.area} 
#     return results 

# @app.get("/testurl")
# def some_name():
#     return say_hello()

# # @app.get("/test")
# # async def root():
# #     return {"Item": Item}

# @app.get("/t1")
# def some_func(Name_of_var:Item):
#     return preprocess(Name_of_var)