from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    Float,
    JSON
)
from sqlalchemy.sql import expression
from database.db_models import handler
import mongoengine as db


class Menu(handler.Base):
    __tablename__ = 'menu'
    menu_id = Column(
        Integer, primary_key=True, unique=True, autoincrement=True
    )
    restaurant_id_fk = Column(Integer, ForeignKey("restaurant.restaurant_id"))
    dish_name = Column(String(200), nullable=False)
    food_image_path = Column(String(1024))
    price = Column(Float, nullable=False)
    food_quantity = Column(String(64))
    is_customisable = Column(Boolean, server_default=expression.false())
    ingredients = Column(JSON)

    def __repr__(self):
        return '<Menu %r>' % self.restaurant_id_fk

    def to_json(self):
        return {
            'restaurant_id_fk': self.restaurant_id_fk,
            'dish_name': self.dish_name,
            'food_image_path': self.food_image_path,
            'price': self.price,
            'food_quantity': self.food_quantity,
            'is_customisable': self.is_customisable,
            'ingredients': self.ingredients
        }


class Cart(handler.Base):
    __tablename__ = 'cart'
    cart_id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    restaurant_id_fk = Column(Integer, ForeignKey("restaurant.restaurant_id"))
    menu_id_fk = Column(Integer, ForeignKey("menu.menu_id"))
    user_id_fk = Column(Integer, ForeignKey("tbl_user.user_id"))
    price = Column(Float, nullable=False)
    dish_name = Column(String(200))
    food_quantity = Column(String(64))
    ingredients = Column(JSON)
    is_ordered = Column(Boolean, server_default=expression.false())

    def __repr__(self):
        return '<Menu %r>' % self.restaurant_id_fk

    def to_json(self):
        return {
            'cart_id': self.cart_id,
            'restaurant_id_fk': self.restaurant_id_fk,
            'menu_id_fk': self.menu_id_fk,
            'user_id_fk': self.user_id_fk,
            'price': self.price,
            'dish_name': self.dish_name,
            'food_quantity': self.food_quantity,
            'ingredients': self.ingredients,
            'is_ordered': self.is_ordered

        }


class RestaurantReview(db.Document):
    """
        MongoDB Data Model
    """
    _id = db.SequenceField(primary_key=True)
    user_id = db.IntField()
    rating = db.IntField()
    review = db.StringField()
    dish_name = db.StringField()
    restaurant_name = db.StringField()
    price = db.FloatField()
    delivered_by = db.StringField()

    def to_json(self):
        return {
            '_id': self._id,
            'user_id': self.user_id,
            'rating': self.rating,
            'review': self.review,
            'dish_name': self.dish_name,
            'restaurant_name': self.restaurant_name,
            'price': self.price,
            'delivered_by': self.delivered_by,
        }


class DeliveryAgentReview(db.Document):
    """
        MongoDB Data Model
    """
    _id = db.SequenceField(primary_key=True)
    user_id = db.IntField()
    customer_name = db.StringField()
    agent_id = db.IntField()
    agent_name = db.StringField()
    rating = db.IntField()
    review = db.StringField()
    order_status = db.StringField()
    dish_name = db.StringField()
    restaurant_name = db.StringField()

    def to_json(self):
        return {
            '_id': self._id,
            'user_id': self.user_id,
            'customer_name': self.customer_name,
            'agent_id': self.agent_id,
            'agent_name': self.agent_name,
            'rating': self.rating,
            'review': self.review,
            'order_status': self.order_status,
            'dish_name': self.dish_name,
            'restaurant_name': self.restaurant_name,
        }
