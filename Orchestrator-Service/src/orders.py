from zeep import Client


def convert_zeep_item_to_dict(item):
    dict_item = {
        "productId": item["productId"],
        "name": item["name"],
        "quantity": item["quantity"],
        "amount": item["amount"]
    }
    return dict_item


def convert_zeep_cart_to_dict(cart):
    dict_cart = {
        "cartId":  cart["cartId"],
        "userId": cart["userId"],
        "status": cart["status"],
        "cartItem": [convert_zeep_item_to_dict(item)
                     for item in cart["cartItem"]]
    }
    return dict_cart


class OrdersService():
    def __init__(self):
        self.client = Client('carts.wsdl')

    def postCartRequest(self, cartData):
        response = self.client.service.postCart(CartSubmissionRequest=cartData)
        print("The type of the response data is : ",
              type(response["CartSubmissionRequest"]))
        cartData = convert_zeep_cart_to_dict(response["CartSubmissionRequest"])
        return cartData

    def getCartRequest(self, status, user_id):
        response = self.client.service.getCartByUser(status=status,
                                                     user_id=user_id)
        cartDatas = [convert_zeep_cart_to_dict(data) for data in response]
        return cartDatas

    def postCartStatusRequest(self, status):
        response = self.client.service.getCartByStatus(status=status)
        cartDatas = [convert_zeep_cart_to_dict(data) for data in response]
        return cartDatas

    def getCartById(self, cartId):
        orders = self.postCartStatusRequest("Pending")
        print("The orders are : ", orders)
        for order in orders:
            if order["cartId"] == cartId:
                return order
        return None
