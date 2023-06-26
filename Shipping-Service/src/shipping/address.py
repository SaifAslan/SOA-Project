from dataclasses import dataclass

@dataclass
class Address:
    """
    A class representing the address of a user
    """
    state: str
    city: str
    zip: str
    street: str
    delivery_point: str
    carrier_route: str