from db import Base
from sqlalchemy import Column, BigInteger,\
  String, DateTime, func
from sqlalchemy.orm import relationship
from db.util import sf


class Guild(Base):
    __tablename__ = "guild"
    guild_id = Column(
        BigInteger,
        primary_key=True,
        default=lambda: int(next(sf))
    )
    name = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    icon = Column(String, server_default="None")
    description = Column(String)
    members = relationship(
            "GuildMember",
            back_populates="guild",
            cascade="all, delete",
            passive_deletes=True
            )
    channels = relationship(
                "Channel",
                cascade="all, delete",
                passive_deletes=True
            )
    roles = relationship(
                "Role",
                cascade="all,delete",
                passive_deletes=True
            )

    def __repr__(self):
        return f"<Guild id={self.guild_id}, name={self.name}>"
