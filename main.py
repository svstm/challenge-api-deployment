from typing import Union
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request, status

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    item_id = item_id * 2
    return {"item_id": item_id, "q": q}

from pydantic import BaseModel

class Item(BaseModel):
    salary: int
    bonus: int
    taxes: int

@app.post("/items2/")
def create_item(item: Item):
    
    r = item.salary + item.bonus - item.taxes
    results = {"result": r}  
    #r = item.salary + item.bonus - item.taxes

@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})

@app.post("/tax")
def tax_test(to_compute: dict):
    necessary_values = ["salary", "bonus", "taxes"]
    missing_values = [value for value in necessary_values if value not in to_compute]

    if missing_values:

        raise HTTPException(status_code=422, detail=f"3 fields expected (salary, bonus, taxes). You forgot: {', '.join(missing_values)}.")

    salary = to_compute["salary"]
    bonus = to_compute["bonus"]
    taxes = to_compute["taxes"]

    try:
        salary = int(salary)
        bonus = int(bonus)
        taxes = int(taxes)
    except ValueError:
        raise HTTPException(status_code=422, detail="expected numbers, got strings.")

  
    r = salary + bonus - taxes
    return {"result": r}

