import requests
from fastapi import APIRouter, Request
import pandas as pd
import json
import hashlib
import hmac
import base64


def getConfigTypes():
    r = requests.get('https://%s/%s%s'% (server_cct,SRRESTPath,'/config/types'), headers=headers,cookies=cookies)
    print(r)
    print(r.headers)
    data_output = json.loads(r.content)
    print(data_output)