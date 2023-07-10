from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from enum import Enum
from shipping.base import Shipment, ShipmentCheckpoint
from shipping.package import Package, Item


app = FastAPI(title="cmp7174 shipping",
              description="""**CMP7174 Shipping Service** This service manages the shipping of goods in our
              ecommerce project. The service manages tracking of shipment from various couriers and serves it in a 
              unified GRPC and REST service. The service persists data on a MongoDB database.""",
              version="0.1.3", docs_url="/documentation", redoc_url="/redoc"
              )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/calculateShippingCost")
def calculateShippingCost():
    pass

@app.post("/calculateShippingCostNoCourier")
def calculateShippingCostNoCourier():
    pass

@app.post("/createPackage")
def createPackage():
    pass

@app.post("/startShipping")
def startShipping():
    pass

@app.get("/trackShipment/{shipment_id}")
def trackShipment(shipment_id: str):
    pass

@app.get("/deliverShipment/{shipment_id}")
def deliverShipment(shipment_id: str):
    pass

@app.post("/updateShipmentStatus/{shipment_id}")
def updateShipmentStatus(shipment_id:str):
    pass

@app.get("/getAllCouriers")
def getAllCouriers():
    pass

@app.get("/getShipmentInformation/{shipment_id}")
def getShipmentInformation(shipment_id:str):
    pass
