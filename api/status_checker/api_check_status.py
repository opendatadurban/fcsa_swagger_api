from fastapi import APIRouter, Request
import requests
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import httpx
import pandas as pd
import json

check_status_router = APIRouter()

postman_details = [{"key": "server","value": "qaeservices1.capetown.gov.za","enabled": True},
                   {"key": "CURGuestRESTPath","value": "coct/api/zcur-guest/","enabled": True},
                   {"key": "SRRESTPath","value": "coct/api/zsreq","enabled": True},
                   {"key": "SSO2Ticket","value": "","enabled": True},
                   {"key": "ServiceID","value": "3A836375BA041EDAADAB8B3576D54151","enabled": True},
                   {"key": "X_Session","value": "","enabled": True},{"key": "SessionID","value": "","enabled": True}]
server_cct = postman_details[0]['value']
guest_path = postman_details[1]['value']
SRRESTPath = postman_details[2]['value']
ServiceID = postman_details[4]


headers = {"X-Session": "", "X-Service": "3A8369E159041EEAADDEA975879D9E5E", "X-Signature": "3A8369E159041EEAADDEA975879D9E5E"}
cookies = dict(MYSAPSSO2="AjQxMDIBABgARwBVAEUAUwBUAF8AVwBTAFIAXwBXACACAAYAMAA1ADADABAARQBBAFEAIAAgACAAIAAgBAAYADIAMAAyADEAMAA2ADIAMwAxADMAMAAzBwAEAAAAAggAAQEJAAIARQ8AAzA1MBAACEVBUSAgICAg%2fwD7MIH4BgkqhkiG9w0BBwKggeowgecCAQExCzAJBgUrDgMCGgUAMAsGCSqGSIb3DQEHATGBxzCBxAIBATAZMA4xDDAKBgNVBAMTA0VBUAIHIAkSCARHBDAJBgUrDgMCGgUAoF0wGAYJKoZIhvcNAQkDMQsGCSqGSIb3DQEHATAcBgkqhkiG9w0BCQUxDxcNMjEwNjIzMTMwMzQwWjAjBgkqhkiG9w0BCQQxFgQU6x1Qj%2fiNYbJq2hUnXzNy9tz4SvkwCQYHKoZIzjgEAwQvMC0CFQCmNWDd3obPqnu%2fB%2f3Moo9y4ryzvwIUelZwlIJmGegVC0pYGTFpN6bBJCU%3d")
'''
    add to jinja templating 
'''
templates = Jinja2Templates(directory="templates")


@check_status_router.get('/', response_class=HTMLResponse)
async def index(request: Request):
    _req = requests.get('https://qaeservices1.capetown.gov.za/coct/api/zcur-guest/login', headers=headers)
    if _req == 200:
        print("okay")
    return templates.TemplateResponse("index.html", {"request": request})

#
# @check_status_router.get('/', tags=["check_status"])
# async def get_sap_cookie( request: Request):
#     r = requests.get('https://qaeservices1.capetown.gov.za/coct/api/zcur-guest/login',headers=headers)
#     print(r.status_code)
#     # print(r.headers)
#     # data_output = json.loads(r.content)
#     # print(data_output)
#     return r
# #
# # def getSessionID(new_SAP):
# #     cookies = dict(MYSAPSSO2=new_SAP)
# #     r = requests.get('https://qaeservices1.capetown.gov.za/coct/api/zsreq/session',headers=headers,cookies=cookies)
# #     print(r)
# #     print(r.headers)
# #     data_output = json.loads(r.content)
# #     print(data_output)
# #     return r
# #
