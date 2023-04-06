from db import Base
from sqlalchemy import Column, BigInteger,\
  ForeignKey, DateTime, Text, func, Boolean, text
from sqlalchemy.orm import relationship
from db.util import sf


class Message(Base):
    __tablename__ = "message"
    message_id = Column(
        BigInteger,
        primary_key=True,
        default=lambda: int(next(sf))
    )
    channel_id = Column(
        BigInteger,
        ForeignKey(
                "channel.channel_id",
                ondelete="CASCADE",
                name="fk_channel"
            ),
        nullable=False
    )
    author_id = Column(
        BigInteger,
        ForeignKey("user.user_id", ondelete="CASCADE"),
        nullable=False
    )
    content = Column(
        Text,
        nullable=False
    )
    timestamp = Column(
        DateTime,
        nullable=False,
        server_default=func.now()
    )
    edited_timestamp = Column(
        DateTime,
        nullable=True,
        onupdate=func.now()
    )
    mention_everyone = Column(
        Boolean,
        server_default=text("false")
    )
    author = relationship("User")

    def __repr__(self) -> str:
        return f"""<Message message_id={self.message_id},
         author_id={self.author_id}"""
