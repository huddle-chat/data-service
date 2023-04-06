from proto import users_pb2, users_pb2_grpc
from sqlalchemy.exc import IntegrityError
import grpc
from db.queries.user import fetch_user_for_login, create_user
from db import Session


class UsersServicer(users_pb2_grpc.UserServiceServicer):
    def GetUserForLogin(self, request, context):
        try:
            session = Session()
            user = fetch_user_for_login(request.email, session)
            if user:
                user_obj = users_pb2.UserForLogin(**user)
                response = users_pb2.LoginResponse(user=user_obj)

                return response
            else:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("Couldnt find a user with that email.")
                return users_pb2.LoginResponse()
        except Exception:
            session.rollback()
            session.close()
            return users_pb2.LoginResponse()

    def RegisterUser(self, request, context):
        try:
            session = Session()
            create_user(
                request.username,
                request.email,
                request.password,
                session
            )

            return users_pb2.RegisterResponse(
                success=True,
                message="Thanks for Signing up!"
            )

        except IntegrityError:
            session.rollback()
            session.close()
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details(
                "A user with that username or email already exists."
            )
            return users_pb2.RegisterResponse()
