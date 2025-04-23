# app/models/city.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.config.database import Base

class City(Base):
    __tablename__ = 'city'

    city_id = Column(Integer, primary_key=True, index=True)
    city = Column(String(50), nullable=False)
    country_id = Column(Integer, nullable=False)
    last_update = Column(DateTime)

