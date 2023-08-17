import grpc
import shipping_pb2
import shipping_pb2_grpc


class ShippingRESTClient:
    def __init__(self, port_number):
        pass

    def calculate_shipping_cost(self):
        pass

    def calculate_shipping_cost_no_courier(self):
        pass

    def create_package(self):
        pass

    def start_shipping(self):
        pass

    def track_shipment(self):
        pass

    def deliver_shipment(self):
        pass

    def update_shipment_status(self):
        pass

    def get_all_couriers(self):
        pass

    def get_shipment_information(self):
        pass


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = shipping_pb2_grpc.ShippingStub(channel)
        response = stub.GetAllCouriers(
            shipping_pb2.CourierListRequest(number_of_couriers=3))
        print("Greeter client received: ", response.couriers)


if __name__ == "__main__":
    run()
