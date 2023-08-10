import urllib3
from fastapi import FastAPI
urllib3.disable_warnings()
from Alchemy import session, Casedata
import datetime
from datetime import timedelta
app = FastAPI()

@app.get("/")
def root():
    return 'Aim : To return data upon specific Dates .........'

@app.get("/data_ent")
def Datedata(date_ent):
    date_ent = datetime
    d2 = date_ent + timedelta(days=1)

    results = session.query(Casedata).filter(date_ent < Casedata.Date_and_Time < d2).all()
    for r in results:
        print(r)

    session.close()
