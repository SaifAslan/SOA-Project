import grpc
import shipping_pb2
import shipping_pb2_grpc


def from_obj_to_grpc_package(package):
    grpc_package = shipping_pb2.Package(
                        shape=package["shape"],
                        weight=package["weight"],
                        length=package["length"],
                        width=package["width"],
                        height=package["height"],
                        items=[from_obj_item_to_grpc_item(item)
                               for item in package["items"]]
                    )
    return grpc_package


def from_obj_to_grpc_address(source):
    grpc_address = shipping_pb2.Address(
                        state=source["state"],
                        city=source["city"],
                        zip=source["zip"],
                        street=source["street"],
                        delivery_point=source["delivery_point"]
                    )
    return grpc_address


def from_grpc_address_to_obj(source):
    data = {
        "state": source.state,
        "city": source.city,
        "zip": source.zip,
        "street": source.street,
        "delivery_point": source.delivery_point
    }
    return data


def from_grpc_item_to_obj_item(item):
    obj_item = {
        "item_id": item.item_id,
        "name": item.name,
        "count": item.count,
    }
    return obj_item


def from_grpc_package_to_obj(response):
    data = {
        "items": [from_grpc_item_to_obj_item(item) for
                  item in response.items],
        "shape": response.shape,
        "weight": response.weight,
        "length": response.length,
        "width": response.width,
        "height": response.height,
    }
    return data


def from_obj_item_to_grpc_item(item):
    grpc_item = shipping_pb2.Item(
        item_id=item["item_id"],
        name=item["name"],
        count=item["count"],
    )
    return grpc_item


def from_grpc_update_to_obj(update):
    update = {
        "status": update.status,
        "location": update.location,
        "datetime": update.datetime
    }
    return update


def from_grpc_shipment_to_obj_shipment(shipment):
    obj_shipment = {
        "shipment_id": shipment.shipment_id,
        "user_id": shipment.user_id,
        "courier": shipment.courier,
        "updates": [from_grpc_update_to_obj(update) for
                    update in shipment.updates],
        "found": shipment.found,
        "delivered": shipment.delivered,
        "last": from_grpc_update_to_obj(shipment.last),
        "package": from_grpc_package_to_obj(shipment.package),
        "source": from_grpc_address_to_obj(shipment.source),
        "destination": from_grpc_address_to_obj(shipment.destination)
    }
    return obj_shipment


class ShippingService():
    def __init__(self):
        self.port = 'localhost:50051'

    def calculateShippingCost(self, courier, package,
                              source, destination):
        with grpc.insecure_channel(self.port) as channel:
            stub = shipping_pb2_grpc.ShippingStub(channel)
            print("I am here")
            response = stub.CalculateShippingCost(
                shipping_pb2.EstimateShipmentCost(
                    courier=courier,
                    package=from_obj_to_grpc_package(package.dict()),
                    source=from_obj_to_grpc_address(source.dict()),
                    destination=from_obj_to_grpc_address(destination.dict())
                ))
        print("I have gotten the response")
        return {
            "amount": response.amount,
            "days": response.days
            }

    def calculateShippingCostNoCourier(self, package, source, destination):
        with grpc.insecure_channel(self.port) as channel:
            stub = shipping_pb2_grpc.ShippingStub(channel)
            response = stub.CalculateShippingCostNoCourier(
                shipping_pb2.EstimateShipmentCostNoCourier(
                    package=from_obj_to_grpc_package(package.dict()),
                    source=from_obj_to_grpc_address(source.dict()),
                    destination=from_obj_to_grpc_address(destination.dict())
                ))
        return {
                "amount": response.amount,
                "days": response.days
            }

    def createPackage(self, items):
        with grpc.insecure_channel(self.port) as channel:
            stub = shipping_pb2_grpc.ShippingStub(channel)
            response = stub.CreatePackage(
                    shipping_pb2.RequestCreatePackage(
                        items=[from_obj_item_to_grpc_item(item.dict())
                               for item in items]
                    )
                )
            return from_grpc_package_to_obj(response)

    def startShipping(self, order_id, courier, package, user_id,
                      source, destination):
        with grpc.insecure_channel(self.port) as channel:
            stub = shipping_pb2_grpc.ShippingStub(channel)
            print("About to make the request")
            response = stub.StartShipping(
                    shipping_pb2.ShippingRequest(
                        order_id=order_id,
                        courier=courier,
                        user_id=user_id,
                        package=from_obj_to_grpc_package(package.dict()),
                        source=from_obj_to_grpc_address(source.dict()),
                        destination=from_obj_to_grpc_address(
                            destination.dict()),
                    )
                )
            return from_grpc_shipment_to_obj_shipment(response)

    def trackShipment(self, shipment_id):
        with grpc.insecure_channel(self.port) as channel:
            stub = shipping_pb2_grpc.ShippingStub(channel)
            print("about to make request")
            response = stub.TrackShipment(
                    shipping_pb2.ShipmentTrackRequest(
                        shipment_id=shipment_id
                    )
                )
            return from_grpc_shipment_to_obj_shipment(response)

    def deliverShipment(self, shipment_id, status, location, datetime):
        with grpc.insecure_channel(self.port) as channel:
            stub = shipping_pb2_grpc.ShippingStub(channel)
            response = stub.DeliverShipment(
                    shipping_pb2.ShipmentUpdateRequest(
                        shipment_id=shipment_id,
                        status=status,
                        location=location,
                        datetime=datetime
                    )
                )
            return from_grpc_shipment_to_obj_shipment(response)

    def updateShipmentStatus(self, shipment_id, status, location, datetime):
        with grpc.insecure_channel(self.port) as channel:
            stub = shipping_pb2_grpc.ShippingStub(channel)
            print("making request.....")
            response = stub.UpdateShipmentStatus(
                    shipping_pb2.ShipmentUpdateRequest(
                        shipment_id=shipment_id,
                        status=status,
                        location=location,
                        datetime=datetime
                    )
                )
            return from_grpc_shipment_to_obj_shipment(response)

    def getAllCouriers(self):
        with grpc.insecure_channel(self.port) as channel:
            stub = shipping_pb2_grpc.ShippingStub(channel)
            response = stub.GetAllCouriers(
                shipping_pb2.CourierListRequest(number_of_couriers=3))
        couriers = []
        # move all couriers into a python list
        for courier in response.couriers:
            couriers.append(courier)

        return {"couriers": couriers}

    def getShipmentInformation(self, shipment_id):
        with grpc.insecure_channel(self.port) as channel:
            stub = shipping_pb2_grpc.ShippingStub(channel)
            response = stub.GetShipmentInformation(
                    shipping_pb2.ShipmentTrackRequest(
                        shipment_id=shipment_id
                    )
                )
            return from_grpc_shipment_to_obj_shipment(response)

    def getAllShipmentInformation(self, user_id, courier):
        with grpc.insecure_channel(self.port) as channel:
            stub = shipping_pb2_grpc.ShippingStub(channel)
            response = stub.GetAllShipments(
                    shipping_pb2.GetAllShipmentsRequest(
                        user_id=user_id,
                        courier=courier,
                    )
                )
            shipments = []
            for shipment in response.shipments:
                shipments.append(from_grpc_shipment_to_obj_shipment(shipment))
            return {
                "shipments": shipments
            }
