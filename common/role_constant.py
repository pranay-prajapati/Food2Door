"admin, delivery_agent, customer, restaurant"


class Permissions:
    ADD_USER = "Add User"
    DELETE_USER = "Delete User"
    ADD_RESTAURANT = "Add Restaurant"
    DELETE_RESTAURANT = "Delete Restaurant"
    APPROVE_RESTAURANT = "Approve Restaurant"
    ADD_DELIVERY_AGENT = "Add Delivery Agent"
    CREATE_ORDER = "Create Order"
    APPROVE_ORDER = "Approve Order"
    ACCEPT_ORDER = "Accept Order"
    CANCEL_ORDER = "Cancel Order"
    MAKE_PAYMENT = "Make Payment"
    TRACK_ORDER = "Track Order"
    RATE_ORDER = "Rate Order"


class Roles:
    ADMIN_PERMISSION = [
        Permissions.ADD_USER,
        Permissions.ADD_RESTAURANT,
        Permissions.ADD_DELIVERY_AGENT,
        Permissions.DELETE_USER,
        Permissions.APPROVE_RESTAURANT,
        Permissions.DELETE_RESTAURANT,
        Permissions.TRACK_ORDER,
        Permissions.MAKE_PAYMENT
    ]

    RESTAURANT_PERMISSION = [
        Permissions.APPROVE_ORDER,
        Permissions.TRACK_ORDER,
        Permissions.CANCEL_ORDER
    ]

    USER_PERMISSION = [
        Permissions.CREATE_ORDER,
        Permissions.MAKE_PAYMENT,
        Permissions.CANCEL_ORDER,
        Permissions.TRACK_ORDER,
        Permissions.RATE_ORDER
    ]

    DELIVERY_AGENT_PERMISSION = [
        Permissions.ACCEPT_ORDER,
        Permissions.CANCEL_ORDER
    ]


