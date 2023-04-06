from db import Session, engine, Base
from db.models.role import Role
from db.models.message import Message
from db.models.guild import Guild
from db.models.channel import Channel
from db.models.guild_member import GuildMember
from db.models.guild_member_role import GuildMemberRole
from db.models.channel_member import ChannelMember
from db.models.channel_allowed_role import ChannelAllowedRole
from db.models.user import User

session = Session()


def seed_users():
    users = [
        User(
          username="Alice",
          email="alice@example.com",
          password="pass1234"
        ),
        User(
          username="Bob",
          email="bob@example.com",
          password="pass1234"
        ),
        User(
          username="Charlie",
          email="charlie@example.com",
          password="pass1234"
        )
    ]

    session.add_all(users)

    session.commit()


if __name__ == "__main__":
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    seed_users()
    session.close()
