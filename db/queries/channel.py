from db.models.user import User
from db.models.channel import Channel
from db.models.channel_allowed_role import ChannelAllowedRole
from db.models.guild import Guild
from db.models.role import Role
from db.models.guild_member_role import GuildMemberRole
from db.models.guild_member import GuildMember
from sqlalchemy import and_
from db import Session


def add_new_channel(
    user_id: int,
    guild_id: int,
    type: int,
    name: str,
    position=1,
    everyone_can_view=True,
    everyone_can_chat=True,
    allowed_role_ids=None
):
    session = Session()
    role = session.query(Role)\
        .join(GuildMemberRole, GuildMemberRole.role_id == Role.role_id)\
        .join(
            GuildMember,
            GuildMember.guild_member_id == GuildMemberRole.guild_member_id
        )\
        .join(User, GuildMember.member_id == User.user_id)\
        .filter(and_(
            User.user_id == user_id,
            Role.can_create_channel is True,
            Role.guild_id == guild_id
        ))\
        .first()

    guild = session.query(Guild).filter_by(guild_id=guild_id).first()

    if role and guild:
        new_entries = []
        new_channel = Channel(
            name=name,
            type=type,
            position=position,
            everyone_can_chat=everyone_can_chat,
            everyone_can_view=everyone_can_view
        )
        guild.channels.append(new_channel)
        new_entries.append(new_channel)
        if allowed_role_ids is not None:
            # Loop through allowed roles and add role to channel
            for role_id in allowed_role_ids:
                car = ChannelAllowedRole(role_id=role_id)
                new_channel.allowed_roles.append(car)
                new_entries.append(car)

        session.add_all(new_entries)
        session.commit()
        session.refresh(new_channel)
    else:
        session.close()
        return False
    session.close()
    return new_channel


def add_members_to_channel(channel_id: int):
    session = Session()
    # Take a channel ID
    # Query the DB to get the guild that the channel belongs to
    # select all users who have a role that is in the allowed_roles
    allowed_roles = session.query(ChannelAllowedRole.role_id)\
        .filter_by(channel_id=channel_id)\
        .all()
    for role_id in allowed_roles:
        print(role_id[0])
    # print(allowed_roles)
    session.close()
