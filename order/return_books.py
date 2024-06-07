# Returns the books back to inventory after order cancellation
from order.models import Order
from order.serializers import OrderSerializer
from store.models import Inventory


def return_books(order_id):
    order = Order.objects.get(id=order_id)
    order_serializer = OrderSerializer(order)
    order_items = order_serializer.data.get("order_items", [])
    for order_item in order_items:
        book = order_item.get('book')
        store = order_item.get('store')
        quantity = order_item.get('quantity')

        inventory = Inventory.objects.get(book=book, store=store)
        inventory.quantity += quantity
        inventory.save()
