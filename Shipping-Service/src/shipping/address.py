from pydantic import BaseModel

class Address(BaseModel):
    """
    A class representing the address of a user
    """
    state: str
    city: str
    zip: str
    street: str
    delivery_point: str