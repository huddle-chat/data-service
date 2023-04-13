from db.models.guild import Guild
from db.models.guild_member import GuildMember
from db.models.user import User
from db.models.channel import Channel
from db.models.channel_member import ChannelMember
from db.schemas.guild_schemas import GuildSchema, GuildList
from db import Session
from google.protobuf.timestamp_pb2 import Timestamp
from sqlalchemy import and_, func, case




def create_guild(owner_id: int, guild_name: str, session: Session, description=None, icon="None"):

    owner = session.query(User).filter_by(user_id=owner_id).first()
    new_entries = []
    if owner is not None:

        schema = GuildSchema()
        # If owner exists, create thew new guild
        new_guild = Guild(name=guild_name, description=description)
        # Assign the owner as the first guild member
        gm = GuildMember(is_owner=True)
        gm.member = owner
        new_guild.members.append(gm)
        # Create a default divider for text channels
        default_divider = Channel(type=2, name="Text Channels", position=0)

        # TODO:
        # Update the channel model to include a parentId
        # Create default channel with the default divider as a parent

        default_channel = Channel(type=0, name="general", position=1)

        cm = ChannelMember()
        cm.channel = default_divider
        cm.member = owner

        new_entries.append(cm)

        cm = ChannelMember()

        cm.channel = default_channel
        cm.member = owner

        new_entries.append(cm)

        new_guild.channels.append(default_divider)
        new_guild.channels.append(default_channel)

        new_entries.append(default_divider)
        new_entries.append(default_channel)

        new_entries.append(new_guild)
        new_entries.append(gm)

        session.add_all(new_entries)
        session.commit()
        session.refresh(new_guild)

        session.close()

        new_guild_dict = schema.dump(new_guild)

        ts = Timestamp()
        ts.FromDatetime(new_guild.created_at)

        new_guild_dict['created_at'] = ts

        return new_guild_dict
        # return new_guild
    else:
        session.close()
        return False


def fetch_guilds_by_user_id(user_id: int, session: Session):

    guilds = session.query(Guild, GuildMember.is_owner, case(
        (func.count(
            case(
                (Channel.last_message_id >
                 func.coalesce(ChannelMember.last_seen_message_id, 0), 1),
                else_=None
            )
        ) > 0, True),
        else_=False
    ).label('has_unread')
    )\
     .join(GuildMember, GuildMember.guild_id == Guild.guild_id)\
     .join(Channel, Channel.guild_id == Guild.guild_id)\
     .join(
        ChannelMember,
        and_(
                ChannelMember.channel_id == Channel.channel_id,
                ChannelMember.member_id == GuildMember.member_id
            ),
        isouter=True
    )\
     .filter(GuildMember.member_id == user_id)\
     .group_by(Guild.guild_id, GuildMember.is_owner)\
     .all()

    print(guilds)


#  # TODO:
#     # Returned object should include:
#         # DONE - whether or not the current user is the owner
#         # whether or not there are channels with unread messages
    if guilds:
        schema = GuildList()
        guilds_dict = schema.dump({
            'guilds': [guild for guild, _, _ in guilds]
        })

        for i in range(len(guilds)):
            guild, is_owner, has_unread = guilds[i]
            ts = Timestamp()
            ts.FromDatetime(guild.created_at)
            guilds_dict['guilds'][i]['created_at'] = ts
            guilds_dict['guilds'][i]['is_owner'] = is_owner
            guilds_dict['guilds'][i]['has_unread'] = has_unread

        print(guilds_dict)
        session.close()
        return guilds_dict['guilds']
    session.close()
    return None
