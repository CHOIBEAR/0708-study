from fastapi import Form, APIRouter
from typing import Annotated

ctr = APIRouter()

@ctr.get("/")
def root():
    return {"test": 1}

@ctr.get("/test")
def test(a : int):
    return {"data": 12345 + a}

@ctr.post("/body")
def body(a : Annotated[int, Form(...)]):
    return {"body": "OK", "data": a}

@ctr.get("/home")
def home():
    return{"집에가고싶다":"ㄹㅇㄹㅇ"}

@ctr.post("/homeplz")
def home(a:Annotated[int, Form(...)]):
    return {"진짜 거짓말 하나도 안하고 집에 가고 싶다.": a}