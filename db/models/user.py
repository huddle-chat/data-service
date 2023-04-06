from db import Base
from sqlalchemy import Column, BigInteger, String, DateTime,\
  Integer, func, Boolean
from sqlalchemy.orm import relationship
from db.util import sf
import random


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
    verification_code = Column(
        Integer,
        default=lambda: random.randint(100000, 999999)
    )
    is_verified = Column(
        Boolean,
        default=False
    )
    guilds = relationship(
            "GuildMember",
            back_populates="member",
            cascade="all, delete",
            passive_deletes=True
        )
    channels = relationship(
            "ChannelMember",
            back_populates="member",
            cascade="all, delete",
            passive_deletes=True
        )

    def __repr__(self) -> str:
        return f"<User user_id={self.user_id} username={self.username}>"
