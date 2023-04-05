from db import Session, engine, Base
from db.models.user import User

session = Session()


def seed_users():
    users = [
        User(
          username="Alice",
          email="alice@example.com",
          password="pass1234"
        ),
        User(
          username="Bob",
          email="bob@example.com",
          password="pass1234"
        ),
        User(
          username="Charlie",
          email="charlie@example.com",
          password="pass1234"
        )
    ]

    session.add_all(users)

    session.commit()


if __name__ == "__main__":
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    seed_users()
    session.close()
