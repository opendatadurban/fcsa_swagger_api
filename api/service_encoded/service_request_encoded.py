from fastapi import APIRouter

from api.status_checker.api_check_status import server_cct, SRRESTPath, private_key, public_key, MYSAPSSO2
import requests


headers = {"X-Session": "", "X-Service": private_key, "X-Signature": public_key}
cookies = dict(MYSAPSSO2=MYSAPSSO2)

service_request_encoded = APIRouter()


def service_request_encoded(new_SAP):
    cookies = dict(MYSAPSSO2=new_SAP)
    dataset_dict = {"username":"","firstName":"John","lastName":"Doe","account_number":"","type":"1001","subtype":"1009","address":"0A, Beach Road, Muizenberg","street_number":"0A","street":"BeachRoad","suburb":"Muizenberg","telephone":"0835559876","email":"j.doe@gmail.com","message":"Pleasecollect the whale carcass from Muizenberg beach before the wind direction changes.","latitude":"-34.108038128850701298","longitude":"18.471525907516479492","comm":"EMAIL"}
    r = requests.post(f'https://{server_cct}/{SRRESTPath}/sr', data=dataset_dict, headers=headers, cookies=cookies)

    print(r.text)
    '''
    print(r.headers)
    data_output = json.loads(r.content)
    print(data_output)
    '''
    return r
