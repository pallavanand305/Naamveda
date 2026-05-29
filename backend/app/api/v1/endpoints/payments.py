"""
Payment API Endpoints - Razorpay Integration
"""

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
import razorpay
from app.core.config import settings
from app.core.security import get_current_user

router = APIRouter()

# Initialize Razorpay client
razorpay_client = razorpay.Client(
    auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
)

class CreateOrderRequest(BaseModel):
    """Create Razorpay order request"""
    amount: int = settings.PREMIUM_REPORT_PRICE  # in paise
    currency: str = "INR"

class VerifyPaymentRequest(BaseModel):
    """Verify payment request"""
    razorpay_order_id: str
    razorpay_payment_id: str
    razorpay_signature: str
    generation_id: str

@router.post("/create-order")
async def create_order(
    request: CreateOrderRequest,
    current_user: dict = Depends(get_current_user)
):
    """
    Create Razorpay order for premium report
    """
    try:
        # Create Razorpay order
        order_data = {
            "amount": request.amount,
            "currency": request.currency,
            "payment_capture": 1,
            "notes": {
                "user_id": current_user['user_id'],
                "product": "premium_name_report"
            }
        }
        
        order = razorpay_client.order.create(data=order_data)
        
        # TODO: Save order to database
        
        return {
            "success": True,
            "order_id": order['id'],
            "amount": order['amount'],
            "currency": order['currency'],
            "key_id": settings.RAZORPAY_KEY_ID
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to create order: {str(e)}"
        )

@router.post("/verify")
async def verify_payment(
    request: VerifyPaymentRequest,
    current_user: dict = Depends(get_current_user)
):
    """
    Verify Razorpay payment signature
    """
    try:
        # Verify signature
        params_dict = {
            'razorpay_order_id': request.razorpay_order_id,
            'razorpay_payment_id': request.razorpay_payment_id,
            'razorpay_signature': request.razorpay_signature
        }
        
        razorpay_client.utility.verify_payment_signature(params_dict)
        
        # TODO: Update payment status in database
        # TODO: Grant access to premium report
        
        return {
            "success": True,
            "message": "Payment verified successfully",
            "generation_id": request.generation_id,
            "payment_id": request.razorpay_payment_id
        }
    
    except razorpay.errors.SignatureVerificationError:
        raise HTTPException(
            status_code=400,
            detail="Invalid payment signature"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Payment verification failed: {str(e)}"
        )

@router.get("/history")
async def get_payment_history(current_user: dict = Depends(get_current_user)):
    """Get user's payment history"""
    # TODO: Implement database query
    return {
        "message": "Payment history endpoint",
        "user_id": current_user['user_id'],
        "payments": []
    }
