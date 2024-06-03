def calculate_price(book_quantity):
    total_price = 0
    for entry in book_quantity:
        book = entry.book
        book_price = book.price
        quantity = entry.quantity
        entry_price = book_price * quantity
        total_price += entry_price

    return total_price
