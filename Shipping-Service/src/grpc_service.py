from concurrent import futures
from shipping.base import Shipment

import grpc
import shipping_pb2
import shipping_pb2_grpc
from service import ShippingService
from shipping.package import Package, Item
from shipping.address import Address
import random

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
        items.append(from_pydantic_item_to_grpc_item(item))
    grpc_package = shipping_pb2.Package(
        items=items,
        shape=package.shape,
        weight=package.weight,
        length=package.length,
        width=package.width,
        height=package.height
    )
    return grpc_package


def from_obj_to_grpc_package(package):
    items = []
    for item in package["items"]:
        items.append(from_obj_item_to_grpc_item(item))
    grpc_package = shipping_pb2.Package(
        items=items,
        shape=package["shape"],
        weight=package["weight"],
        length=package["length"],
        width=package["width"],
        height=package["height"]
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


def from_obj_address_to_grpc_address(address):
    grpc_address = shipping_pb2.Address(
        state=address["state"],
        city=address["city"],
        zip=address["zip"],
        street=address["street"],
        delivery_point=address["delivery_point"])
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


def from_obj_item_to_grpc_item(item):
    grpc_item = shipping_pb2.Item(
        item_id=item["item_id"],
        name=item["name"],
        count=item["count"],
    )
    return grpc_item


def from_pydantic_shipment_to_grpc_shipment(shipment: Shipment):
    grpc_shipment = shipping_pb2.Shipment(
        shipment_id=shipment.shipment_id,
        user_id=shipment.user_id,
        courier=shipment.courier,
        updates=shipment.updates,
        found=shipment.found,
        delivered=shipment.delivered,
        last=shipment.last,
        package=from_pydantic_package_to_grpc_package(shipment.package),
        source=from_pydantic_address_to_grpc_address(shipment.source),
        destination=from_pydantic_address_to_grpc_address(shipment.destination)
    )
    return grpc_shipment


def from_obj_update_to_grpc_update(update):
    if update is None:
        return None
    grpc_update = shipping_pb2.ShipmentUpdate(
        status=update["status"],
        location=update["location"],
        datetime=update["datetime"]
    )
    return grpc_update


def from_obj_shipment_grpc_shipment(shipment: Shipment):
    grpc_shipment = shipping_pb2.Shipment(
        shipment_id=shipment["shipment_id"],
        user_id=shipment.get("user_id", "Not provided"),
        courier=shipment["courier"],
        updates=[from_obj_update_to_grpc_update(update) for
                 update in shipment["updates"]],
        found=shipment["found"],
        delivered=shipment["delivered"],
        last=from_obj_update_to_grpc_update(shipment["last"]),
        package=from_obj_to_grpc_package(shipment["package"]),
        source=from_obj_address_to_grpc_address(shipment["source"]),
        destination=from_obj_address_to_grpc_address(shipment["destination"])
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
        response = shipping_pb2.EstimateShipmentCostResponse(
                                                    amount=amount,
                                                    days=random.randint(1, 7))
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
        response = shipping_pb2.EstimateShipmentCostResponse(
                                                    amount=amount,
                                                    days=random.randint(1, 7))
        return response

    def CreatePackage(self, request, context):
        items = []
        for item in request.items:
            items.append(from_grpc_item_to_pydantic_item(item))
        package = shippingService.createPackage(items)
        response = from_pydantic_package_to_grpc_package(package)
        return response

    def StartShipping(self, request, context):
        package = from_grpc_package_to_pydantic_package(request.package)
        source = from_grpc_address_to_pydantic_address(request.source)
        destination = from_grpc_address_to_pydantic_address(
            request.destination)
        user_id = request.user_id
        courier = request.courier
        order_id = request.order_id
        print
        shipment = shippingService.startShipping(order_id, courier, package,
                                                 user_id, source, destination)
        response = from_pydantic_shipment_to_grpc_shipment(shipment)
        return response

    def TrackShipment(self, request, context):
        shipping_id = request.shipment_id
        shipment = shippingService.trackShipment(shipping_id)
        response = from_obj_shipment_grpc_shipment(shipment)
        return response

    def DeliverShipment(self, request, context):
        shipment_id = request.shipment_id
        shipment = shippingService.deliverShipment(shipment_id)
        response = from_obj_shipment_grpc_shipment(shipment)
        return response

    def UpdateShipmentStatus(self, request, context):
        print("Starting the process..")
        shipment_id = request.shipment_id
        shipment_update = {
            "status": request.status,
            "location": request.location,
            "datetime": request.datetime
        }
        shipment = shippingService.updateShipmentStatus(shipment_id,
                                                        shipment_update)
        response = from_obj_shipment_grpc_shipment(shipment)
        return response

    def GetAllCouriers(self, request, context):
        couriers = shippingService.getAllCouriers()
        response = shipping_pb2.CourierListResponse(couriers=couriers)
        return response

    def GetShipmentInformation(self, request, context):
        shipment_id = request.shipment_id
        shipment = shippingService.getShipmentInformation(shipment_id)
        response = from_obj_shipment_grpc_shipment(shipment)
        return response

    def GetAllShipments(self, request, context):
        # done
        shipments = shippingService.getAllShipments(request.user_id,
                                                    request.courier)
        grpc_shipments = []
        for shipment in shipments:
            grpc_shipments.append(from_obj_shipment_grpc_shipment(shipment))
        return shipping_pb2.AllShipmentsResponse(shipments=grpc_shipments)


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
