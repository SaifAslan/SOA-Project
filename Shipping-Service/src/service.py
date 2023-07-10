from typing import List
from database import saveShipment, getShipment, updateShipment
from shipping.address import Address
from shipping.package import Package, Item
from shipping.tracker_factory import get_tracker, get_all_supported_couriers
from shipping.base import Shipment, ShipmentCheckpoint
from utils import get_random_string
import random
import datetime


WEIGHT_PER_ITEM = 7.5 # weight for each item in lbs
SHAPES = ["rectanglar", "square", "wrapped"]

class ShippingService:
    def __init__(self):
        pass
    def calculateShippingCost(courier: str, package: Package, source: Address, 
                              destination: Address):
        
        return get_tracker(courier).calculate_cost(source, destination, package)
        
    def calculateShippingCostNoCourier(package: Package, source: Address, destination: Address):
        total = 0
        couriers = get_all_supported_couriers()
        num_couriers = len(couriers)
        
        for courier in couriers:
            total += get_tracker(courier).calculate_cost(source, destination, package)
        avg_cost = total / num_couriers
        return avg_cost
        
    def createPackage(items: List[Item]):
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
    
    def startShipping(courier: str, package: Package):
        shipment = Shipment(courier=courier, package=package, tracking_number=get_random_string(), updates=[], found=True, delivered=False, last=None)
        saveShipment(shipment)
        return shipment
    
    def trackShippment(shipment_id: str):
        shipment:Shipment = getShipment(shipment_id)
        # convert to shipment class
        shipment_update = get_tracker(shipment.courier).track(shipment_id)
        shipment.updates.append(shipment_update)
        shipment.last = shipment_update
        updateShipment(shipment_id, shipment)
        return shipment
    
    def deliverShipment(shipment_id: str):
        delivery_update = ShipmentCheckpoint(status="delivered", location="final destination", datetime=datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        shipment:Shipment = getShipment(shipment_id)
        shipment.updates.append(delivery_update)
        shipment.last = delivery_update
        shipment.delivered = True
        shipment.found = True
        updateShipment(shipment_id, shipment)
        return shipment

    def updateShipmentStatus(shipment_id, shipment_update):
        shipment:Shipment = getShipment(shipment_id)
        shipment.updates.append(shipment_update)
        shipment.last = shipment_update
        shipment.found = True
        updateShipment(shipment_id, shipment)
        return shipment
    
    def getAllCouriers():
        return get_all_supported_couriers()
    
    def getShipmentInformation(shipment_id):
        shipment:Shipment = getShipment(shipment_id)
        # convert to appropriate shipment type
        return shipment