from marshmallow import Schema, fields
from db.schemas.user_schemas import UserSchema


class ChannelMemberSchema(Schema):
    member = fields.Nested(UserSchema)
    last_seen_message_id = fields.Int()


class ChannelSchema(Schema):
    channel_id = fields.Int()
    name = fields.Str()
    type = fields.Int()
    date_created = fields.DateTime()
    position = fields.Int()
    everyone_can_view = fields.Bool()
    everyone_can_chat = fields.Bool()
    guild_id = fields.Int()
    last_message_id = fields.Int()
