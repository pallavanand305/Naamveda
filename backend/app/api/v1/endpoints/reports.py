"""
Report Generation API Endpoints
PDF report generation and download
"""

from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import FileResponse
from app.core.security import get_current_user
from app.services.pdf_generator import PDFReportGenerator

router = APIRouter()

@router.get("/{generation_id}")
async def get_report(
    generation_id: str,
    current_user: dict = Depends(get_current_user)
):
    """Get report data"""
    # TODO: Fetch from database
    return {
        "generation_id": generation_id,
        "user_id": current_user['user_id'],
        "message": "Report data endpoint"
    }

@router.get("/{generation_id}/pdf")
async def download_pdf(
    generation_id: str,
    current_user: dict = Depends(get_current_user)
):
    """Download PDF report"""
    try:
        # TODO: Verify user has access (payment completed)
        # TODO: Fetch generation data from database
        
        # Mock data for MVP
        report_data = {
            "generation_id": generation_id,
            "baby_name": "Sample Name",
            "names": [],
            "user_name": current_user.get('name', 'Parent')
        }
        
        # Generate PDF
        generator = PDFReportGenerator()
        pdf_path = generator.generate_report(report_data)
        
        return FileResponse(
            pdf_path,
            media_type='application/pdf',
            filename=f'naamveda_report_{generation_id}.pdf'
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate PDF: {str(e)}"
        )
