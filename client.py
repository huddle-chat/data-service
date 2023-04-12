import grpc
from proto import guilds_pb2, guilds_pb2_grpc

def test():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = guilds_pb2_grpc.GuildServiceStub(channel)
        request = guilds_pb2.GuildsByUserIdRequest(user_id=7051975974723846144)

        response = stub.GetGuildsByUserId(request)
        print(response)

if __name__ == "__main__":
    test()
