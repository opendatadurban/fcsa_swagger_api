from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn
from api.api import ApiRouter



description = """
#### CCT API code and documentation for talking to the City's Service Request API
"""

'''
import all routes to be used in app(FASTAPI)
'''
app = ApiRouter(title='cct-api', version=1.0, description=description,)

templates = Jinja2Templates(directory="templates")
'''
    import all api routes that have been created
    Each route has a test that has been created for them
'''
# @app.get('/')
# async def index(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})

from api.api import ApiRouter
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000, debug=True)
