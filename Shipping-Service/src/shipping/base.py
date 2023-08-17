from abc import ABC, abstractmethod
from pydantic import BaseModel
from datetime import datetime
from typing import List
from shipping.package import Package
from shipping.address import Address


def format_timestamp(input_date: datetime):
    temp = input_date.timestamp()
    temp = str(temp).split('.')[0]
    return temp


DELIVERED = 'delivered'


class InvalidShippingNumber(ValueError):
    '''
    This is an error that is thrown wnen an invalid tracking number
    is provided
    '''
    def __init__(self, message):
        self.message = message
        super(InvalidShippingNumber, self).__init__()


class ShipmentCheckpoint(BaseModel):
    """
    Represents a tracking checkpoint
    """
    status: str
    location: str
    datetime: str


class Shipment(BaseModel):
    """
    Represents the tracking results for a parcel
    """
    shipment_id: str
    user_id: str
    courier: str
    tracking_number: str
    package: Package
    source: Address
    destination: Address
    updates: List[ShipmentCheckpoint]
    found: bool
    delivered: bool
    last: ShipmentCheckpoint = None

    # def __post_init__(self):
    #     """
    #     If the tracking results is initalized with updates
    #     update the values of found, last and check if the last update has a
    #     status of delivered
    #     """
    #     self.found = False
    #     self.last = None
    #     if len(self.updates) > 0:
    #         self.found = True
    #         self.last = sorted(self.updates, key=lambda k: k.datetime)[-1]
    #         if self.last.status == DELIVERED:
    #             self.delivered = True


class CourierTracker(ABC):
    """
    Basic representation of a tracker
    """
    @abstractmethod
    def sanitize(self, tracking_number: str):
        """
        Sanitize a given tracking number
        """
        raise NotImplementedError

    @abstractmethod
    def fetch_results(self, tracking_number: str):
        """
        Fetch the results for a given tracking number
        """
        raise NotImplementedError

    @abstractmethod
    def parse_results(self, tracking_info: str):
        """
        Parse the results of given tracking number
        """
        raise NotImplementedError

    @abstractmethod
    def track(self, tracking_number: str):
        """
        Tracks the given tracking number
        """
        raise NotImplementedError

    @abstractmethod
    def track_silently(self, tracking_number: str):
        """
        Track a given item silently given the tracking number
        """
        raise NotImplementedError

    @abstractmethod
    def calculate_cost(self, source: Address, target: Address,
                       package: Package):
        raise NotImplementedError
