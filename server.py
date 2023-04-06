from db.models.role import Role
from db.models.message import Message
from db.models.guild import Guild
from db.models.channel import Channel
from db.models.guild_member import GuildMember
from db.models.guild_member_role import GuildMemberRole
from db.models.channel_member import ChannelMember
from db.models.channel_allowed_role import ChannelAllowedRole
from db.models.user import User

# The above models have to be imported before any of them
# can be used in the application

from concurrent import futures
import grpc
from dotenv import load_dotenv
import os
from proto import users_pb2_grpc
from service.users_service import UsersServicer

load_dotenv()

PORT = os.getenv("PORT")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_pb2_grpc.add_UserServiceServicer_to_server(UsersServicer(), server)

    server.add_insecure_port(f"[::]:{PORT}")
    print(f"Server now listening on port: {PORT}!!")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
