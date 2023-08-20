# Software oriented architecture E-Commerce mircoservice project implementation
This is the implementation of the group project for software oriented architecture

### Installation Guide
1) Install docker and docker compose following the guide on the official website
   https://docs.docker.com/compose/install/
2) Once docker compose is installed simply run the command `docker-compose up` in the current directory. This will pull all the relevant images from docker hub and startup all the containers
3) Once containers have all been started (You can check this on the container dashbaord of the docker app) you can go to http;//localhost:3000 to view the frontend application
4) On the frontend appliction go to login page and register a user
5) Login with that user
6) Add products to cart
7) Checkout using and pay email: anyemail@gmail.com, card: 4242 4242 4242 4242, cvv: 678, expire date: 02/30, postal code: any
8) To view orders: login first, click the order tab  in the navigation bar
9) To track the order: navigate to order page and enter the order id and click "track"

The other services are also all serviced individually and can be found on the following ports 
- Frontend = http;//localhost:3000 (WebApp)
- Shipping = http;//localhost:50051 (GRPC)
- Orders = http;//localhost:8080 (SOAP)
- Product = http;//localhost:5150 (REST)
- Payment = http;//localhost:8070 (REST)
- Authentication = http;//localhost:6001(REST)
- Orchestrator = http;//localhost:5001 (REST)

Once done testing, you can shutdown all the containers from the docker desktop app by deleting the orchestration container.

Thank you.