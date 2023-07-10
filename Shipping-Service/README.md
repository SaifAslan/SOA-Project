# Implementation of the shipping service in python
This sub project focuses on the implementation of the shipping service in python. The service makes use of two communication protocols. REST via HTTP and and GRPC with ProtocolBuffers. 

To start the application run the following commands:
- Install and start mongodb server ``
- Create Grpc Stups ` python -m grpc_tools.protoc -I . --python_out=. --pyi_out=. --grpc_python_out=. shipping.proto`
