from pymongo import MongoClient
from typing import Any, List, Optional
from pydantic import BaseModel, Field, Json


MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DB_NAME = 'cmp7174ecommerce'
COLLECTION_NAME = 'shipmennt'


client = MongoClient(MONGODB_HOST, MONGODB_PORT)
shippment_db = client[DB_NAME][COLLECTION_NAME]


def saveShipment(shipment):
    id = shipment["shipment_id"]
    shippment_db.insert_one(shipment)
    return getShipment(shipment_id=id)

def getAllShipments():
    shipments = shippment_db.find({})
    results = []
    for shipment in shipments:
        results.append(shipment)
    return results

def getShipment(shipment_id: str):
    shipment = shippment_db.find_one({'shipment_id': shipment_id})
    return shipment

def updateShipment(shipment_id, updated_shipment):
    query = {'shipment_id': shipment_id}
    values = {"$set": updated_shipment}
    shippment_db.update_one(query, values)
    return getShipment(shipment_id)

def deleteShipment(shipment_id):
    shipment = shippment_db.delete_one({'shipment_id': shipment_id})
    return shipment
