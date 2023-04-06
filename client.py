import grpc
from proto import users_pb2, users_pb2_grpc

#This client.py file only exists for testing purposes
def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = users_pb2_grpc.UserServiceStub(channel)
        request = users_pb2.UserLoginRequest(email="alice@example.com")
        response = stub.GetUserForLogin(request)

        print(type(response))
        if response:
            print(response)


if __name__ == "__main__":
    run()
