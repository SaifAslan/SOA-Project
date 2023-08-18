// Step 1: Install dependencies and set up Mongoose
const mongoose = require('mongoose');


// Step 2: Define the Mongoose Schema for transactions
const transactionSchema = new mongoose.Schema({
  userId: {
    type: String, // Assuming you have a User model with an ObjectId as the primary key
    required: true,
  },
  orderId: {
    type: String,
    required: true,
  },
  amount: {
    type: Number,
    required: true,
  },
  paymentMethod: {
    type: String,
    required: true,
    default:'stripe'
  },
  status: {
    type: String,
    enum: ['pending', 'completed', 'failed'],
    default: 'pending',
  },
  createdAt: {
    type: Date,
    default: Date.now,
  },
  updatedAt: {
    type: Date,
    default: Date.now,
  },
  // You can add more fields relevant to your use case, e.g., customer information, payment gateway details, etc.
});

// Step 3: Create the Mongoose Model for transactions
const Transaction = mongoose.model('Transaction', transactionSchema);

// Export the model to be used in other parts of your application
module.exports = Transaction;
