from celery import Celery
from service import ShippingService

# using the ampq broker
app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y