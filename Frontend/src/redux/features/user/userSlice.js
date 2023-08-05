import { createSlice } from "@reduxjs/toolkit";

export const userSlice = createSlice({
  name: "user",
  initialState: {
    userId: "",
    firstName: "",
    lastName: "",
    email: "",
    token: "",
  },
  reducers: {
    login: (state, action) => {
      state = action.payload;
    },
    logout: (state, action) => {
      state = this.initialState;
    },
  },
});

// Action creators are generated for each case reducer function
export const { login, logout } = userSlice.actions;

export default userSlice.reducer;
