from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn

from api.api import ApiRouter

app = FastAPI(title='cct-api', version=1.0, description="Well done",)
app.include_router(ApiRouter,tags=['Api'])

'''
    creating 
'''
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000, debug=True)


