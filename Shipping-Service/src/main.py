from concurrent import futures
import logging

import grpc
import shipping_pb2_grpc
from grpc_service import ShippingGRPCService
import threading
import uvicorn
from rest_service import app


def serveGRPC():
    print("Starting GRPC Server")
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    shipping_pb2_grpc.add_ShippingServicer_to_server(ShippingGRPCService(),
                                                     server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("GRPC Server started, listening on ", port)
    server.wait_for_termination()


def serveHTTP():
    print("Starting HTTP Server")
    port = 8000
    host = "0.0.0.0"
    print("HTTP Server started, listening on ", port)
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    logging.basicConfig()
    # start grpc server in seperate thread
    # serveGRPC()
    threading.Thread(target=serveGRPC, name="grpc-server").start()
    threading.Thread(target=serveHTTP, name="rest-server").start()
