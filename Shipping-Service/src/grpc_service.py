from concurrent import futures
import logging

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

class ShippingGRPCService(shipping_pb2_grpc.ShippingServicer):
    def CalculateShippingCost(self, request, context):
        return super().CalculateShippingCost(request, context)
    
    def CalculateShippingCostNoCourier(self, request, context):
        return super().CalculateShippingCostNoCourier(request, context)
    
    def CreatePackage(self, request, context):
        return super().CreatePackage(request, context)
    
    def StartShipping(self, request, context):
        return super().StartShipping(request, context)
    
    def TrackShippment(self, request, context):
        return super().TrackShippment(request, context)
    
    def DeliverShipment(self, request, context):
        return super().DeliverShipment(request, context)
    
    def UpdateShipmentStatus(self, request, context):
        return super().UpdateShipmentStatus(request, context)
    
    def GetAllCouriers(self, request, context):
        return super().GetAllCouriers(request, context)
    
    def GetShipmentInformation(self, request, context):
        return super().GetShipmentInformation(request, context)
    
    