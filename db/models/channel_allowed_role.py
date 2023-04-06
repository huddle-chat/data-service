from db import Base
from sqlalchemy import Column, BigInteger, UniqueConstraint,\
  ForeignKey, Boolean, text
from sqlalchemy.orm import relationship


class ChannelAllowedRole(Base):
    __tablename__ = 'channel_allowed_role'
    __table_args__ = (
        UniqueConstraint('channel_id', 'role_id'),
      )
    channel_id = Column(
        BigInteger,
        ForeignKey("channel.channel_id", ondelete="CASCADE"),
        primary_key=True
    )
    role_id = Column(
        BigInteger,
        ForeignKey("role.role_id", ondelete="CASCADE"),
        primary_key=True
    )
    can_message = Column(Boolean, server_default=text("true"))
    role = relationship("Role", cascade="all, delete")

    def __repr__(self) -> str:
        return f"""
            <ChannelAllowedRole channel_id={self.channel_id},
            role_id={self.role_id}>
            """
