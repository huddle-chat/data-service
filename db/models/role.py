from db import Base
from sqlalchemy import Column, BigInteger, String, Boolean, text, ForeignKey
from sqlalchemy.orm import relationship
from db.util import sf


class Role(Base):
    __tablename__ = "role"
    role_id = Column(
        BigInteger,
        primary_key=True,
        default=lambda: int(next(sf))
    )
    guild_id = Column(
        BigInteger,
        ForeignKey("guild.guild_id", ondelete="CASCADE"),
        nullable=False
    )
    name = Column(String, nullable=False)
    color = Column(String, server_default=text("'#ffffff'"))
    can_invite = Column(Boolean, server_default=text("false"))
    can_create_channel = Column(Boolean, server_default=text("false"))
    can_delete_channel = Column(Boolean, server_default=text("false"))
    can_delete_message = Column(Boolean, server_default=text("false"))
    can_kick_member = Column(Boolean, server_default=text("false"))
    members = relationship(
          "GuildMemberRole",
          cascade="all, delete",
          passive_deletes=True,
          back_populates="role"
    )

    def __repr__(self):
        return f"<Role name={self.name} guild_id={self.guild_id} >"
