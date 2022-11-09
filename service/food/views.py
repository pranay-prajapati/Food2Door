from datetime import datetime

from flask import jsonify, Flask, request
from email_service.email_config import SimpleMailProvider
from exception.http_exception import HttpException
from common.constant import INVALID_FORM_MESSAGE
from common.session import get_current_user_id
from common import constant
from models.common_models import OrderStatus
from models.food_management import DeliveryAgentReview,RestaurantReview
from service.food.query import FoodRepo
from service.user.query.user_query import UserRepo
import email_service.utility.utils

app = Flask(__name__)
app.config["WTF_CSRF_ENABLED"] = False


class FoodData:

    @staticmethod
    def add_menu(request_data):
        restaurant_data = list()
        user_id = get_current_user_id()

        for i in range(len(request_data["data"])):
            menu_data = {
                'restaurant_id_fk': FoodRepo.get_restaurant_data(user_id).restaurant_id,
                'dish_name': request_data.get("data")[i].get("dish_name"),
                'price': request_data.get("data")[i].get("price"),
                "food_quantity": request_data.get("data")[i].get("food_quantity"),
                'ingredients': request_data.get("data")[i].get("ingredients"),
                'is_customisable': request_data.get("data")[i].get("is_customisable")
            }
            restaurant_data.append(menu_data)
        FoodRepo.add_menu(restaurant_data)

        return jsonify({
            'data': restaurant_data,
            'message': 'dishes added successfully'
        })

    @staticmethod
    def show_restaurant():
        user_data = UserRepo.get_user_details(user_id=get_current_user_id())
        data = FoodRepo.show_restaurant(user_data.city)
        res_list = list()
        for i in range(len(data)):
            restaurant_data = {
                'restaurant_id': data[i].restaurant_id,
                'restaurant_name': data[i].restaurant_name,
                'restaurant_address': data[i].restaurant_address,
                'restaurant_contact': data[i].restaurant_contact,
                'establishment_type': data[i].establishment_type.value,
                'outlet_type': data[i].outlet_type.value
            }
            res_list.append(restaurant_data)

        return jsonify(
            {'message': 'success',
             'data': res_list
             })

    @staticmethod
    def show_menu(restaurant_id):
        data = FoodRepo.show_menu_by_restaurant_id(restaurant_id)
        menu_list = list()
        for i in range(len(data)):
            menu_data = {
                'menu_id': data[i].menu_id,
                'dish_name': data[i].dish_name,
                'price': data[i].price,
                'food_image_path': data[i].food_image_path if data[i].food_image_path else None,
                'food_quantity': data[i].food_quantity if data[i].food_quantity else None,
                'is_customisable': data[i].is_customisable if data[i].is_customisable else False,
                'ingredients': data[i].ingredients

            }
            menu_list.append(menu_data)

        return jsonify(
            {'message': 'success',
             'data': menu_list
             })

    @staticmethod
    def add_cart(restaurant_id, menu_ids, cart_data):

        # menu_list = list()
        order_list = list()
        menu_list = list(menu_ids.split(','))

        user_id = get_current_user_id()
        restaurant_data = FoodRepo.get_restaurant_by_id(restaurant_id)
        if restaurant_data.is_closed:
            print('closed')
            raise HttpException('Restaurant is closed')
        # user_data = UserRepo.get_user_details(user_id=user_id)
        #

        for i in range(len(menu_list)):
            menu = FoodRepo.get_menu_details_by_id(menu_list[i])
            order_data = {
                'user_id_fk': user_id,
                'restaurant_id_fk': restaurant_data.restaurant_id,
                'menu_id_fk': menu[0].menu_id,
                'dish_name': menu[0].dish_name,
                'price': menu[0].price,
                'ingredients': menu[0].ingredients,
                'food_quantity': cart_data.get('data')[i].get('food_quantity'),
                'is_ordered': cart_data.get('data')[i].get('is_ordered')
            }
            # if
            order_list.append(order_data)
        # addition to cart table
        FoodRepo.add_cart(order_list)
        # if cart_data.get('is_ordered'):
        # if cart.is_ordered:
        #     FoodData.order_assignment(order_list, restaurant_data)
        # order_data = {key: order_data[key] for key in order_data if key not in ['restaurant_id']}
        # order_list.append(order_data)

        # FoodRepo.add_cart(order_list)
        # data = FoodRepo.add_cart(restaurant_id, menu_id)
        # data =

        return jsonify({
            'message': 'order successfully' if cart_data.get('is_ordered') else 'complete your order request',
            'order_data': order_list,
        })

    @staticmethod
    def agent_order_assignment(restaurant_id, cart_id, menu_id=None):

        order_list = list()
        agent_list = list()
        # menu_list = list(menu_id.split(','))
        cart_list = list(cart_id.split(','))
        user_id = get_current_user_id()
        user_details = UserRepo.get_user_details(user_id=user_id)
        customer_data = {
            'customer_address': user_details.address,
            'customer_name': user_details.name,
            'customer_number': user_details.contact_number
        }
        restaurant_data = FoodRepo.get_restaurant_by_id(restaurant_id)
        restaurant_city = restaurant_data.restaurant_city
        restaurant_details = {
            'restaurant_name': restaurant_data.restaurant_name,
            'restaurant_address': restaurant_data.restaurant_address,
            'restaurant_contact': restaurant_data.restaurant_contact
        }
        for i in range(len(cart_list)):
            # update_cart_details = FoodRepo.update_cart_details(cart_list[i])
            # if update_cart_details:
            cart = FoodRepo.get_cart_details(cart_list[i])
            order_data = {
                'user_id_fk': user_id,
                'dish_name': cart.dish_name,
                'price': cart.price,
                'ingredients': cart.ingredients
            }
            order_list.append(order_data)
            # else:
            #     raise HttpException("something went wrong")
        available_agent_data = UserRepo.get_available_delivery_agent_by_location(restaurant_city)

        for i in range(len(available_agent_data)):
            user_id = available_agent_data[i].user_id_fk
            agent_details = UserRepo.get_user_details(user_id=user_id)
            agent_data = {
                'agent_id': available_agent_data[i].agent_id,
                'agent_name': agent_details.name,
                'agent_email': agent_details.email,
                'agent_phone': agent_details.contact_number
            }
            agent_list.append(agent_data)

            value_map = {'agent_name': agent_data.get('agent_name'),
                         "restaurant_data": restaurant_details,
                         "customer_data": customer_data,
                         "order_data": order_list}
            # send mail
            SimpleMailProvider.send_mail(
                subject=email_service.utility.utils.SUBJECT_MAP.get('notify_agent'),
                receiver=[agent_details.email],
                filename='notify_delivery_agent', value_map=value_map
            )

        return jsonify({
            "message": "sent successfully"
        })

        # send mail to restaurant

    @staticmethod
    def agent_order_acceptance(restaurant_id, cart_id, menu_id, agent_id, order_id, update):
        order_data_list = list(order_id.split(','))
        order_list = list()
        # agent_list = list()
        menu_list = list(menu_id.split(','))
        cart_list = list(cart_id.split(','))
        user_id = get_current_user_id()
        restaurant_data = FoodRepo.get_restaurant_by_id(restaurant_id)
        agent_user_id = UserRepo.get_agent_details_by_id(agent_id)
        agent_details = UserRepo.get_user_details(user_id=agent_user_id.user_id_fk)

        for i in range(len(menu_list)):
            menu = FoodRepo.get_cart_details(cart_list[i])
            cart_data = {
                'agent_id_fk': agent_id,
                'user_id_fk': user_id,
                # 'dish_name': menu.dish_name,
                'menu_id_fk': menu.menu_id_fk,
                'quantity': menu.food_quantity,
                'price': menu.price,
            }

            order_list.append(cart_data)

        # for i in range(len(order_data_list)):
        #     order = FoodRepo.get_order_details(order_data_list[i])
        #     order_data = {
        #         "order_id": order.order_id,
        #     }
        #     order_data_list.append(order_data)

        value_map = {
            'username': UserRepo.get_user_details(user_id=user_id).name,
            'agent_name': agent_details.name,
            'agent_contact': agent_details.contact_number
        }
        if update.get('update') is None:
            for i in range(len(order_data_list)):
                order = FoodRepo.get_order_details(order_data_list[i])
                order_update = FoodRepo.update_order_details(order_list[i], order.order_id)
            SimpleMailProvider.send_mail(
                subject=email_service.utility.utils.SUBJECT_MAP.get('notify_customer'),
                receiver=[UserRepo.get_user_details(user_id=user_id).email],
                filename='notify_customer', value_map=value_map
            )

        if update.get('update') == OrderStatus.picked.name:
            for i in range(len(order_data_list)):
                order = FoodRepo.get_order_details(order_data_list[i])
                data = {
                    'order_status': OrderStatus.picked.name,
                    'pickup_time': datetime.now(),
                    'is_picked': True,
                }
                order_update = FoodRepo.update_order_details(data, order.order_id)

            # order = FoodRepo.update_order_details(data)
            SimpleMailProvider.send_mail(
                subject=email_service.utility.utils.SUBJECT_MAP.get('picked_notification'),
                receiver=[UserRepo.get_user_details(user_id=user_id).email],
                filename='picked_notification', value_map=value_map
            )
        if update.get('update')  == OrderStatus.delivered.name:
            for i in range(len(order_data_list)):
                order = FoodRepo.get_order_details(order_data_list[i])
                data = {
                    'order_status': OrderStatus.delivered.name,
                    'delivery_time': datetime.now(),
                    'is_delivered': True
                }
                order_update = FoodRepo.update_order_details(data, order.order_id)

            SimpleMailProvider.send_mail(
                subject=email_service.utility.utils.SUBJECT_MAP.get('delivery_notification'),
                receiver=[UserRepo.get_user_details(user_id=user_id).email],
                filename='delivery_notification', value_map=value_map
            )

        return jsonify({
            "message": "sent successfully"
        })

        # agent_data = User

        # for i in range(len(order_data)):
        #     # restaurant_data = FoodRepo.get_restaurant_by_id(order_data[i].get('restaurant_id'))
        #     order_list.append(restaurant_data)
        # add to order table

        # menu_data = FoodRepo.get_menu_details_by_id(order_data.get('menu_id'))
        # acceptance = FoodRepo.order_acceptance(menu_data.menu_id)
        # if acceptance:
        #     print(f"your order accepted by {restaurant_data.restaurant_name}")
        #     preparing = FoodRepo.order_preparing(menu_data.menu_id)
        #     if preparing:
        #         print(f"your food is being prepared by {restaurant_data.restaurant_name}")
        #         agent_data = UserRepo.get_available_delivery_agent_by_location(restaurant_data.restaurant_city)
        #     ##delivery agent code below this
        #
        # else:
        #     print("waiting for acceptance")

    @staticmethod
    def res_order_assignment(restaurant_id, menu_id, cart_id):
        order_list = list()
        menu_list = list(menu_id.split(','))
        cart_list = list(cart_id.split(','))
        user_id = get_current_user_id()
        user_details = UserRepo.get_user_details(user_id=user_id)

        customer_data = {
            'customer_address': user_details.address,
            'customer_name': user_details.name,
            'customer_number': user_details.contact_number
        }

        # menu_data = FoodRepo.get_menu_details_by_id(menu_id)

        for i in range(len(cart_list)):
            update_cart_details = FoodRepo.update_cart_details(cart_list[i])
            if update_cart_details:
                menu = FoodRepo.get_cart_details(cart_list[i])
                order_data = {
                    'user_id_fk': user_id,
                    'dish_name': menu.dish_name,
                    'price': menu.price,
                    'quantity': menu.food_quantity,
                    'ingredients': menu.ingredients
                }
                order_list.append(order_data)
                FoodRepo.order_acceptance(menu_id)
            else:
                raise HttpException(message="Something went wrong")
        FoodRepo.add_order_details(order_list)
        # FoodRepo.order_acceptance(menu_id)
        restaurant_data = FoodRepo.get_restaurant_by_id(restaurant_id)
        value_map = {
            'restaurant_name': restaurant_data.restaurant_name,
            "customer_name": customer_data["customer_name"],
            'customer_data': customer_data,
            'order_data': order_list
        }
        SimpleMailProvider.send_mail(
            subject=email_service.utility.utils.SUBJECT_MAP.get('notify_restaurant_team'),
            receiver=restaurant_data.restaurant_email,
            filename='notify_restaurant', value_map=value_map
        )

        return jsonify({
            "message": "sent successfully"
        })

    @staticmethod
    def agent_rating(restaurant_id, menu_id, agent_id, order_id,data):
        if not data:
            raise HttpException(constant.BAD_REQUEST)
        restaurant_data = FoodRepo.get_restaurant_by_id(restaurant_id)
        menu_data = FoodRepo.get_menu_details_by_id(menu_id)
        agent_data = UserRepo.get_agent_details_by_id(agent_id)
        agent_name = UserRepo.get_user_details(user_id = agent_data.user_id_fk).name
        user_id = get_current_user_id()
        user_data = UserRepo.get_user_details(user_id= user_id)
        order_data = FoodRepo.get_order_details(order_id)

        data = {
            'user_id': get_current_user_id(),
            'customer_name': user_data.name,
            'agent_id': agent_data.agent_id,
            'agent_name': agent_name,
            'rating' : data.get('rating'),
            'review': data.get('review'),
            'dish_name': menu_data[0].dish_name,
            'restaurant_name': restaurant_data.restaurant_name
        }

        DeliveryAgentReview(**data).save()

        return jsonify(
            {
                "message":"Review added successfully",
                "data": data

            }
        )
