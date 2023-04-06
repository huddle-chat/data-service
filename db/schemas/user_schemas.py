from marshmallow import fields, Schema


class UserSchema(Schema):
    user_id = fields.Int()
    username = fields.Str()
    email = fields.Str()
    avatar = fields.Str()
    online_status = fields.Int()
    created_at = fields.DateTime()
    password = fields.Str()
    is_verified = fields.Bool()


class UserNoEmail(Schema):
    user_id = fields.Int()
    username = fields.Str()
    avatar = fields.Str()
    online_status = fields.Int()
    created_at = fields.DateTime()
