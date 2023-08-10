from grpc_service import serveGRPC
import threading
import logging
from rest_service import serveHTTP


if __name__ == "__main__":
    logging.basicConfig()
    # start grpc server in seperate thread
    # serveGRPC()
    threading.Thread(target=serveGRPC, name="grpc-server").start()
    threading.Thread(target=serveHTTP, name="rest-server").start()
