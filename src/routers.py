from fastapi import APIRouter,Query
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends
from sqlalchemy import select,desc
from src.database import get_db
from src.models import VWdemand,Study
from src.schema import VWDemandSchema,StudyPydantic
from src.functions import as_dict

router = APIRouter()

@router.get("/post")
async def read_root():
    return {"detail":"Hello World"}

# @router.get("/orders", response_model=list[OrderBase])
# def get_orders(db: Session = Depends(get_db)):
#     orders = db.query(Order).all()
#     return orders

# @router.get("/processed_orders", response_model=list[ProcessedOrderSchema])
# def get_processed_orders(db:Session= Depends(get_db)):
 
#     try:
#         processed_orders=db.query(ProcessedOrder).all()
#         return processed_orders
#     finally:
#         db.close()

@router.get("/processed_demands", response_model=List[VWDemandSchema])
async def get_processed_orders(
    db:Session= Depends(get_db)):
 
    try:
        processed_orders = db.query(VWdemand).order_by(VWdemand.patients_demand.desc(), VWdemand.nzip.desc()).limit(20).all()
        processed_orders_dicts = [order.as_dict() for order in processed_orders]
        return processed_orders_dicts
    finally:
        db.close()

@router.get("/processed_studies",response_model=List[StudyPydantic])
async def get_processed_studies(
    db:Session = Depends(get_db)):

    try:
        processed_orders = db.query(Study).order_by(Study.nct_id.desc()).limit(10).all()
        processed_orders_dicts = [order.as_dict() for order in processed_orders]
        return processed_orders_dicts
    finally:
        db.close()



