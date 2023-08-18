from zeep import Client


def postProcessingCartItem(cartItems):
    output = []
    for item in cartItems:
        output.append(item["__values__"])
    return output


class OrdersService():
    def __init__(self):
        self.client = Client('carts.wsdl')

    def postCartRequest(self, cartData):
        res = self.client.service.postCart(CartSubmissionRequest=cartData)
        cartData = res["__values__"]["CartSubmissionRequest"]["__values__"]
        cartData["cartItem"] = postProcessingCartItem(cartData["cartItem"])
        return cartData

    def getCartRequest(self, status, user_id):
        response = self.client.service.getCartByUser(status=status,
                                                     user_id=user_id)
        cartDatas = response["__values__"]["cartData"]["__values__"]
        for cartData in cartDatas:
            cartData["cartItem"] = postProcessingCartItem(cartData["cartItem"])
        return cartDatas

    def postCartStatusRequest(self, status):
        response = self.client.service.getCartByStatus(status=status)
        cartDatas = response["__values__"]["cartData"]["__values__"]
        for cartData in cartDatas:
            cartData["cartItem"] = postProcessingCartItem(cartData["cartItem"])
        return cartDatas

    def getCartById(self, cartId):
        orders = self.postCartStatusRequest("Pending")
        for order in orders:
            if order["cartId"] == cartId:
                return order
        return None
