import { createSlice } from "@reduxjs/toolkit";

export const userSlice = createSlice({
  name: "user",
  initialState: {
    address: "",
    email: "",
    mobileNumber: "",
    userID: 0,
    userName: "",
    userType: "",
  },
  reducers: {
    login: (state, action) => {
      return (state = action.payload);
    },
    logout: (state, action) => {
      return (state = {
        address: "",
        email: "",
        mobileNumber: "",
        userID: 0,
        userName: "",
        userType: "",
      });
    },
  },
});

// Action creators are generated for each case reducer function
export const { login, logout } = userSlice.actions;

export default userSlice.reducer;
