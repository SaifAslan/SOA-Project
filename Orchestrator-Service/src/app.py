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


@app.post("/CalcualateShippingCost")
def calculateShippingCost():
    return shippingService.calculateShippingCost()


@app.post("/CalculateShippingCostNoCourier")
def calculateShippingCostNoCourier():
    return shippingService.calculateShippingCostNoCourier()


@app.post("/CreatePackage")
def createPackage():
    return shippingService.createPackage()


@app.post("/StartShipping")
def startShipping():
    return shippingService.startShipping()


@app.post("/TrakcShipment")
def trackShipment():
    return shippingService.trackShipment()


@app.get("/TrackShipment")
def delivereShipment():
    return shippingService.deliverShipment()


@app.put("/UpdateShipmentStatus")
def updateShipmentStatus():
    return shippingService.updateShipmentStatus()


@app.get("/GetAllCouriers")
def getAllCouriers():
    return shippingService.getAllCouriers()


@app.get("/GetShipmentInformation")
def getShipmentInformation():
    return shippingService.getShipmentInformation()


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
def postCartRequest():
    return ordersService.postCartRequest()


@app.get("/GetCartRequest/{id}")
def getCartRequest():
    return ordersService.getCartRequest()


@app.post("/PostCartStatusRequest")
def postCartStatusRequest():
    return ordersService.postCartRequest()


def serveHTTP():
    print("Starting HTTP Server")
    port = 8000
    host = "0.0.0.0"
    print("HTTP Server started, listening on ", port)
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    serveHTTP()
