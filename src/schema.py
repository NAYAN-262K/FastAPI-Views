from pydantic import BaseModel,Field
from typing import Optional
from datetime import datetime

# class OrderBase(BaseModel):
#     quantity: int=Field(alias="quantity",default=None)
#     order_status: str=Field(alias="order_status",default=None)
#     pizza_size: str=Field(alias="pizza_size",default=None)

#     class Config:
#         orm_mode = True
#         allow_population_by_field_name = True


# class ProcessedOrderSchema(BaseModel):
#     id: int =Field(alias="id",default=None)
#     quantity: int=Field(alias="quantity",default=None)
#     order_status: str=Field(alias="order_status",default=None)
#     pizza_size: str=Field(alias="pizza_size",default=None)

#     class Config:
#         orm_mode = True
#         allow_population_by_field_name = True

class VWDemandSchema(BaseModel):
    nzip:str = Field(alias="nzip",default=None)
    enrollment : int = Field(alias="enrollment",default=None)
    number_of_studies : int = Field(alias="number_of_studies",default=None)
    patients_demand : int = Field(alias="patients_demand",default=None)

    class Config:
        orm_mode = True
        allow_population_by_field_name = True



class StudyPydantic(BaseModel):
    nct_id: str = Field(alias="nct_id")
    start_date: Optional[datetime] = Field(alias="start_date")
    completion_date: Optional[datetime] = Field(alias="completion_date")
    study_type: Optional[str] = Field(alias="study_type")
    overall_status: Optional[str] = Field(alias="overall_status")
    phase: Optional[str] = Field(alias="phase")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


