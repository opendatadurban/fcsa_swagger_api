from fastapi import APIRouter

from api.status_checker.api_check_status import check_status_router

ApiRouter = APIRouter()
'''
    include all routes
'''
ApiRouter.include_router(check_status_router,prefix='/status_checker')
