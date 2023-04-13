import grpc
from proto import guilds_pb2, guilds_pb2_grpc

def test():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = guilds_pb2_grpc.GuildServiceStub(channel)

        request = guilds_pb2.CreateGuildRequest(
            user_id=7052023103353847808,
            name="Awesome New Guild"
        )

        response = stub.CreateGuild(request)

        print(response)

if __name__ == "__main__":
    test()
