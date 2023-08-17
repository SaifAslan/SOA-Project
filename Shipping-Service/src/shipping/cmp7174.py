from shipping.address import Address
from shipping.package import Package
from shipping.base import CourierTracker
import random
from datetime import datetime

epsilone = 0.1


def generate_random_location():
    locations = ["New York", "Paris", "Birmingham", "London", "San Fransisco"]
    choice = random.choice(locations)
    return choice


def generate_shipment_status():
    status = ["Ongoing", "Packaging", "Checking", "Delivered"]
    choice = random.choices(status, weights=[30, 30, 30, 10], k=1)[0]
    return choice


class CMP7174Tracker(CourierTracker):
    """
    Basic representation of a tracker
    """
    def sanitize(self, tracking_number: str):
        """
        Sanitize a given tracking number
        """
        cleaned_number = str(tracking_number).replace(' ', '').strip()
        return cleaned_number

    def fetch_results(self, tracking_number: str):
        """
        Fetch the results for a given tracking number
        """
        # generate random tracking results
        status = generate_shipment_status()
        location = generate_random_location()

        results = {
            "status": status,
            "location": location,
            "datetime": datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        }
        return results

    def parse_results(self, results):
        """
        Parse the results of given tracking number
        """
        # clean randomly generated results from tracking info
        cleaned_results = results
        return cleaned_results

    def track(self, tracking_number: str):
        """
        Tracks the given tracking number
        """
        tracking_number = self.sanitize(tracking_number)
        results = self.fetch_results(tracking_number)
        results = self.parse_results(results)

        return results

    def track_silently(self, tracking_number: str):
        """
        Track a given item silently given the tracking number
        """
        return self.track(tracking_number)

    def calculate_cost(self, source: Address, target: Address,
                       package: Package):
        return 199.99
