from marshmallow import Schema, fields
from db.schemas.user_schemas import UserSchema


class GuildMemberSchema(Schema):
    member = fields.Nested(UserSchema)
    joined_at = fields.DateTime()


class GuildSchema(Schema):
    guild_id = fields.Int()
    name = fields.Str()
    created_at = fields.DateTime()
    icon = fields.Str()
    description = fields.String()


class GuildList(Schema):
    guilds = fields.List(fields.Nested(GuildSchema))
