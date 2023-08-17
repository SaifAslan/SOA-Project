from typing import List
from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from authentication import AuthenticationServicee
from orders import OrdersService
from payments import PaymentService
from products import ProductService
from shipping import ShippingService
from users import UserService

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

authenticationService = AuthenticationServicee()
ordersService = OrdersService()
paymentService = PaymentService()
productService = ProductService()
shippingService = ShippingService()
userService = UserService()


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
    package: Package
    source: Address
    destination: Address


class ShippingRequestWithCourier(ShippingRequest):
    courier: str


class CreatePackageRequest(BaseModel):
    items: List[Item]


class StartShippingRequest(BaseModel):
    order_id: str
    user_id: str
    courier: str
    package: Package
    source: Address
    destination: Address


class CartItem(BaseModel):
    productId: str
    name: str
    quantity: int
    amount: float


class CartDataRequest(BaseModel):
    cartId: str
    cartItem: List[CartItem]


class CartData(CartDataRequest):
    userId: str
    status: str = "Pending"


@app.get("/GetProduct")
def getProduct():
    return productService.getProduct()


@app.put("/UpdateProduct")
def updateProduct():
    return productService.putProduts()


@app.post("/AddProduct")
def addProduct():
    return productService.postProducts()


@app.get("/GetProduct/{id}/")
def getProducts():
    return productService.getProducts()


@app.post("/CalculateShippingCost")
def calculateShippingCost(sr: ShippingRequestWithCourier):
    return shippingService.calculateShippingCost(sr.courier,
                                                 sr.package,
                                                 sr.source,
                                                 sr.destination)


@app.post("/CalculateShippingCostNoCourier")
def calculateShippingCostNoCourier(sr: ShippingRequest):
    return shippingService.calculateShippingCostNoCourier(sr.package,
                                                          sr.source,
                                                          sr.destination)


@app.post("/CreatePackage")
def createPackage(pr: CreatePackageRequest):
    return shippingService.createPackage(pr.items)


@app.post("/StartShipping")
def startShipping(ssr: StartShippingRequest):
    return shippingService.startShipping(ssr.order_id, ssr.courier,
                                         ssr.package, ssr.user_id,
                                         ssr.source, ssr.destination)


@app.get("/TrackShipment/{shipment_id}")
def trackShipment(shipment_id: str):
    return shippingService.trackShipment(shipment_id)


@app.get("/DeliverShipment/{shipment_id}")
def delivereShipment(shipment_id: str):
    return shippingService.deliverShipment(shipment_id, "none", "none", "none")


@app.put("/UpdateShipmentStatus/{shipment_id}")
def updateShipmentStatus(shipment_id: str):
    return shippingService.updateShipmentStatus(shipment_id, "none",
                                                "none", "none")


@app.get("/GetAllCouriers")
def getAllCouriers():
    return shippingService.getAllCouriers()


@app.get("/GetShipmentInformation/{shipment_id}")
def getShipmentInformation(shipment_id: str):
    return shippingService.getShipmentInformation(shipment_id)


@app.get("/GetAllShipments")
def getAllShipmentInformation(user_id: str = None, courier: str = None):
    return shippingService.getAllShipmentInformation(user_id, courier)


@app.get("/InitializePyament")
def initializePayment():
    return paymentService.createPaymentIntent()


@app.post("/AddUser")
def addUser():
    return userService.addUser()


@app.get("/GetUser/{id}")
def getUser():
    return userService.getUser()


@app.post("/AuthenticateUser")
def authenticationUser():
    return authenticationService.authenticateUser()


@app.get("/CheckService/{service_name}")
def checkService():
    return "handle checking if a particular servcie is active"


@app.post("/PostCartRequest")
def postCartRequest(cartData: CartDataRequest):
    cartData = cartData.dict()
    return ordersService.postCartRequest(cartData)


@app.get("/GetCartRequest/{user_id}/{status}")
def getCartRequest(user_id: str, status: str):
    return ordersService.getCartRequest(user_id, status)


@app.post("/PostCartStatusRequest/{status}")
def postCartStatusRequest(status: str):
    return ordersService.postCartRequest(status)


def serveHTTP():
    print("Starting HTTP Server")
    port = 8000
    host = "0.0.0.0"
    print("HTTP Server started, listening on ", port)
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    serveHTTP()
