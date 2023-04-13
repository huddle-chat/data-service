from proto import guilds_pb2, guilds_pb2_grpc
from db.queries.guild import fetch_guilds_by_user_id, create_guild
from db import Session


class GuildServicer(guilds_pb2_grpc.GuildServiceServicer):
    def GetGuildsByUserId(self, request, context):
        try:
            session = Session()
            guilds = fetch_guilds_by_user_id(request.user_id, session)
            return guilds_pb2.GuildsByUserIdResponse(guilds=guilds)
        except Exception as e:
            print(e)
            session.rollback()
            session.close()
            return guilds_pb2.GuildsByUserIdResponse()

    def CreateGuild(self, request, context):
        try:
            session = Session()
            new_guild = create_guild(
                request.user_id,
                request.name, session,
                description=request.description,
                icon=request.icon
            )

            new_guild['is_owner'] = True
            new_guild['has_unread'] = False

            return guilds_pb2.CreateGuildResponse(guild=new_guild)

        except Exception as e:
            print(e)
            return guilds_pb2.CreateGuildResponse()

        return {}
