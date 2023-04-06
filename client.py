import grpc
from proto import users_pb2, users_pb2_grpc


# This client.py file only exists for testing purposes
def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = users_pb2_grpc.UserServiceStub(channel)
        request = users_pb2.LoginRequest(email="matt123@gmail.com")
        response = stub.GetUserForLogin(request)

        # req = users_pb2.RegisterRequest(
        #     username="matt-yard",
        #     email="matt123@gmail.com",
        #     password="helloWorld"
        # )

        # response = stub.RegisterUser(req)

        print(response)
        if response:
            print(response)


if __name__ == "__main__":
    run()
