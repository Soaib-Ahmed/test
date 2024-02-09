class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password


class Customer(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)

    def place_order(self):
        for product in self.cart:
            if product.stock > 0:
                product.stock -= 1
                print(f"Order placed: {product.name}")
            else:
                print(f"Product out of stock: {product.name}")

        self.cart = []


class Seller(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.products = []

    def create_product(self, name, stock):
        product = Product(name, stock)
        self.products.append(product)

    def publish_products(self):
        for product in self.products:
            print(f"Product published: {product.name}")


class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock


# Example usage:
customer = Customer("customer@example.com", "password")
seller = Seller("seller@example.com", "password")

seller.create_product("Product A", 5)
seller.create_product("Product B", 0)
seller.create_product("Product C", 10)

seller.publish_products()

customer.add_to_cart(seller.products[0])  # Adding Product A to the cart
customer.add_to_cart(seller.products[1])  # Adding Product B to the cart
customer.add_to_cart(seller.products[2])  # Adding Product C to the cart

customer.place_order()