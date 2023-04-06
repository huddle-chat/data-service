from db import Base
from sqlalchemy import Column, BigInteger,\
  UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship


class ChannelMember(Base):
    __tablename__ = 'channel_member'
    __table_args__ = (
        UniqueConstraint('channel_id', 'member_id'),
      )
    channel_id = Column(
          BigInteger,
          ForeignKey("channel.channel_id", ondelete="CASCADE"),
          primary_key=True
        )
    member_id = Column(
          BigInteger,
          ForeignKey("user.user_id", ondelete="CASCADE"),
          primary_key=True
        )
    channel = relationship("Channel", back_populates="members")
    member = relationship("User", back_populates="channels")
    last_seen_message_id = Column(
        BigInteger,
        ForeignKey("message.message_id", ondelete="CASCADE"),
        nullable=True
    )

    def __repr__(self) -> str:
        return f"""<ChannelMember channel_id={self.channel_id},
    member_id={self.member_id} >"""
