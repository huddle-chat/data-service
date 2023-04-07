from proto import users_pb2, users_pb2_grpc
from sqlalchemy.exc import IntegrityError
import grpc
from db.queries.user import fetch_user_for_login, create_user,\
    fetch_user_verification, verify_user, fetch_current_user_by_id
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
            verification_code = create_user(
                request.username,
                request.email,
                request.password,
                session
            )

            return users_pb2.RegisterResponse(
                success=True,
                message="Thanks for Signing up!",
                verification_code=verification_code
            )

        except IntegrityError:
            session.rollback()
            session.close()
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details(
                "A user with that username or email already exists."
            )
            return users_pb2.RegisterResponse()

    def GetUserVerification(self, request, context):
        try:
            session = Session()
            user = fetch_user_verification(request.email, session)
            if user:
                return users_pb2.VerificationResponse(
                    email=user.email,
                    verification_code=user.verification_code,
                    is_verified=user.is_verified
                )
            else:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("Couldnt find a user with that email.")
                return users_pb2.VerificationResponse()
        except Exception:
            return users_pb2.VerificationResponse()

    def VerifyUser(self, request, context):
        try:
            session = Session()
            user = verify_user(request.email, session)
            if user:
                return users_pb2.VerificationResponse(
                    email = user.email,
                    verification_code=user.verification_code,
                    is_verified=user.is_verified
                )
            else:
                context.set_code(grpc.StatusCode.NOT_FOUND)
                context.set_details("Couldnt find a user with that email.")
                return users_pb2.VerificationResponse()
        except Exception:
            return users_pb2.VerificationResponse()

    def GetCurrentUserById(self, request, context):
        try:
            session = Session()
            user = fetch_current_user_by_id(request.user_id, session)

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
