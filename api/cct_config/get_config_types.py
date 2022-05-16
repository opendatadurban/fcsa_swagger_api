import requests
from fastapi.responses import HTMLResponse

from fastapi import APIRouter, Request
import pandas as pd
import json
import hashlib
import hmac
import base64

from api.status_checker.api_check_status import server_cct, SRRESTPath, private_key, public_key, MYSAPSSO2

headers = {"X-Session": "", "X-Service": private_key, "X-Signature": public_key}
cookies = dict(MYSAPSSO2=MYSAPSSO2)

config_types_router = APIRouter()

@config_types_router.get('/', response_class=HTMLResponse)
def get_config_types():
    r = requests.get('https://%s/%s%s'% (server_cct,SRRESTPath,'/config/types'), headers=headers,cookies=cookies)
    print(r)
    print(r.headers)
    data_output = json.loads(r.content)
    print(data_output)