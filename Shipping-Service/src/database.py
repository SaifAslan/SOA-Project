from pymongo import MongoClient
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DB_NAME = 'cmp7174ecommerce'
COLLECTION_NAME = 'shipmennt'

client = MongoClient(MONGODB_HOST, MONGODB_PORT)
shippment_db = client[DB_NAME][COLLECTION_NAME]


def saveShipment(shipment):
    response = shippment_db.insert_one(shipment)
    print(response)
    return shipment

def getAllShipments():
    shipments = shippment_db.find({})
    return shipments

def getShipment(shipment_id: str):
    shipment = shippment_db.find_one({'shipment_id': shipment_id})
    return shipment

def updateShipment(shipment_id, updated_shipment):
    response = shippment_db.find_one_and_update(filter={'shipment_id': shipment_id}, update=updated_shipment)
    print(response)
    return updated_shipment