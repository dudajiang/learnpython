# -*- coding:utf-8 -*-


# 储存并返回商品信息
def get_goods_info():
    goods_dict = {
        "001": {"name": "爱马仕腰带", "price": 1999},
        "002": {"name": "劳力士男表", "price": 19999},
        "003": {"name": "巴宝莉眼镜", "price": 4999},
        "004": {"name": "路虎发现四", "price": 99999}
    }
    return goods_dict

# 打印商品信息
def print_goods_info(goods_dict):
    print('-------------------本店提供以下商品--------------------')
    for name, value in goods_dict.items():
      print('(商品编号:{}、商品名称:{}、商品价格:{})'.format(name,value['name'],value.get('price')))


def serial_num_judge(serial_num, goods_dict):
    # 判断编号是否存在
    if serial_num == 'q' or serial_num == 'Q':
        return 'Q'
    while serial_num not in goods_dict.keys():
        print('商品编号不存在，请重新输入！')
        print_goods_info(goods_dict)
        serial_num = input('根据商品信息输入商品编号，退出购物请输入Q：')
        if serial_num == 'q' or serial_num == 'Q':
            return 'Q'
    return serial_num


def amount_judge(amount):
    # 判断输入数量合法性
    while True:
        try:
            amount = eval(amount)
            if amount < 0 or type(amount) != int:
                amount = input('输入有误，请重新输入您要购买的数量：')
            else:
                return amount
        except:
            amount = input('输入有误，请重新输入您要购买的数量：')


def payment_judge(amount_of_payment):
    # 判断付款金额合法性
    while True:
        try:
            amount_of_payment = eval(amount_of_payment)
            if amount_of_payment < 0:
                print('请输入合法金额！')
                amount_of_payment = input('请您付款：')
            else:
                return amount_of_payment
        except:
            print('请输入合法金额！')
            amount_of_payment = input('请您付款：')


def add_goods_to_shopping_cart(serial_num, goods_dict, amount, shopping_cart):
    # 将商品加入购物车中，并返回购物车（字典）
    name = goods_dict[serial_num]['name']
    price = goods_dict[serial_num]['price']
    total_price = amount * price
    if name not in shopping_cart.keys():
        # 如果购物车中没有该商品，则加入该商品及相关信息
        shopping_cart[name] = [price, amount, total_price]
    else:
        # 如果购物车中有该商品，则更新该商品相关信息
        amount = amount + shopping_cart[name][1]
        total_price = total_price + shopping_cart[name][2]
        shopping_cart[name] = [price, amount, total_price]
    return shopping_cart


def check_out(shopping_cart):
    sum_price = 0
    print('--------------欢迎来到订单结算页面---------------')
    print('您当前购物车商品信息为：')

    # 使用for循环打印购物车信息
    for goods in shopping_cart:
        price = shopping_cart[goods][0]
        amount = shopping_cart[goods][1]
        total_price = shopping_cart[goods][2]
        print('商品名称：{}     商品单价:{}      数量：{}      总价：{}'.
              format(goods, price, amount, total_price))
        sum_price += total_price
    print('订单总额为：', sum_price)

    # 结算订单
    amount_of_payment = input('请您付款：')
    amount_of_payment = payment_judge(amount_of_payment)
    while amount_of_payment < sum_price:
        print('付款失败，输入金额小于订单金额')
        amount_of_payment = input('请您付款：')
        amount_of_payment = payment_judge(amount_of_payment)
    print('付款成功，找您{}元'.format(amount_of_payment - sum_price))
    print('--------------本次购物结束，期待您的下次光临--------------')


def main():
    # 获取商品信息
    goods_dict = get_goods_info()
    # 初始化购物车
    shopping_cart = {}
    while True:
        # 打印商品列表
        print_goods_info(goods_dict)

        # 接收用户输入
        serial_num = input('根据商品信息输入商品编号，退出购物请输入Q：')

        # 判断用户输入是否合法，并采取相应操作
        serial_num = serial_num_judge(serial_num, goods_dict)

        if serial_num == 'Q' and len(shopping_cart) == 0:
            # 选择退出时购物车中没有商品，直接结束本次购物
            print('--------------本次购物结束，期待您的下次光临--------------')
            return

        elif serial_num == 'Q' and len(shopping_cart) != 0:
            # 选择退出时购物车中有商品，则进入结账界面，调用结账函数，完成结账
            check_out(shopping_cart)
            return

        else:
            amount = input('请输入您要购买的数量：')
            # 判断用户输入数量是否合法
            amount = amount_judge(amount)

            if amount != 0:
                # 数量不为零，则调用购物车函数，更新购物车信息
                shopping_cart = add_goods_to_shopping_cart(serial_num, goods_dict,amount, shopping_cart)


if __name__ == '__main__':
    main()
