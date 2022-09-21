import enum

from sqlalchemy import Column, TIMESTAMP, func, text


class DatetimeMixin(object):
    """
    common mixin class for datetime
    """
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    )


class VehicleType(enum.Enum):
    """
    Vehicle Type
    """
    without_gear = "Without Gear"
    with_gear = "With Gear"


class PartTime(enum.Enum):
    morning = "Morning"
    evening = "Evening"


class JobType(enum.Enum):
    """
    Job Type
    """
    part_time = PartTime
    full_time = "Full-Time"


class EstablishmentType(enum.Enum):
    both = "Both"
    dine_in = "Dine-in"
    delivery = "Delivery"


class OutletType(enum.Enum):
    bakery = "Bakery"
    bar = "Bar"
    beverage_shop = "Beverage Shop"
    bhojnalaya = "Bhojnalaya"
    cafe = "Cafe"
    casual_dining = "Casual Dining"
    club = "Club"
    dessert_parlour = "Dessert Parlour"
    dhaba = "Dhaba"
    food_court = "Food Court"
    food_truck = "Food Truck"
    pub = "Pub"
    paan_shop = "Paan Shop"
    quick_bytes = "Quick Bytes"
    sweet_shop = "Sweet Shop"


class CuisineType(enum.Enum):
    afgan = "Afgan"


class OrderStatus(enum.Enum):
    placed = "Placed"
    baking = "Baking"
    picked = "Picked"
    on_the_way = "On the way"
    delivered = "Delivered"


class PaymentMode(enum.Enum):
    bhim_upi = "Bhim UPI"
    credit_card = "Credit Card"
    debit_card = "Debit Card"
    paytm_wallet = "Paytm Wallet"



