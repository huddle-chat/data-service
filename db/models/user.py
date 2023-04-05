from db import Base
from sqlalchemy import Column, BigInteger, String, DateTime, Integer, func
from db.util import sf


class User(Base):
    __tablename__ = "user"
    user_id = Column(
        BigInteger,
        primary_key=True,
        default=lambda: int(next(sf))
    )
    username = Column(
        String,
        unique=True,
        nullable=False
    )
    email = Column(
        String,
        unique=True,
        nullable=False
    )
    password = Column(String, nullable=False)
    avatar = Column(String, server_default="None")
    created_at = Column(
        DateTime,
        nullable=False,
        server_default=func.now()
    )
    online_status = Column(
        Integer,
        default=1
    )
