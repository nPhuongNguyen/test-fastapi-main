from pydantic import BaseModel
from datetime import datetime

class CitySchema(BaseModel):
    city: str  # Chỉ định nghĩa trường bạn muốn expose
    
    class Config:
        from_attributes = True  # Cho phép convert từ SQLAlchemy model