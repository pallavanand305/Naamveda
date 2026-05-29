"""
Naamveda - FastAPI Main Application
AI-Powered Indian Baby Naming Platform
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from loguru import logger
import time

from app.core.config import settings
from app.api.v1 import api_router

# Initialize FastAPI app
app = FastAPI(
    title="Naamveda API",
    description="AI-Powered Indian Baby Naming Platform",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log all requests with timing"""
    start_time = time.time()
    
    logger.info(f"Request: {request.method} {request.url.path}")
    
    response = await call_next(request)
    
    process_time = time.time() - start_time
    logger.info(f"Completed in {process_time:.2f}s - Status: {response.status_code}")
    
    response.headers["X-Process-Time"] = str(process_time)
    return response

# Exception handlers
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Global exception handler"""
    logger.error(f"Global exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": "Internal server error",
            "detail": str(exc) if settings.ENVIRONMENT == "development" else None
        }
    )

# Health check
@app.get("/")
async def root():
    """API health check"""
    return {
        "status": "active",
        "message": "Naamveda API is running",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    """Detailed health check"""
    return {
        "status": "healthy",
        "environment": settings.ENVIRONMENT,
        "database": "connected",  # TODO: Add actual DB check
        "ai": "ready"
    }

# Include API router
app.include_router(api_router, prefix="/api/v1")

# Startup event
@app.on_event("startup")
async def startup_event():
    """Run on application startup"""
    logger.info("🕉️ Naamveda API starting up...")
    logger.info(f"Environment: {settings.ENVIRONMENT}")
    logger.info(f"Allowed origins: {settings.ALLOWED_ORIGINS}")

# Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    """Run on application shutdown"""
    logger.info("Naamveda API shutting down...")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
