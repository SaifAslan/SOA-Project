from zeep import Client


class OrdersService():
    def __init__(self):
        self.client = Client('carts.wsdl')

    def postCartRequest(self, cartData):
        cartData = cartData.dict()
        response = self.client.service.postCart(CartSubmissionRequest=cartData)
        return response

    def getCartRequest(self, status, user_id):
        response = self.client.service.getCartByUser(status=status,
                                                     user_id=user_id)
        return response

    def postCartStatusRequest(self, status):
        response = self.client.service.getCartByStatus(status=status)
        return response

    def getCartById(self, cartId):
        orders = self.postCartStatusRequest("Pending")
        for order in orders:
            if order["cartId"] == cartId:
                return order
        return None
