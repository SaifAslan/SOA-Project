from typing import List
from database import saveShipment, getShipment, updateShipment, getAllShipments
from shipping.address import Address
from shipping.package import Package, Item
from shipping.tracker_factory import get_tracker, get_all_supported_couriers
from shipping.base import Shipment, ShipmentCheckpoint
from utils import get_random_string
import random
import datetime

WEIGHT_PER_ITEM = 7.5  # weight for each item in lbs
SHAPES = ["rectanglar", "square", "wrapped"]


class ShippingService:
    def __init__(self):
        pass

    def calculateShippingCost(self, courier: str, package: Package,
                              source: Address,
                              destination: Address):

        return get_tracker(courier).calculate_cost(source, destination,
                                                   package)

    def calculateShippingCostNoCourier(self, package: Package, source: Address,
                                       destination: Address):
        total = 0
        couriers = get_all_supported_couriers()
        num_couriers = len(couriers)

        for courier in couriers:
            total += get_tracker(courier).calculate_cost(source, destination,
                                                         package)
        avg_cost = total / num_couriers
        return avg_cost

    def createPackage(self, items: List[Item]):
        num_items = len(items)
        weight = WEIGHT_PER_ITEM * num_items
        length = random.randint(3, 11)
        width = random.randint(3, 11)
        height = random.randint(3, 11)
        shape = random.choice(SHAPES)

        package = Package(items=items, weight=weight,
                          length=length, width=width,
                          height=height, shape=shape)
        return package

    def startShipping(self, order_id: str, courier: str, package: Package,
                      user_id: str,
                      source: Address, destination: Address):

        shipment = Shipment(shipment_id=order_id, courier=courier,
                            package=package, user_id=user_id,
                            source=source, destination=destination,
                            tracking_number=get_random_string(),
                            updates=[], found=True, delivered=False, last=None)
        saveShipment(shipment.dict())
        return shipment

    def trackShipment(self, shipment_id: str):
        shipment: Shipment = getShipment(shipment_id)
        # if already delivered then there is no need to do additional tracking
        if shipment["delivered"]:
            return shipment

        # convert to shipment class
        shipment_update = get_tracker(shipment["courier"]).track(shipment_id)

        if shipment_update["status"] == "Delivered":
            shipment["delivered"] = True
            shipment["found"] = True
        shipment["updates"].append(shipment_update)
        shipment["last"] = shipment_update
        updateShipment(shipment_id, shipment)
        return shipment

    def deliverShipment(self, shipment_id: str):
        shipment: Shipment = getShipment(shipment_id)
        if shipment["delivered"]:
            return shipment
        delivery_update = ShipmentCheckpoint(
            status="Delivered",
            location=shipment["destination"]["delivery_point"],
            datetime=datetime.datetime
            .now().strftime("%m/%d/%Y, %H:%M:%S"))
        shipment["updates"].append(delivery_update.dict())
        shipment["last"] = delivery_update.dict()
        shipment["delivered"] = True
        shipment["found"] = True
        updateShipment(shipment_id, shipment)
        return shipment

    def updateShipmentStatus(self, shipment_id, shipment_update):
        shipment: Shipment = getShipment(shipment_id)
        if shipment["delivered"]:
            return shipment
        shipment["updates"].append(shipment_update)
        shipment["last"] = shipment_update
        shipment["found"] = True
        updateShipment(shipment_id, shipment)
        return shipment

    def getAllCouriers(self):
        return get_all_supported_couriers()

    def getShipmentInformation(self, shipment_id):
        shipment: Shipment = getShipment(shipment_id)
        # convert to appropriate shipment type
        return shipment

    def getAllShipments(self, user_id=None, courier=None):
        shipments: List[Shipment] = getAllShipments()
        if user_id:
            shipments = filter(lambda x: x["user_id"] == user_id, shipments)
        if courier:
            shipments = filter(lambda x: x["courier"] == courier, shipments)
        return shipments
