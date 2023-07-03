from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from enum import Enum


app = FastAPI(title="cmp7174 shipping",
              description="""**CMP7174 Shipping Service** This service manages the shipping of goods in our
              ecommerce project. The service manages tracking of shipment from various couriers and serves it in a 
              unified GRPC and REST service. The service persists data on a MongoDB database.""",
              version="0.1.3", docs_url="/documentation", redoc_url="/redoc"
              )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
