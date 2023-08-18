# FROM node:18-alpine as builder
# WORKDIR /app
# COPY package.json .
# COPY package-lock.json .
# RUN npm install .
# COPY . .
# RUN npm run build

# FROM nginx 
# WORKDIR /usr/share/nginx/html
# RUN rm -rf ./*
# COPY --from=builder /app/build .
# ENTRYPOINT ["nginx", "-g","daemon off; "]

# Use an official Node.js runtime as the base image
FROM node:14-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install app dependencies
RUN npm install

# Copy app source code
COPY . .

# Build the React app
RUN npm run build

# Install a simple web server to serve the app
RUN npm install -g serve

# Expose the port the app will run on
EXPOSE 3000

# Define the command to start the app
CMD ["serve", "-s", "build"]