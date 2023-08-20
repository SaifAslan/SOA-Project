import { createSlice, current } from "@reduxjs/toolkit";

export const cartSlice = createSlice({
  name: "cart",
  initialState: {
    cartId: 0,
    cartItems: [],
    deliveryCosts: 0,
  },
  reducers: {
    addProduct: (state, action) => {
      let cartItemsLength = state.cartItems.length;
      let foundItem;
      for (let i = 0; i < cartItemsLength; i++) {
        if (state.cartItems[i].productId === action.payload.product.productId) {
          state.cartItems[i].quantity = action.payload.quantity;
          state.cartItems[i].amount =
            action.payload.quantity * +action.payload.product.price;
          foundItem = state.cartItems[i];
          break;
        }
      }
      if (!foundItem) {
        state.cartItems.push({
          productId: action.payload.product.productId,
          name: action.payload.product.productName,
          quantity: action.payload.quantity,
          amount: action.payload.quantity * +action.payload.product.price,
        });
      }
      return state;
    },
    removeProduct: (state, action) => {
      let newState = {
        ...current(state),
        cartItems: current(state).cartItems.filter(
          (item) => item.productId != action.payload
        ),
      };

      return newState;
    },
    emptyCart: (state, action) => {
      state = {
        cartId: 0,
        cartItems: [],
        deliveryCost:0
      };
      return state;
    },
    addCartId: (state, action) => {
      state.cartId = action.payload;
      return state;
    },
    addDeliveryCost: (state, action) => {
      state.deliveryCost = action.payload
      return state;
    }
  },
});

export const { addProduct, removeProduct, emptyCart, addCartId , addDeliveryCost} =
  cartSlice.actions;

export default cartSlice.reducer;
