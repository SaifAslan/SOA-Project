from dataclasses import dataclass


@dataclass
class Package:
    rectangular: str
    weight: str
    length: str
    width: str
    height: str
    origin: str
    destination: str
    tracking_id: str
    