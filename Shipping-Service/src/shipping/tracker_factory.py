from abc import ABC, abstractmethod

from shipping.base import CourierTracker
from shipping.cmp7174 import CMP7174Tracker
from shipping.easymail import EasyMailTracker
from shipping.speedex import SpeedexTracker
from shipping.usps import USPSTracker


class TrackerFactory(ABC):
    @abstractmethod
    def get_tracker(self):
        raise NotImplementedError


# keeps track of all the shipping vendors
vendors = dict()

# register all the trackers we have on the system
vendors['cmp7174'] = CMP7174Tracker
vendors['easymail'] = EasyMailTracker
vendors['speedex'] = SpeedexTracker
vendors['usps'] = USPSTracker


# retrieves the courier tracker clas based on the vendor name
def get_tracker(vendor_name: str) -> CourierTracker:
    vendor_name = vendor_name.lower()
    vendor_class = vendors.get(vendor_name, None)
    if vendor_class is None:
        raise NotImplementedError("Tracking vendor not available")
    vendor_class_instance = vendor_class()
    return vendor_class_instance


def get_all_supported_couriers():
    couriers = []
    for k, v in vendors.items():
        couriers.append(k)
    # return all the couriers stored in the vendors map
    return couriers
