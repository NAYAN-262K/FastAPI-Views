# models.py

from sqlalchemy import Column, Integer, String,DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# class Order(Base):
#     __tablename__ = 'orders'

#     id = Column(Integer, primary_key=True, index=True)
#     quantity = Column(Integer)
#     order_status = Column(String)
#     pizza_size = Column(String)

# def __repr__(self):
#         return 'OrderModel(id=%s)' % self.id

# class ProcessedOrder(Base):
#     __tablename__ = "processed_orders_view"
#     id = Column(Integer, primary_key=True, index=True)
#     quantity = Column(Integer)
#     order_status = Column(String)
#     pizza_size = Column(String)

# def __repr__(self):
#      return 'ProcessedOrderView(id=%s)' %self.id

class VWdemand(Base):
    __tablename__ = "vw_demand"

    nzip = Column(String, primary_key=True)
    enrollment = Column(Integer)
    number_of_studies = Column(Integer)
    patients_demand = Column(Integer)


    def as_dict(self):
        return {
            "nzip": self.nzip,
            "enrollment": self.enrollment,
            "number_of_studies": self.number_of_studies,
            "patients_demand": self.patients_demand,
        }
    
def __repr__(self):
     return 'VWdemand(id=%s)' %self.id


class Study(Base):
    __tablename__ = 'studies'
    __table_args__ = ({'schema': 'ctgov'},)

    nct_id = Column(String, primary_key=True)
    start_date = Column(DateTime)
    completion_date = Column(DateTime)
    study_type = Column(String)
    overall_status = Column(String)
    phase = Column(String)
    
    def as_dict(self):
        return {
            "nct_id": self.nct_id,
            "start_date": self.start_date,
            "completion_date": self.completion_date,
            "study_type": self.study_type,
            "overall_status":self.overall_status,
            "phase":self.phase
        }
    
def __repr__(self):
     return 'Study(id=%s)' %self.nct_id
     