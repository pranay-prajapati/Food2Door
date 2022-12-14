from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String,
    ForeignKey,
    Enum,
    DateTime, Float
)
from models.common_models import DatetimeMixin, OrderStatus, PaymentMode
from database.db_models import handler
from sqlalchemy.orm import relationship
from sqlalchemy.sql import expression


class Order(DatetimeMixin, handler.Base):
    __tablename__ = 'order'
    order_id = Column(
        Integer, primary_key=True, unique=True, autoincrement=True
    )
    agent_id_fk = Column(Integer, ForeignKey("delivery_agent.agent_id"))
    user_id_fk = Column(Integer, ForeignKey("tbl_user.user_id"))
    menu_id_fk = Column(Integer, ForeignKey("menu.menu_id"))
    order_status = Column(Enum(OrderStatus))
    pickup_time = Column(DateTime)
    delivery_time = Column(DateTime)
    quantity = Column(String(64))
    price = Column(Float, nullable=False)
    # is_ordered = Column(Boolean, server_default=expression.false())
    is_accepted = Column(Boolean, server_default=expression.false())
    is_picked = Column(Boolean, server_default=expression.false())
    is_delivered = Column(Boolean, server_default=expression.false())

    # menu = relationship("Menu")

    def __repr__(self):
        return '<Order %r>' % self.order_id

    def to_json(self):
        return {
            'order_id': self.order_id,
            # 'restaurant_id_fk': self.restaurant_id_fk,
            'agent_id_fk': self.agent_id_fk,
            'user_id_fk': self.user_id_fk,
            'order_status': self.order_status,
            'pickup_time': self.pickup_time,
            'delivery_time': self.delivery_time,
            'quantity': self.quantity
        }


class Payment(DatetimeMixin, handler.Base):
    __tablename__ = 'payment'
    payment_id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    order_id_fk = Column(Integer, ForeignKey("order.order_id"))
    upi_id = Column(String(20), nullable=False)
    credit_card_number = Column(String(16), nullable=False)
    debit_card_number = Column(String(16), nullable=False)
    payment_mode = Column(Enum(PaymentMode))

    # user = relationship("User")

    def __repr__(self):
        return '<Payment %r>' % self.payment_id

    def to_json(self):
        return {
            'payment_id': self.payment_id,
            'order_id_fk': self.order_id_fk,
            'upi_id': self.upi_id,
            'credit_card_number': self.credit_card_number,
            'debit_card_number': self.debit_card_number,
            'payment_mode': self.payment_mode
        }
