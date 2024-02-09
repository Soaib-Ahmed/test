class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            total += item['price'] * item['quantity']
        print('Total price:', total)
        if amount < total:
            print(f'Please provide {total - amount} more')
        else:
            extra = amount - total
            print(f'Here is your extra {extra}')

    def remove_item(self, item):
        updated_cart = []
        found = False

        for item in self.cart:
            if item['item'] == item:
                found = True
            else:
                updated_cart.append(item)

        if found:
            self.cart = updated_cart
            print(f'Removed {item} from the cart')
        else:
            print(f'{item} not found in the cart')

seaum = Shopping('Seaum Ahmed')
seaum.add_to_cart('Alu', 40, 6)
seaum.add_to_cart('Banana', 10, 4)
seaum.add_to_cart('Lau', 80, 2)


seaum.checkout(100)
seaum.remove_item('kola')
print(seaum.cart)
