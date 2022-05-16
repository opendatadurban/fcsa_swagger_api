from fastapi import APIRouter

from api.cct_config.get_config_types import config_types_router
from api.status_checker.api_check_status import check_status_router

ApiRouter = APIRouter()
'''
    include all routes
'''
ApiRouter.include_router(check_status_router,prefix='/status')
ApiRouter.include_router(config_types_router,prefix='/config-types')
