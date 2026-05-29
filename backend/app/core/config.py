"""
Application Configuration
Loads environment variables and provides settings
"""

from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    """Application settings"""
    
    # App
    APP_NAME: str = "Naamveda"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    
    # Database
    DATABASE_URL: str
    
    # Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # OpenAI
    OPENAI_API_KEY: str
    OPENAI_MODEL: str = "gpt-4-turbo-preview"
    
    # Razorpay
    RAZORPAY_KEY_ID: str
    RAZORPAY_KEY_SECRET: str
    
    # Google OAuth
    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str
    
    # Frontend
    FRONTEND_URL: str = "http://localhost:3000"
    
    # CORS
    ALLOWED_ORIGINS: str = "http://localhost:3000"
    
    @property
    def allowed_origins_list(self) -> List[str]:
        """Convert ALLOWED_ORIGINS string to list"""
        return [origin.strip() for origin in self.ALLOWED_ORIGINS.split(",")]
    
    # Email (Optional)
    SMTP_HOST: str = ""
    SMTP_PORT: int = 587
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
    
    # SMS (Optional)
    TWILIO_ACCOUNT_SID: str = ""
    TWILIO_AUTH_TOKEN: str = ""
    TWILIO_PHONE_NUMBER: str = ""
    
    # Logging
    LOG_LEVEL: str = "INFO"
    
    # Pricing
    PREMIUM_REPORT_PRICE: int = 29900  # ₹299 in paise
    FREE_NAMES_COUNT: int = 3
    PREMIUM_NAMES_COUNT: int = 10
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# Initialize settings
settings = Settings()
