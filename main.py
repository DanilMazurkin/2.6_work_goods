from helpers import goods_max_min_price


def run_program():
    with open('./list_goods.txt', 'r', encoding='utf-8') as file:
        list_goods = file.readlines()
        good_list = goods_max_min_price(list_goods, True)
        print(good_list)


if __name__ == '__main__':
    run_program()
