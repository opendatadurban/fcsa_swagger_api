from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn
from api.status_checker.api_check_status import check_status_router

description = """
#### CCT API code and documentation for talking to the City's Service Request API
"""

app = FastAPI(title='cct-api', version=1.0, description=description,)
'''
import all routes to be used in app(FASTAPI)
'''
app.include_router(check_status_router)

templates = Jinja2Templates(directory="templates")
'''
    import all api routes that have been created
    Each route has a test that has been created for them
'''
@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000, debug=True)
