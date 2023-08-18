from typing import List
from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from orders import OrdersService
from shipping import ShippingService
import random


# from pydantic import BaseModel

app = FastAPI(title="cmp7174 orchestration service",
              description="""**CMP7174 Orchestrations Service**
              this service orchestrates all other subervices
              into a single service that can be consumed
              by the frontend""",
              version="0.1.3", docs_url="/documentation", redoc_url="/redoc"
              )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

ordersService = OrdersService()
shippingService = ShippingService()


class Item(BaseModel):
    item_id: str
    name: str
    count: int


class Package(BaseModel):
    items: List[Item]
    shape: str
    weight: float
    length: float
    width: float
    height: float


class Address(BaseModel):
    """
    A class representing the address of a user
    """
    state: str
    city: str
    zip: str
    street: str
    delivery_point: str


class ShippingRequest(BaseModel):
    source: Address
    destination: Address


class ShippingRequestWithItems(ShippingRequest):
    items: List[Item]


class CreatePackageRequest(BaseModel):
    items: List[Item]


class StartShippingRequest(BaseModel):
    package: Package
    source: Address
    destination: Address


class CartItem(BaseModel):
    productId: str
    name: str
    quantity: int
    amount: float


class CartDataRequest(BaseModel):
    userId: str
    cartItem: List[CartItem]


class CartData(CartDataRequest):
    cartId: str
    status: str = "Pending"


def get_random_id():
    # choose from all lowercase letter
    letters = ["1", "2", "3", "4", "5", "6",
               "7", "8", "9", "0"]
    result_str = ''.join(random.choice(letters) for i in range(5))
    return int(result_str)


@app.post("/CalculateShippingCostNoCourier")
def calculateShippingCostNoCourier(sr: ShippingRequestWithItems):
    cpr = CreatePackageRequest(items=sr.items)
    package = createPackage(cpr)
    del package["items"]
    package = Package(
        items=sr.items,
        **package
    )
    return shippingService.calculateShippingCostNoCourier(package,
                                                          sr.source,
                                                          sr.destination)


@app.post("/CreatePackage")
def createPackage(pr: CreatePackageRequest):
    return shippingService.createPackage(pr.items)


@app.post("/CreateOrder")
def postCartRequest(cartData: CartDataRequest):
    cartData = cartData.dict()
    cartData["cartId"] = get_random_id()
    cartData["status"] = "Pending"
    return ordersService.postCartRequest(cartData)


@app.post("/StartShipping/{order_id}")
def startShipping(order_id: int, ssr: ShippingRequest):
    print("The order id is ", order_id)
    order = ordersService.getCartById(order_id)
    if order is None:
        return "Failed to create order"
    userId = order["userId"]
    orderId = str(order["cartId"])
    courier = "cmp7174"
    cartItems = order["cartItem"]
    shipmentItems = []
    for cartItem in cartItems:
        item = Item(
            item_id=cartItem["productId"],
            name=cartItem["name"],
            count=cartItem["quantity"]
        )
        shipmentItems.append(item)
    cpr = CreatePackageRequest(items=shipmentItems)
    package = createPackage(cpr)
    del package["items"]
    package = Package(
        items=shipmentItems,
        **package
    )
    shipment = shippingService.startShipping(orderId, courier,
                                             package, userId,
                                             ssr.source, ssr.destination)
    order["shipment"] = shipment
    return order


@app.get("/TrackOrder/{order_id}")
def trackShipment(order_id: int):
    order = ordersService.getCartById(order_id)
    if order is None:
        return "Failed to findl order"
    shipment = shippingService.trackShipment(str(order["cartId"]))
    order["shipment"] = shipment
    return order


@app.get("/DeliverOrder/{order_id}")
def delivereShipment(order_id: int):
    order = ordersService.getCartById(order_id)
    if order is None:
        return "Failed to findl order"
    shipment = shippingService.deliverShipment(str(order["cartId"]), "none",
                                               "none", "none")
    order["shipment"] = shipment
    return order


@app.get("/GetAllCouriers")
def getAllCouriers():
    return shippingService.getAllCouriers()


@app.get("/GetOrderInformation/{order_id}")
def getShipmentInformation(order_id: str):
    order = ordersService.getCartById(order_id)
    if order is None:
        return "Failed to findl order"
    shipment = shippingService.getShipmentInformation(str(order["cartId"]))
    order["shipment"] = shipment
    return order


@app.get("/GetAllShipments")
def getAllShipmentInformation(user_id: str = None):
    courier = "cmp7174"
    orders = ordersService.getCartRequest("", user_id)
    for order in orders:
        order["shipment"] = shippingService.getAllShipmentInformation(
                                        str(order["cartId"]), courier)
    return orders


@app.get("/CheckService/{service_name}")
def checkService():
    return "handle checking if a particular servcie is active"


@app.get("/GetCartRequest/{user_id}/{status}")
def getCartRequest(user_id: str, status: str):
    return ordersService.getCartRequest(user_id, status)


@app.post("/PostCartStatusRequest/{status}")
def postCartStatusRequest(status: str):
    return ordersService.postCartRequest(status)


def serveHTTP():
    print("Starting HTTP Server")
    port = 5001
    host = "0.0.0.0"
    print("HTTP Server started, listening on ", port)
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    serveHTTP()
