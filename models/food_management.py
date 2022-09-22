from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    Float
)
from sqlalchemy.sql import expression
from database.db_models import handler


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
    ingredients = Column(String(200), nullable=False)

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
