"""
Authentication API Endpoints
Google OAuth + OTP login
"""

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr
from app.core.security import create_access_token
from datetime import timedelta

router = APIRouter()

class GoogleLoginRequest(BaseModel):
    """Google OAuth login request"""
    google_token: str

class OTPSendRequest(BaseModel):
    """OTP send request"""
    phone_or_email: str

class OTPVerifyRequest(BaseModel):
    """OTP verify request"""
    phone_or_email: str
    otp: str

class TokenResponse(BaseModel):
    """Token response"""
    access_token: str
    token_type: str = "bearer"
    user: dict

@router.post("/google", response_model=TokenResponse)
async def google_login(request: GoogleLoginRequest):
    """
    Google OAuth login
    Verify Google token and create user session
    """
    try:
        # TODO: Verify Google token
        # from google.oauth2 import id_token
        # from google.auth.transport import requests
        
        # For MVP, mock response
        user_data = {
            "user_id": "mock-user-123",
            "email": "user@example.com",
            "name": "Test User"
        }
        
        # Create JWT token
        access_token = create_access_token(
            data={"sub": user_data["user_id"], "email": user_data["email"]}
        )
        
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user": user_data
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Google authentication failed: {str(e)}"
        )

@router.post("/otp/send")
async def send_otp(request: OTPSendRequest):
    """
    Send OTP to phone or email
    """
    try:
        # TODO: Implement OTP sending via Twilio/SendGrid
        
        return {
            "success": True,
            "message": f"OTP sent to {request.phone_or_email}",
            "expires_in": 300  # 5 minutes
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to send OTP: {str(e)}"
        )

@router.post("/otp/verify", response_model=TokenResponse)
async def verify_otp(request: OTPVerifyRequest):
    """
    Verify OTP and create user session
    """
    try:
        # TODO: Verify OTP from cache/database
        
        # For MVP, accept any 6-digit OTP
        if len(request.otp) != 6:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid OTP format"
            )
        
        # Mock user data
        user_data = {
            "user_id": "mock-user-456",
            "phone_or_email": request.phone_or_email,
            "name": "OTP User"
        }
        
        # Create JWT token
        access_token = create_access_token(
            data={"sub": user_data["user_id"]}
        )
        
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user": user_data
        }
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"OTP verification failed: {str(e)}"
        )

@router.get("/me")
async def get_current_user_info():
    """Get current user information"""
    # TODO: Implement with actual user from token
    return {
        "user_id": "mock-user-123",
        "email": "user@example.com",
        "name": "Test User"
    }
