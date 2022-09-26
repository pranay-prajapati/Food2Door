from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    VARBINARY,
    Enum,
    LargeBinary

)
from sqlalchemy.sql import expression
# from database.db_creator import PostgresHandler
from database.db_models import handler
from models.common_models import DatetimeMixin, VehicleType, JobType, EstablishmentType, OutletType


class User(DatetimeMixin, handler.Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    contact_number = Column(String(10), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    address = Column(String(256))
    city = Column(String(64))
    state = Column(String(64))
    zip_code = Column(String(6))
    password_hash = Column(LargeBinary(64))
    is_owner = Column(Boolean, server_default=expression.false())
    is_delivery_agent = Column(Boolean, server_default=expression.false())

    def __repr__(self):
        return '<User %r>' % self.name

    def to_json(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'contact_number': self.contact_number,
            'email': self.email,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'zip_code': self.zip_code,
            'is_owner': self.is_owner,
            'is_delivery_agent': self.is_delivery_agent
        }


class DeliveryAgent(DatetimeMixin, handler.Base):
    __tablename__ = 'delivery_agent'
    agent_id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    user_id_fk = Column(Integer, ForeignKey("user.user_id"))
    vehicle_type = Column(Enum(VehicleType))
    driving_licence_number = Column(String(16), unique=True, nullable=False)
    aadhar_card_number = Column(String(16), unique=True, nullable=False)
    vehicle_number = Column(String(12), nullable=False)
    job_type = Column(Enum(JobType))

    def __repr__(self):
        return '<DeliveryAgent %r>' % self.user_id_fk

    def to_json(self):
        return {
            'agent_id': self.agent_id,
            'user_id_fk': self.user_id_fk,
            'vehicle_type': self.vehicle_type,
            'driving_licence_number': self.driving_licence_number,
            'aadhar_card_number': self.aadhar_card_number,
            'vehicle_number': self.vehicle_number,
            'job_type': self.job_type
        }


class Restaurant(DatetimeMixin, handler.Base):
    __tablename__ = 'restaurant'
    restaurant_id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    user_id_fk = Column(Integer, ForeignKey("user.user_id"))
    restaurant_name = Column(String(100), nullable=False)
    restaurant_address = Column(String(50), nullable=False)
    restaurant_contact = Column(String(10), nullable=False)
    fssai_number = Column(String(14), nullable=False)
    gst_number = Column(String(24), nullable=False)
    establishment_type = Column(Enum(EstablishmentType))
    outlet_type = Column(Enum(OutletType))
    is_closed = Column(Boolean, server_default=expression.false())

    # need to be added
    # cuisine_type = Column(Enum(EstablishmentType))
    # operational_hours = Column(Enum(EstablishmentType))

    def __repr__(self):
        return '<Restaurant %r>' % self.restaurant_id

    def to_json(self):
        return {
            'restaurant_id': self.restaurant_id,
            'user_id_fk': self.user_id_fk,
            'restaurant_name': self.restaurant_name,
            'restaurant_address': self.restaurant_address,
            'restaurant_contact': self.restaurant_contact,
            'fssai_number': self.fssai_number,
            'gst_number': self.gst_number,
            'establishment_type': self.establishment_type,
            'outlet_type': self.outlet_type,
        }
