from sqlalchemy import Column, Integer, String, Boolean
from .database import Base

class RegUser(Base):
    __tablename__ = "reg__users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    temp_code = Column(String, nullable=False)
    is_temp = Column(Boolean, default=True, nullable=False)
    password = Column(String, nullable=True)
