
FROM python:3.11

RUN mkdir /code

WORKDIR /code

COPY . /code

RUN pip install -r requirements.txt

#COPY . .

CMD uvicorn app:app --host=0.0.0.0 --port=8000
#CMD ["uvicorn", "app:app", "--reload"]

#CMD ["uvicorn", "app:app", "--host=0.0.0.0", "--port=80"]

#CMD ["python", "app.py"]
