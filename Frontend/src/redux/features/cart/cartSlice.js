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
        if (state.cartItems[i].itemId === action.payload.product.product) {
          state.cartItems[i].quantity = action.payload.quantity;
          foundItem = state.cartItems[i];
          break;
        }
      }
      if (!foundItem) {
        state.cartItems.push({
          itemId: action.payload.product.id,
          name: action.payload.product.title,
          quantity: action.payload.quantity,
          amount: action.payload.quantity * +action.payload.product.price,
        });
      }
      return state;
    },
    removeProduct: (state, action) => {
      return state.cartItems.filter(
        (item) => item.itemid !== action.payload.product.id
      );
    },
    emptyCart: (state, action) => {
      return (state.cartItems = []);
    },
  },
});

export const { addProduct, removeProduct, emptyCart } = cartSlice.actions;

export default cartSlice.reducer;
