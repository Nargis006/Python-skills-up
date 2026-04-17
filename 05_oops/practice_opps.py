class OnlineStore:
    product_Count = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price
        OnlineStore.product_Count += 1
    
    def product_details(self):
        print(f"Product name is {self.name} and price is {self.price}")

    @staticmethod
    def calculate_discount(price, discount):
        return price - (price * discount / 100)
    
    @classmethod
    def total_products(cls):
        print(f"Total products in store: {cls.product_Count}")
    
phone = OnlineStore("iPhone", 1000)
print(phone.calculate_discount(phone.price, 10)) # 900.0

Tablets = OnlineStore("iPad", 800)
print(Tablets.calculate_discount(Tablets.price, 15)) # 680.0

Macbook = OnlineStore("MacBook", 1500)
print(Macbook.calculate_discount(Macbook.price, 20)) # 1200.0

OnlineStore.total_products()  # Output: Total products in store: 3