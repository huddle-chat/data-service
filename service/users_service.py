from proto import users_pb2, users_pb2_grpc
from google.protobuf.timestamp_pb2 import Timestamp
from db import Session
from db.models.user import User
from db.schemas.user_schemas import UserSchema


class UsersServicer(users_pb2_grpc.UserServiceServicer):
    def GetUserForLogin(self, request, context):
        session = Session()
        db_user = session.query(User).filter_by(email=request.email).first()
        if db_user:
            schema = UserSchema()

            user_dict = schema.dump(db_user)

            test_ts = Timestamp()
            test_ts.FromDatetime(db_user.created_at)

            user_dict["created_at"] = test_ts

            user_obj = users_pb2.UserForLogin(**user_dict)

            response = users_pb2.LoginResponse(user=user_obj)

            return response
        else:
            return users_pb2.LoginResponse()
