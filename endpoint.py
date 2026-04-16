from fastapi import FastAPI
from bot import autoreply 
from pydantic import BaseModel
from collections import deque
from fastapi.responses import RedirectResponse
#from fastapi import background_tasks
import time



app=FastAPI()
queue=deque()
class Data(BaseModel):
    contact:str
    number:int
    message:str
@app.post("/automate")
def automate(contact_data:Data)->dict:
    autoreply(contact_name=contact_data.contact,number=contact_data.number,msg=contact_data.message)
    return {"JOB_status":"Completed"}
@app.post("/enqueue")
def enqueue(contact_data:Data)->dict:
    queue.append(contact_data)
    return {"JOB_STATUS":"Processing..."}
@app.get("/start")
def start_messaging():
    start=time.time()
    n=len(queue)
    while len(queue)>0:
        print(f"{n} Jobs Pending")
        message_data=queue.popleft()
        autoreply(contact_name=message_data.contact,number=message_data.number,msg=message_data.message)
        n-=1
    end=time.time()
    diff=start-end
    return {"Time_Taken":diff}

