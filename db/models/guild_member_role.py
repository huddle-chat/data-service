from db import Base
from sqlalchemy import Column, BigInteger,\
  UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship


class GuildMemberRole(Base):
    __tablename__ = "guild_member_role"
    __table_args__ = (
        UniqueConstraint('guild_member_id', 'role_id'),
      )
    guild_member_id = Column(
        BigInteger,
        ForeignKey("guild_member.guild_member_id", ondelete="CASCADE"),
        primary_key=True
    )
    role_id = Column(
        BigInteger,
        ForeignKey("role.role_id", ondelete="CASCADE"),
        primary_key=True
    )
    member = relationship(
        "GuildMember",
        back_populates="roles",
        cascade="all, delete"
    )
    role = relationship(
        "Role",
        back_populates="members",
        cascade="all, delete"
    )

    def __repr__(self):
        return f"<GMRole gm_id={self.guild_member_id} role_id={self.role_id}>"
