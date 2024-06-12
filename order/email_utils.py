from book.tasks import send_email_task


def send_order_placed_email(user, order_details):
    subject = 'Order related email'
    message = f'''
        Thankyou for placing your order with us
        Here are your order details:
            created at : {order_details['created_at']}
            total_amount: {float(order_details['total_amount'])}
            order items: {order_details['order_items']}
    '''
    from_email = 'support@BookStore.com'
    user_email_id = str(user.email)
    print(user_email_id)
    recipient_list = [user_email_id, ]

    send_email_task.delay(subject, message, from_email, recipient_list)


def send_order_cancelled_email(user, order_details):
    subject = 'Order Cancellation Email'
    message = f'''
        Your order #{order_details['id']} is successfully cancelled
        Amount Rs {order_details['total_amount']} will be refunded back in your account in 2 to 3 
        business days.
    '''
    from_email = 'support@BookStore.com'
    user_email_id = str(user.email)
    recipient_list = [user_email_id, ]

    send_email_task.delay(subject, message, from_email, recipient_list)


def send_order_out_for_delivery_email(order):
    subject = 'Order Status'
    message = f'''
        Your order labelled {order.id} is Out for delivery
    '''

    from_email = 'support@BookStore.com'
    user_email_id = str(order.user.email)
    recipient_list = [user_email_id, ]
    send_email_task.delay(subject, message, from_email, recipient_list)