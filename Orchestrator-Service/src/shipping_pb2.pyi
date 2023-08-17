from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Address(_message.Message):
    __slots__ = ["state", "city", "zip", "street", "delivery_point"]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    ZIP_FIELD_NUMBER: _ClassVar[int]
    STREET_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_POINT_FIELD_NUMBER: _ClassVar[int]
    state: str
    city: str
    zip: str
    street: str
    delivery_point: str
    def __init__(self, state: _Optional[str] = ..., city: _Optional[str] = ..., zip: _Optional[str] = ..., street: _Optional[str] = ..., delivery_point: _Optional[str] = ...) -> None: ...

class Item(_message.Message):
    __slots__ = ["item_id", "name", "count"]
    ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    item_id: str
    name: str
    count: int
    def __init__(self, item_id: _Optional[str] = ..., name: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class Package(_message.Message):
    __slots__ = ["items", "shape", "weight", "length", "width", "height"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    SHAPE_FIELD_NUMBER: _ClassVar[int]
    WEIGHT_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Item]
    shape: str
    weight: float
    length: float
    width: float
    height: float
    def __init__(self, items: _Optional[_Iterable[_Union[Item, _Mapping]]] = ..., shape: _Optional[str] = ..., weight: _Optional[float] = ..., length: _Optional[float] = ..., width: _Optional[float] = ..., height: _Optional[float] = ...) -> None: ...

class ShipmentUpdate(_message.Message):
    __slots__ = ["status", "location", "datetime"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    status: str
    location: str
    datetime: str
    def __init__(self, status: _Optional[str] = ..., location: _Optional[str] = ..., datetime: _Optional[str] = ...) -> None: ...

class ShipmentUpdateRequest(_message.Message):
    __slots__ = ["shipment_id", "status", "location", "datetime"]
    SHIPMENT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    shipment_id: str
    status: str
    location: str
    datetime: str
    def __init__(self, shipment_id: _Optional[str] = ..., status: _Optional[str] = ..., location: _Optional[str] = ..., datetime: _Optional[str] = ...) -> None: ...

class Shipment(_message.Message):
    __slots__ = ["shipment_id", "user_id", "courier", "updates", "found", "delivered", "last", "package", "source", "destination"]
    SHIPMENT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    COURIER_FIELD_NUMBER: _ClassVar[int]
    UPDATES_FIELD_NUMBER: _ClassVar[int]
    FOUND_FIELD_NUMBER: _ClassVar[int]
    DELIVERED_FIELD_NUMBER: _ClassVar[int]
    LAST_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    shipment_id: str
    user_id: str
    courier: str
    updates: _containers.RepeatedCompositeFieldContainer[ShipmentUpdate]
    found: bool
    delivered: bool
    last: ShipmentUpdate
    package: Package
    source: Address
    destination: Address
    def __init__(self, shipment_id: _Optional[str] = ..., user_id: _Optional[str] = ..., courier: _Optional[str] = ..., updates: _Optional[_Iterable[_Union[ShipmentUpdate, _Mapping]]] = ..., found: bool = ..., delivered: bool = ..., last: _Optional[_Union[ShipmentUpdate, _Mapping]] = ..., package: _Optional[_Union[Package, _Mapping]] = ..., source: _Optional[_Union[Address, _Mapping]] = ..., destination: _Optional[_Union[Address, _Mapping]] = ...) -> None: ...

class ShippingRequest(_message.Message):
    __slots__ = ["courier", "user_id", "package", "source", "destination", "order_id"]
    COURIER_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    courier: str
    user_id: str
    package: Package
    source: Address
    destination: Address
    order_id: str
    def __init__(self, courier: _Optional[str] = ..., user_id: _Optional[str] = ..., package: _Optional[_Union[Package, _Mapping]] = ..., source: _Optional[_Union[Address, _Mapping]] = ..., destination: _Optional[_Union[Address, _Mapping]] = ..., order_id: _Optional[str] = ...) -> None: ...

class RequestCreatePackage(_message.Message):
    __slots__ = ["items"]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[Item]
    def __init__(self, items: _Optional[_Iterable[_Union[Item, _Mapping]]] = ...) -> None: ...

class EstimateShipmentCostNoCourier(_message.Message):
    __slots__ = ["package", "source", "destination"]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    package: Package
    source: Address
    destination: Address
    def __init__(self, package: _Optional[_Union[Package, _Mapping]] = ..., source: _Optional[_Union[Address, _Mapping]] = ..., destination: _Optional[_Union[Address, _Mapping]] = ...) -> None: ...

class EstimateShipmentCost(_message.Message):
    __slots__ = ["courier", "package", "source", "destination"]
    COURIER_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    courier: str
    package: Package
    source: Address
    destination: Address
    def __init__(self, courier: _Optional[str] = ..., package: _Optional[_Union[Package, _Mapping]] = ..., source: _Optional[_Union[Address, _Mapping]] = ..., destination: _Optional[_Union[Address, _Mapping]] = ...) -> None: ...

class EstimateShipmentCostResponse(_message.Message):
    __slots__ = ["amount", "days"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    amount: float
    days: int
    def __init__(self, amount: _Optional[float] = ..., days: _Optional[int] = ...) -> None: ...

class ShipmentTrackRequest(_message.Message):
    __slots__ = ["shipment_id"]
    SHIPMENT_ID_FIELD_NUMBER: _ClassVar[int]
    shipment_id: str
    def __init__(self, shipment_id: _Optional[str] = ...) -> None: ...

class CourierListResponse(_message.Message):
    __slots__ = ["couriers"]
    COURIERS_FIELD_NUMBER: _ClassVar[int]
    couriers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, couriers: _Optional[_Iterable[str]] = ...) -> None: ...

class CourierListRequest(_message.Message):
    __slots__ = ["number_of_couriers"]
    NUMBER_OF_COURIERS_FIELD_NUMBER: _ClassVar[int]
    number_of_couriers: int
    def __init__(self, number_of_couriers: _Optional[int] = ...) -> None: ...

class AllShipmentsResponse(_message.Message):
    __slots__ = ["shipments"]
    SHIPMENTS_FIELD_NUMBER: _ClassVar[int]
    shipments: _containers.RepeatedCompositeFieldContainer[Shipment]
    def __init__(self, shipments: _Optional[_Iterable[_Union[Shipment, _Mapping]]] = ...) -> None: ...

class GetAllShipmentsRequest(_message.Message):
    __slots__ = ["courier", "user_id"]
    COURIER_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    courier: str
    user_id: str
    def __init__(self, courier: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...
