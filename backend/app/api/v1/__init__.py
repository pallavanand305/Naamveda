"""
API v1 Router
Combines all API endpoints
"""

from fastapi import APIRouter
from app.api.v1.endpoints import auth, names, payments, reports

api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(names.router, prefix="/names", tags=["Name Generation"])
api_router.include_router(payments.router, prefix="/payments", tags=["Payments"])
api_router.include_router(reports.router, prefix="/reports", tags=["Reports"])
