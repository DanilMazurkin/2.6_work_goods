with open('./list_goods.txt', 'r', encoding='utf-8') as file:
    list_goods = file.readlines()


def goods_max_min_price(list_of_goods, is_max):
    """Возвращает товары в зависимости от is_max
    list_of_goods (list): Список с товарами
    is_max (bool): Параметр какие товары возвращать
    :return list_of_goods_by_price (list): Возвращает товары в зависимости от is_max
    """

    list_of_goods_by_price = list()

    max_price = 0
    min_price = 10000

    for good in list_of_goods:
        try:
            price = int(good.split(":")[1])
        except IndexError:
            print("Проблема с файлом!")
            continue

        if price > max_price:
            max_price = price

        if price < min_price:
            min_price = price

    for good in list_of_goods:
        price = int(good.split(":")[1])

        if price == max_price and is_max:
            list_of_goods_by_price.append(good)
        if price == min_price and not is_max:
            list_of_goods_by_price.append(good)

    return list_of_goods_by_price

