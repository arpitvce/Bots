from fastapi import FastAPI
from bot import autoreply 
from pydantic import BaseModel
from collections import deque

app=FastAPI()
#queue=deque()
class Data(BaseModel):
    contact:str
    number:int
    message:str
@app.post("/automate")
def automate(contact_data:Data)->None:
    autoreply(contact_name=contact_data.contact,number=contact_data.number,msg=contact_data.message)
    return {"JOB_status":"Completed"}

