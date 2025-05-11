import json

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self, customer_name, address, mobile):
        self.customer_name = customer_name
        self.address = address
        self.mobile = mobile
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total_price(self):
        return sum(item.price for item in self.items)

class Restaurant:
    def __init__(self):
        self.menu = []
        self.orders = []

    def add_menu_item(self, item):
        self.menu.append(item)

    def place_order(self, order):
        self.orders.append(order)
        self.save_orders_to_json()

    def get_sales_report(self):
        return sum(order.total_price() for order in self.orders)

    def save_orders_to_json(self):
        data = []
        for order in self.orders:
            data.append({
                "customer_name": order.customer_name,
                "address": order.address,
                "mobile": order.mobile,
                "items": [{"name": item.name, "price": item.price} for item in order.items],
                "total_price": order.total_price()
            })
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)

    def load_orders_from_json(self):
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
                for o in data:
                    order = Order(o["customer_name"], o["address"], o["mobile"])
                    for item in o["items"]:
                        order.add_item(MenuItem(item["name"], item["price"]))
                    self.orders.append(order)
        except FileNotFoundError:
            pass
