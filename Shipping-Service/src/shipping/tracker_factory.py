from abc import ABC, abstractmethod


class TrackerFactory(ABC):
    @abstractmethod
    def get_tracker(self):
        raise NotImplementedError
    

# keeps track of all the shipping vendors
venders = dict()


def get_tracker_class(vendor_name: str):
    vendor_name = vendor_name.lower()
    vendor_class = venders.get(vendor_name, None)
    if vendor_class is None:
        raise NotImplementedError("Tracking vender not available")
    vendor_class_instance = vendor_class()
    return vendor_class_instance