"""
Pydantic models for request/response validation
"""

from pydantic import BaseModel, Field
from typing import List

class GenerateRequest(BaseModel):
    """Request model for PRD generation"""
    idea: str = Field(
        ...,
        min_length=10,
        max_length=5000,
        description="The product idea to generate a PRD for",
        example="A mobile app that helps users track their daily water intake with gamification"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "idea": "A mobile app that helps users track their daily water intake with gamification and social features"
            }
        }

class GenerateResponse(BaseModel):
    """Response model containing the generated PRD"""
    summary: str = Field(
        ...,
        description="Executive summary of the product idea and problem statement"
    )
    features: List[str] = Field(
        ...,
        description="List of key features and user stories"
    )
    roadmap: List[str] = Field(
        ...,
        description="30/60/90-day development roadmap milestones"
    )
    architecture: str = Field(
        ...,
        description="High-level technical architecture overview"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "summary": "HydroTrack is a mobile application designed to help users maintain healthy hydration habits...",
                "features": [
                    "User Story: As a health-conscious user, I want to log my water intake so I can track my daily hydration",
                    "Feature: Daily hydration goal setting with customizable targets",
                    "Feature: Push notifications and reminders to drink water"
                ],
                "roadmap": [
                    "30 Days: MVP with basic tracking, goal setting, and notifications",
                    "60 Days: Add gamification, achievements, and social sharing features",
                    "90 Days: Integrate with fitness wearables and add analytics dashboard"
                ],
                "architecture": "Mobile: React Native for iOS/Android. Backend: Node.js with Express. Database: PostgreSQL for user data, Redis for caching..."
            }
        }