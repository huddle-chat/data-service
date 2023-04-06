from db.models.guild import Guild
from db.models.guild_member import GuildMember
from db.models.user import User
from db.schemas.guild_schemas import GuildSchema
from db import Session

schema = GuildSchema()


def create_guild(owner_id: int, guild_name: str, description=None):
    session = Session()

    owner = session.query(User).filter_by(user_id=owner_id).first()
    new_entries = []
    if owner is not None:
        new_guild = Guild(name=guild_name, description=description)
        gm = GuildMember(is_owner=True)
        gm.member = owner
        new_guild.members.append(gm)

        new_entries.append(new_guild)
        new_entries.append(gm)

        session.add_all(new_entries)
        session.commit()
        session.refresh(new_guild)

        session.close()

        return schema.dump(new_guild)
    else:
        session.close()
        return False
