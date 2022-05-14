#
#
#
#
# postman_details = [{"key": "server","value": "qaeservices1.capetown.gov.za","enabled": True},
#                    {"key": "CURGuestRESTPath","value": "coct/api/zcur-guest/","enabled": True},
#                    {"key": "SRRESTPath","value": "coct/api/zsreq","enabled": True},
#                    {"key": "SSO2Ticket","value": "","enabled": True},
#                    {"key": "ServiceID","value": "3A836375BA041EDAADAB8B3576D54151","enabled": True},
#                    {"key": "X_Session","value": "","enabled": True},{"key": "SessionID","value": "","enabled": True}]
# server_cct = postman_details[0]['value']
# guest_path = postman_details[1]['value']
# SRRESTPath = postman_details[2]['value']
# ServiceID = postman_details[4]
# headers = {}
# headers["X-Session"] = ""
# # headers['ServiceID'] = ServiceID['value']
# # headers["Cookies"] = ""
# headers["X-Service"] = "" # public key
# headers["X-Signature"] = "" # private key
#
# # headers["content-type"] = 'application/json; charset=utf-8'
#
# cookies = dict(MYSAPSSO2="AjQxMDIBABgARwBVAEUAUwBUAF8AVwBTAFIAXwBXACACAAYAMAA1ADADABAARQBBAFEAIAAgACAAIAAgBAAYADIAMAAyADEAMAA2ADIAMwAxADMAMAAzBwAEAAAAAggAAQEJAAIARQ8AAzA1MBAACEVBUSAgICAg%2fwD7MIH4BgkqhkiG9w0BBwKggeowgecCAQExCzAJBgUrDgMCGgUAMAsGCSqGSIb3DQEHATGBxzCBxAIBATAZMA4xDDAKBgNVBAMTA0VBUAIHIAkSCARHBDAJBgUrDgMCGgUAoF0wGAYJKoZIhvcNAQkDMQsGCSqGSIb3DQEHATAcBgkqhkiG9w0BCQUxDxcNMjEwNjIzMTMwMzQwWjAjBgkqhkiG9w0BCQQxFgQU6x1Qj%2fiNYbJq2hUnXzNy9tz4SvkwCQYHKoZIzjgEAwQvMC0CFQCmNWDd3obPqnu%2fB%2f3Moo9y4ryzvwIUelZwlIJmGegVC0pYGTFpN6bBJCU%3d")
# #%%
# def getSAPCOOKIE():
#     r = requests.get('https://qaeservices1.capetown.gov.za/coct/api/zcur-guest/login',headers=headers)
#     print(r)
#     print(r.headers)
#     data_output = json.loads(r.content)
#     print(data_output)
#     return r
#
# def getSessionID(new_SAP):
#     cookies = dict(MYSAPSSO2=new_SAP)
#     r = requests.get('https://qaeservices1.capetown.gov.za/coct/api/zsreq/session',headers=headers,cookies=cookies)
#     print(r)
#     print(r.headers)
#     data_output = json.loads(r.content)
#     print(data_output)
#     return r
#
