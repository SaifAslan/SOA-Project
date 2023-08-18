from pymongo import MongoClient
import os
# from typing import Any, List, Optional
# from pydantic import BaseModel, Field, Json
mongo_user = 'root'
mongo_password = 'examplepassword'
auth_db = 'admin'

MONGODB_HOST = os.environ.get("MONGODB_HOST", 'localhost')
MONGODB_PORT = 27017
DB_NAME = 'cmp7174ecommerce'
COLLECTION_NAME = 'shipment'


client = MongoClient(host=MONGODB_HOST, port=MONGODB_PORT,
                     username=mongo_user, password=mongo_password,
                     authSource=auth_db)
shippment_db = client[DB_NAME][COLLECTION_NAME]


def saveShipment(shipment):
    id = shipment["shipment_id"]
    shippment_db.insert_one(shipment)
    return getShipment(shipment_id=id)


def getAllShipments():
    shipments = shippment_db.find({})
    results = []
    for shipment in shipments:
        del shipment["_id"]
        results.append(shipment)
    return results


def getShipment(shipment_id: str):
    shipment = shippment_db.find_one({'shipment_id': shipment_id})
    del shipment["_id"]
    return shipment


def updateShipment(shipment_id, updated_shipment):
    query = {'shipment_id': shipment_id}
    values = {"$set": updated_shipment}
    shippment_db.update_one(query, values)
    return getShipment(shipment_id)


def deleteShipment(shipment_id):
    shipment = shippment_db.delete_one({'shipment_id': shipment_id})
    del shipment["_id"]
    return shipment
