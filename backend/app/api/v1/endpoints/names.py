"""
Name Generation API Endpoints
"""

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime, date
from app.services.ai_generator import AINameGenerator
from app.core.security import get_current_user

router = APIRouter()

class NameGenerationRequest(BaseModel):
    """Request model for name generation"""
    gender: str = Field(..., description="Male/Female/Unisex")
    date_of_birth: date = Field(..., description="Baby's date of birth")
    time_of_birth: Optional[str] = Field(None, description="Time of birth (HH:MM)")
    nakshatra: Optional[str] = Field(None, description="Birth nakshatra")
    starting_letter: Optional[str] = Field(None, description="Preferred starting letter")
    religion: str = Field(default="Hindu", description="Hindu/Sikh/Jain/Buddhist")
    style_preference: str = Field(default="Modern", description="Modern/Traditional/Unique")
    emotional_intention: str = Field(
        default="Success",
        description="Success/Peace/Devotion/Prosperity/Wisdom/Strength"
    )

class NameResponse(BaseModel):
    """Response model for generated name"""
    name: str
    meaning: str
    sanskrit_origin: str
    cultural_significance: str
    destiny_number: int
    soul_number: int
    personality_number: int
    life_path_number: int
    compatibility_score: int
    lucky_traits: dict
    spiritual_blessing: str
    why_this_name: str
    is_auspicious: bool

@router.post("/generate-preview", response_model=List[NameResponse])
async def generate_preview(request: NameGenerationRequest):
    """
    Generate free preview (3 names)
    No authentication required
    """
    try:
        generator = AINameGenerator()
        
        dob = datetime.combine(request.date_of_birth, datetime.min.time())
        
        names = generator.generate_preview(
            gender=request.gender,
            dob=dob,
            starting_letter=request.starting_letter,
            religion=request.religion,
            style=request.style_preference,
            emotional_intention=request.emotional_intention
        )
        
        return names
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to generate names: {str(e)}"
        )

@router.post("/generate-premium", response_model=List[NameResponse])
async def generate_premium(
    request: NameGenerationRequest,
    current_user: dict = Depends(get_current_user)
):
    """
    Generate premium report (10 names)
    Requires authentication and payment
    """
    try:
        # TODO: Verify payment before generating
        
        generator = AINameGenerator()
        
        dob = datetime.combine(request.date_of_birth, datetime.min.time())
        
        names = generator.generate_premium(
            gender=request.gender,
            dob=dob,
            time_of_birth=request.time_of_birth,
            nakshatra=request.nakshatra,
            starting_letter=request.starting_letter,
            religion=request.religion,
            style=request.style_preference,
            emotional_intention=request.emotional_intention
        )
        
        # TODO: Save to database
        
        return names
    
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to generate premium names: {str(e)}"
        )

@router.get("/history")
async def get_history(current_user: dict = Depends(get_current_user)):
    """Get user's name generation history"""
    # TODO: Implement database query
    return {
        "message": "History endpoint - coming soon",
        "user_id": current_user['user_id']
    }

@router.post("/save")
async def save_name(
    name: str,
    current_user: dict = Depends(get_current_user)
):
    """Save a favorite name"""
    # TODO: Implement database save
    return {
        "message": "Name saved successfully",
        "name": name
    }
