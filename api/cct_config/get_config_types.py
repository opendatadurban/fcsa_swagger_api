import requests
from fastapi.responses import HTMLResponse
from fastapi import APIRouter, Request
import json

from api.status_checker.api_check_status import server_cct, SRRESTPath, private_key, public_key, MYSAPSSO2

headers = {"X-Session": "", "X-Service": private_key, "X-Signature": public_key}
cookies = dict(MYSAPSSO2=MYSAPSSO2)

config_types_router = APIRouter()


@config_types_router.get('/config-types', response_class=HTMLResponse)
def get_config_types(request: Request):
    _req = requests.get(f'https://{server_cct}/{SRRESTPath}/config/types', headers=headers, cookies=cookies)
    if _req == 200:
        data_output = json.loads(_req.content)
        return {
            'data': data_output
        }
    else:
        print("bad connection error")
