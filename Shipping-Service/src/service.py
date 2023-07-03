
from typing import List

from shipping.address import Address
from shipping.package import Package, Item
from shipping.tracker_factory import get_tracker, get_all_supported_couriers
import random


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
        pass
    
    def trackShippment():
        pass
    
    def deliverShipment():
        pass
    
    def updateShipmentStatus():
        pass