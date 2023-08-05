from celery import Celery
from service import ShippingService

# using the ampq broker
# celery worker to perform asynchonous tasks of getting information 
app = Celery('tasks', broker='pyamqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y