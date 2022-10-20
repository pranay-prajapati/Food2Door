TEMPLATE_MAP = {
    'test_email': 'test_email.html',
    'welcome_email': 'welcome_user.html',
    'mfa_code_email': 'mfa_code.html',
    'notify_delivery_agent': 'notify_delivery_agent.html',
    'notify_restaurant': 'notify_restaurant.html'
}

SUBJECT_MAP = {
    'test_email': 'Test Email Notification',
    'welcome_email': 'Welcome to FooD2Door',
    'mfa_code': 'Your Code has been sent successfully ',
    'notify_agent': 'Request for Order Delivery',
    'notify_restaurant_team': 'Request for Order'
}


def get_subject_by_type(email_type: str):
    if email_type not in SUBJECT_MAP:
        print(f'Invalid email type is found : {email_type}')
    subject = SUBJECT_MAP.get(email_type)
    return subject


def get_template_path(request_type: str):
    if request_type not in TEMPLATE_MAP:
        print(f'No Templated is found for type : {request_type}')
    template_path = TEMPLATE_MAP.get(request_type)
    return template_path
