from pydantic import BaseModel

class SMSRequest(BaseModel):
    product_name: str
    tone: str

class SMSResponse(BaseModel):
    message: str
