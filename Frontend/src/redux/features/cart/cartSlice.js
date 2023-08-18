import { createSlice } from "@reduxjs/toolkit";

export const cartSlice = createSlice({
  name: "cart",
  initialState: {
    cartItems: [],
  },
  reducers: {
    addProduct: (state, action) => {
      let cartItemsLength = state.cartItems.length;
      let foundItem;
      for (let i = 0; i < cartItemsLength; i++) {
        if (state.cartItems[i].productId === action.payload.product.id) {
          state.cartItems[i].quantity = action.payload.quantity;
          state.cartItems[i].amount =
            action.payload.quantity * +action.payload.product.price;
          foundItem = state.cartItems[i];
          break;
        }
      }
      if (!foundItem) {
        state.cartItems.push({
          productId: action.payload.product.id,
          name: action.payload.product.title,
          quantity: action.payload.quantity,
          amount: action.payload.quantity * +action.payload.product.price,
        });
      }
      return state;
    },
    removeProduct: (state, action) => {
      return state.cartItems.filter(
        (item) => item.productId !== action.payload.product.id
      );
    },
    emptyCart: (state, action) => {
      return (state.cartItems = []);
    },
  },
});

export const { addProduct, removeProduct, emptyCart } = cartSlice.actions;

export default cartSlice.reducer;
