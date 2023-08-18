from ast import List
from shipping.base import Shipment
from celery import Celery
from service import ShippingService
from database import getAllShipments, updateShipment


# using the ampq broker
# celery worker to perform asynchonous tasks of getting information
app = Celery('tasks', broker='pyamqp://guest@localhost//')


@app.task
def updateAllShipmentStatus():
    # This is a job to update the shipment status of all shipemnts
    shippingService = ShippingService()
    shipments: List[Shipment] = getAllShipments()
    for shipment in shipments:
        current_state = shippingService.trackShippment(shipment["id"])
        shipment.updates.append(current_state)
        updateShipment(shipment["id"], shipment)


app.conf.beat_schedule = {
    "run-me-every-ten-seconds": {
        "task": "tasks.updateAllShipmentStatus",
        "schedule": 86400,
    }
}
