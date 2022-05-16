from fastapi import APIRouter, Request
import requests
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import httpx
import pandas as pd
import json
'''
ensure that variables are added and populated
'''
import os
from dotenv import load_dotenv
load_dotenv()
'''
API KEYS
'''
public_key = os.getenv('PUBLIC_KEY')
private_key = os.getenv('PRIVATE_KEY')
SERVICE_ID = os.getenv('SERVICE_ID')
MYSAPSSO2 = os.getenv('MYSAPSSO2')

check_status_router = APIRouter()

postman_details = [{"key": "server","value": "qaeservices1.capetown.gov.za","enabled": True},
                   {"key": "CURGuestRESTPath","value": "coct/api/zcur-guest/","enabled": True},
                   {"key": "SRRESTPath","value": "coct/api/zsreq","enabled": True},
                   {"key": "SSO2Ticket","value": "","enabled": True},
                   {"key": "ServiceID","value": SERVICE_ID,"enabled": True},
                   {"key": "X_Session","value": "","enabled": True},{"key": "SessionID","value": "","enabled": True}]
server_cct = postman_details[0]['value']
guest_path = postman_details[1]['value']
SRRESTPath = postman_details[2]['value']
ServiceID = postman_details[4]


headers = {"X-Session": "", "X-Service": private_key, "X-Signature": public_key}
cookies = dict(MYSAPSSO2=MYSAPSSO2)
'''
    add to jinja templating 
'''
templates = Jinja2Templates(directory="templates")


@check_status_router.get('/', response_class=HTMLResponse)
async def index(request: Request):
    _req = requests.get('https://qaeservices1.capetown.gov.za/coct/api/zcur-guest/login', headers=headers)
    if _req.status_code == 200:
        data_output = json.loads(_req.content)
        print(data_output)
    return templates.TemplateResponse("index.html", {"request": request})


@check_status_router.get('/session-id', response_class=HTMLResponse)
async def get_session_id(new_sap):

    cookies = dict(MYSAPSSO2=new_sap)
    _req = requests.get('https://qaeservices1.capetown.gov.za/coct/api/zsreq/session',headers=headers,cookies=cookies)
    if _req.status_code == 200:
        data_output = json.loads(_req.content)
        print(data_output)
    else:
        print("bad connection error")




