
class Good:
    """Represent Good"""

    def __init__(
            self, name, count, price,
            date_production=None, count_day_expiration=None
    ):
        self.name = name
        self.count = count
        self.price = price
        self.date_production = date_production
        self.count_day_expiration = count_day_expiration

    def check_expiration_date(self):
        # Если дата меньше текушей, то просрочен
        # Вернем True False

    def __str__(self):
        return f'Товар цена: {self.price}, имя: {self.name}, количество: {self.count}'