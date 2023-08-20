const express = require("express");
const Transaction = require("../models/transaction");
require("dotenv").config();
const stripe = require('stripe')(process.env.STRIPE_SK);


exports.postPayment = async (req, res, next) => {
  try {
    const { userId, orderId, amount, paymentMethod } = req.body;

    // Create a PaymentIntent with the order amount and currency
    const paymentIntent = await stripe.paymentIntents.create({
      amount,
      currency: "gbp",
      payment_method_types: ['card'],

    });
    // Creating an invoice

    const newTransaction = new Transaction({
      userId,
      orderId,
      amount,
    });

    await newTransaction.save();

    res.send({
      clientSecret: paymentIntent.client_secret,
    });

  } catch (err) {
    if (!err.statusCode) {
      err.statusCode = 500;
    }
    next(err);
  }
};

