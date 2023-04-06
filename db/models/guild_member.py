from db import Base
from sqlalchemy import Column, BigInteger, text,\
  UniqueConstraint, DateTime, func, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from db.util import sf


class GuildMember(Base):
    __tablename__ = "guild_member"
    __table_args__ = (
        UniqueConstraint('guild_id', 'member_id'),
      )
    guild_member_id = Column(
          BigInteger,
          primary_key=True,
          default=lambda: int(next(sf))
        )
    member_id = Column(
          BigInteger,
          ForeignKey('user.user_id', ondelete="CASCADE"),
          nullable=False
        )
    guild_id = Column(
          BigInteger,
          ForeignKey('guild.guild_id', ondelete="CASCADE"),
          nullable=False
        )
    joined_at = Column(DateTime, server_default=func.now())
    is_owner = Column(Boolean, server_default=text("false"))
    guild = relationship("Guild", back_populates="members")
    member = relationship("User", back_populates="guilds")
    roles = relationship(
        "GuildMemberRole",
        back_populates="member",
        cascade="all, delete",
        passive_deletes=True
    )

    def __repr__(self):
        return f"""<GuildMember guild_id={self.guild_id},
        member_id={self.member_id}"""
