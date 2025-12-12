"""
API endpoint for PRD generation
Handles the /generate POST request
"""

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
import logging

from app.core.model import GenerateRequest, GenerateResponse
from app.core.prompt import generate_prd

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/generate", response_model=GenerateResponse)
async def generate_prd_endpoint(request: GenerateRequest):
    """
    Generate a Product Requirement Document from an idea
    
    Args:
        request: GenerateRequest containing the product idea
        
    Returns:
        GenerateResponse with structured PRD data
        
    Raises:
        HTTPException: If generation fails
    """
    try:
        logger.info(f"Received PRD generation request for idea: {request.idea[:100]}...")
        
        # Validate input
        if not request.idea or len(request.idea.strip()) < 10:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Idea must be at least 10 characters long"
            )
        
        # Generate PRD using the core logic
        prd_data = await generate_prd(request.idea)
        
        logger.info("PRD generation successful")
        return prd_data
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error generating PRD: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to generate PRD: {str(e)}"
        )