# Some shops

class Store:

    def __init__(self, name: str, address: str) -> None:
        self.name = name
        self.address = address
        self.goods = {}
        print(f'Назание магазина: {name}\nАдрес магазина: {address}\n')

    def add_item(self, item_name: str, item_price: str) -> None:
        self.goods[item_name] = float(item_price)
        print(f'Добавлен товар: {item_name}, цена {item_price}')

    def del_item(self, item_name: str) -> None:
        if item_name in self.goods:
            del self.goods[item_name]
            print(f'Товар {item_name} удален')

    def get_price(self, item_name) -> None:
        item_price = self.goods.get(item_name, None)

        if item_price:
            print(f'{item_name} стоят {item_price}')
        else:
            print(f'Товара {item_name} нет в магазине')

    def get_item_list(self) -> str:
        merch = ''
        number = 0
        for name, price in self.goods.items():
            number += 1
            merch += f'{number}. название: {name}, цена: {price}\n'

        return merch

    def update_price(self, item_name: str, new_price: str) -> None:
        if item_name in self.goods:
            print(f'В настоящее время {item_name}, стоит {self.goods[item_name]}')
            self.goods[item_name] = float(new_price)
            print(f'Цена товара была изменена теперь: {item_name}, стоит {new_price}\n')


print('Добавляю Магазины:')
shop_1 = Store(name='Пятерочка', address='ул. Окружная, 1Д')
shop_2 = Store(name='АМК|Автосеть', address='ул. Селькоровская, 78Б')
shop_3 = Store(name='Магнит', address='Вторая новосибирская, 12 (помещение 1, 2)')

print('Добавляю в Магнит 3 товара:')
shop_3.add_item('Яблоки', '65.35')
shop_3.add_item('Дыни', '92.50')
shop_3.add_item('Бананы', '35.40')

print('\nСписок товаров:')
print(shop_3.get_item_list())

print('Обновляю цену товара:')
shop_3.update_price('Дыни', '120.33')

print('Список товаров:')
print(shop_3.get_item_list())

print('Получаю цену товаров:')
shop_3.get_price('Яблоки')
shop_3.get_price('Валенки')

print('\nУдаляю товар:')
shop_3.del_item('Бананы')

print('\nСписок товаров:')
print(shop_3.get_item_list())