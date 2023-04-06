from db import Base
from sqlalchemy import Column, BigInteger, ForeignKey,\
  Integer, String, Boolean, text, DateTime, func
from sqlalchemy.orm import relationship
from db.util import sf


class Channel(Base):
    __tablename__ = "channel"
    channel_id = Column(
        BigInteger,
        primary_key=True,
        default=lambda: int(next(sf))
    )
    type = Column(Integer, nullable=False)
    name = Column(String)
    date_created = Column(DateTime, server_default=func.now())
    position = Column(Integer)
    everyone_can_view = Column(Boolean, server_default=text('true'))
    everyone_can_chat = Column(Boolean, server_default=text('true'))
    guild_id = Column(
          BigInteger,
          ForeignKey("guild.guild_id", ondelete="CASCADE"),
          nullable=True
        )
    members = relationship(
          "ChannelMember",
          back_populates="channel",
          cascade="all, delete",
          passive_deletes=True
        )
    messages = relationship(
        "Message",
        cascade="all, delete",
        passive_deletes=True,
        foreign_keys="[Message.channel_id]",
        post_update=True
    )
    last_message_id = Column(
        BigInteger,
        ForeignKey(
            "message.message_id",
            ondelete="CASCADE",
            name="fk_last_message"
        ),
        nullable=True
    )
    allowed_roles = relationship(
                "ChannelAllowedRole",
                cascade="all, delete",
                passive_deletes=True
            )

    def __repr__(self):
        return f"<Channel id={self.channel_id}>"

