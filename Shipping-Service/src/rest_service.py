from typing import List
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from shipping.package import Package, Item
from shipping.address import Address

from service import ShippingService
from pydantic import BaseModel


app = FastAPI(title="cmp7174 shipping",
              description="""**CMP7174 Shipping Service** This service manages
              the shipping of goods in our ecommerce project.
              The service manages  tracking of shipment from
              various couriers and serves it in a unified GRPC and
              REST service. The service persists data on a
              MongoDB database.""",
              version="0.1.3", docs_url="/documentation", redoc_url="/redoc"
              )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class ShippingRequest(BaseModel):
    package: Package
    source: Address
    destination: Address


class ShippingRequestWithCourier(ShippingRequest):
    courier: str


class CreatePackageRequest(BaseModel):
    items: List[Item]


class StartShippingRequest(BaseModel):
    order_id: str
    user_id: str
    courier: str
    package: Package
    source: Address
    destination: Address


# create shipping service to be used for the operations
shippingService = ShippingService()


@app.post("/calculateShippingCost/")
def calculateShippingCost(sr: ShippingRequestWithCourier):
    amount = shippingService.calculateShippingCost(sr.courier, sr.package,
                                                   sr.source, sr.destination)
    return amount


@app.post("/calculateShippingCostNoCourier")
def calculateShippingCostNoCourier(sr: ShippingRequest):
    amount = shippingService.calculateShippingCostNoCourier(sr.package,
                                                            sr.source,
                                                            sr.destination)
    return amount


@app.post("/createPackage")
def createPackage(pr: CreatePackageRequest):
    package = shippingService.createPackage(pr.items)
    return package


@app.post("/startShipping")
def startShipping(ssr: StartShippingRequest):
    shipment = shippingService.startShipping(ssr.order_id, ssr.courier,
                                             ssr.package, ssr.user_id,
                                             ssr.source, ssr.destination)
    return shipment


@app.get("/trackShipment/{shipment_id}")
def trackShipment(shipment_id: str):
    shipment = shippingService.trackShipment(shipment_id)
    return shipment


@app.get("/deliverShipment/{shipment_id}")
def deliverShipment(shipment_id: str):
    shipment = shippingService.deliverShipment(shipment_id)
    return shipment


@app.post("/updateShipmentStatus/{shipment_id}")
def updateShipmentStatus(shipment_id: str):
    shipment = shippingService.updateShipmentStatus(shipment_id, {})
    return shipment


@app.get("/getAllCouriers")
def getAllCouriers():
    couriers = shippingService.getAllCouriers()
    return {"couriers": couriers}


@app.get("/getShipmentInformation/{shipment_id}")
def getShipmentInformation(shipment_id: str):
    shipment = shippingService.getShipmentInformation(shipment_id)
    return shipment


@app.get("/getAllShipments")
def getAllShipmentInformation(user_id: str = None, courier: str = None):
    shipments = shippingService.getAllShipments(user_id, courier)
    return shipments


def serveHTTP():
    print("Starting HTTP Server")
    port = 8000
    host = "0.0.0.0"
    print("HTTP Server started, listening on ", port)
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    serveHTTP()
