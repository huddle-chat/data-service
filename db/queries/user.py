from db.models.user import User
import bcrypt
from db.schemas.user_schemas import UserSchema
from google.protobuf.timestamp_pb2 import Timestamp


def create_user(username: str, email: str, password: str, session) -> int:
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    new_user = User(
        username=username,
        email=email,
        password=hashed_pw.decode()
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    code = new_user.verification_code
    session.close()

    return code


def fetch_user_for_login(email: str, session):

    user = session.query(User).filter_by(email=email).first()
    session.close()

    if user:
        schema = UserSchema()

        user_dict = schema.dump(user)

        ts = Timestamp()
        ts.FromDatetime(user.created_at)

        user_dict["created_at"] = ts

        return user_dict
    else:
        return None


def fetch_user_verification(email: str, session):
    user = session.query(User.email, User.verification_code, User.is_verified)\
        .filter_by(email=email).first()

    if user:
        return user

    else:
        return None


def verify_user(email: str, session):
    user = session.query(User).filter_by(email=email).first()

    if user:
        user.is_verified = True
        session.add(user)
        session.commit()
        session.refresh(user)
        session.close()
        return user
    else:
        return None


def fetch_current_user_by_id(user_id: int, session):
    user = session.query(User).filter_by(user_id=user_id).first()
    session.close()

    if user:
        schema = UserSchema()

        user_dict = schema.dump(user)

        ts = Timestamp()
        ts.FromDatetime(user.created_at)

        user_dict["created_at"] = ts

        return user_dict

    else:
        return None
