from concurrent import futures
import logging

import grpc
import shipping_pb2
import shipping_pb2_grpc
from service import ShippingService

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
    
    