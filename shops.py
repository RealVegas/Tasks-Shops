# Some shops

class Store:

    def __init__(self, name: str, address: str) -> None:
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self) -> None:
        pass

    def del_item(self) -> None:
        pass

    def get_price(self) -> None:
        pass

    def get_item_list(self) -> None:
        pass

    def update_price(self) -> None:
        pass


shop_1 = Store(name='Пятерочка', address='ул. Окружная, 1Д')
shop_2 = Store(name='АЦ "Династия"', address='ул. Республики, 222А')
shop_3 = Store(name='Магнит', address='Вторая новосибирская, 12 (помещение 1, 2)')