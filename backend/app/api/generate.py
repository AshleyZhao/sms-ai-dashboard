from fastapi import APIRouter
from app.models.schema import SMSRequest, SMSResponse
from app.services.ai import generate_sms

router = APIRouter()

@router.post("/generate-sms", response_model=SMSResponse)
async def generate_sms_endpoint(payload: SMSRequest):
    message = generate_sms(payload.product_name, payload.tone)
    return SMSResponse(message=message)
