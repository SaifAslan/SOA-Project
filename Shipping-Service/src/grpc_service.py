from concurrent import futures
from shipping.base import Shipment

import grpc
import shipping_pb2
import shipping_pb2_grpc
from service import ShippingService
from shipping.package import Package, Item
from shipping.address import Address

# create shipping service to be used for the operations
shippingService = ShippingService()


def from_grpc_package_to_pydantic_package(package):
    items = []
    for item in package.items:
        items.append(from_grpc_item_to_pydantic_item(item))
    pydantic_package = Package(
        items=items,
        shape=package.shape,
        weight=package.weight,
        length=package.length,
        width=package.width,
        height=package.height
    )
    return pydantic_package


def from_pydantic_package_to_grpc_package(package):
    items = []
    for item in package.items:
        item.append(from_pydantic_item_to_grpc_item(item))
    grpc_package = shipping_pb2.Package(
        items=items,
        shape=package.shape,
        weight=package.weight,
        length=package.length,
        width=package.width,
        height=package.height
    )
    return grpc_package


def from_grpc_address_to_pydantic_address(address):
    pydantic_address = Address(
        state=address.state,
        city=address.city,
        zip=address.zip,
        street=address.street,
        delivery_point=address.delivery_point
    )
    return pydantic_address


def from_pydantic_address_to_grpc_address(address):
    grpc_address = shipping_pb2.Address(state=address.state,
                                        city=address.city,
                                        zip=address.zip,
                                        street=address.street,
                                        delivery_point=address.delivery_point)
    return grpc_address


def from_grpc_item_to_pydantic_item(item):
    pydantic_item = Item(
        item_id=item.item_id,
        name=item.name,
        count=item.count,
    )
    return pydantic_item


def from_pydantic_item_to_grpc_item(item):
    grpc_item = shipping_pb2.Item(
        item_id=item.item_id,
        name=item.name,
        count=item.count,
    )
    return grpc_item


def from_pydantic_shipment_to_grpc_shipment(shipment: Shipment):
    grpc_shipment = shipping_pb2.Shipment(
        shipment_id=shipment.shipment_id,
        user_id="testing",
        courier=shipment.courier,
        updates=shipment.updates,
        found=shipment.found,
        delivered=shipment.delivered,
        last=shipment.last,
        package=shipment.package
    )
    return grpc_shipment


class ShippingGRPCService(shipping_pb2_grpc.ShippingServicer):
    def CalculateShippingCost(self, request, context):
        pydantic_package = from_grpc_package_to_pydantic_package(
            request.package)
        pydantic_source = from_grpc_address_to_pydantic_address(
            request.source)
        pydantic_destination = from_grpc_address_to_pydantic_address(
            request.destination)
        courier = request.courier

        amount = shippingService.calculateShippingCost(courier,
                                                       pydantic_package,
                                                       pydantic_source,
                                                       pydantic_destination)
        response = shipping_pb2.EstimateShipmentCostResponse(amount, 0)
        return response

    def CalculateShippingCostNoCourier(self, request, context):
        pydantic_package = from_grpc_package_to_pydantic_package(
            request.package)
        pydantic_source = from_grpc_address_to_pydantic_address(
            request.source)
        pydantic_destination = from_grpc_address_to_pydantic_address(
            request.destination)

        amount = shippingService.calculateShippingCostNoCourier(
            pydantic_package, pydantic_source, pydantic_destination)
        response = shipping_pb2.EstimateShipmentCostResponse(amount, 0)
        return response

    def CreatePackage(self, request, context):
        items = []
        for item in request.items:
            item.append(from_grpc_item_to_pydantic_item(item))
        package = shippingService.createPackage(items)
        response = from_pydantic_package_to_grpc_package(package)
        return response

    def StartShipping(self, request, context):
        package = from_grpc_package_to_pydantic_package(request.package)
        # source = from_grpc_address_to_pydantic_address(request.source)
        # destination = from_grpc_address_to_pydantic_address(
        #     request.destination)
        # user_id = "testing"
        courier = request.courier
        shipment = shippingService.startShipping(courier, package)
        response = from_pydantic_shipment_to_grpc_shipment(shipment)
        return response

    def TrackShippment(self, request, context):
        shipping_id = request.shipping_id
        shipment = shippingService.trackShippment(shipping_id)
        response = from_pydantic_shipment_to_grpc_shipment(shipment)
        return response

    def DeliverShipment(self, request, context):
        shipment_id = request.shipment_id
        shipment = shippingService.deliverShipment(shipment_id)
        response = from_pydantic_shipment_to_grpc_shipment(shipment)
        return response

    def UpdateShipmentStatus(self, request, context):
        return super().UpdateShipmentStatus(request, context)

    def GetAllCouriers(self, request, context):
        couriers = shippingService.getAllCouriers()
        response = shipping_pb2.CourierListResponse(couriers=couriers)
        return response

    def GetShipmentInformation(self, request, context):
        shipment_id = request.shipment_id
        shipment = shippingService.getShipmentInformation(shipment_id)
        response = from_pydantic_shipment_to_grpc_shipment(shipment)
        return response


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


if __name__ == "__main__":
    serveGRPC()
