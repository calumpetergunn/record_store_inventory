class Product:
    def __init__(self, title, artist, record_label, format, genre, quantity, buy_cost, sell_price, id = None):
        self.title = title
        self.artist = artist
        self.record_label = record_label
        self.format = format
        self.genre = genre
        self.quantity = quantity
        self.buy_cost = buy_cost
        self.sell_price = sell_price
        self.id = id

    def add_stock(self, amount):
        self.quantity += amount

    def reduce_stock(self, amount):
        self.quantity -= amount

    def calculate_margin(self):
        margin = self.sell_price - self.buy_cost
        return round(margin, 2)

    def calculate_total_margin(self):
        total_margin = (self.sell_price - self.buy_cost) * self.quantity
        return round(total_margin, 2)


