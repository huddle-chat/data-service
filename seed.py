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
from db.queries.guild import create_guild

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


def seed_guilds():

    new_entries = []

    me = User(
        username="matt",
        email="matt@example.com",
        password="pass1234"
    )

    new_entries.append(me)

    new_guild = Guild(name="matt's server")

    gm = GuildMember()
    gm.member = me
    gm.guild = new_guild

    new_entries.append(new_guild)
    new_entries.append(gm)

    chan = Channel(type=0, position=0, name='general')

    new_guild.channels.append(chan)

    cm = ChannelMember()
    cm.member = me
    cm.channel = chan

    new_entries.append(cm)

    session.add_all(new_entries)
    session.commit()
    session.close()


if __name__ == "__main__":
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    seed_users()
    seed_guilds()
    session.close()
