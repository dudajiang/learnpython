
goods_dict = {
    "001": {"name": "爱马仕腰带", "price": 1999},
    "002": {"name": "劳力士男表", "price": 19999},
    "003": {"name": "巴宝莉眼镜", "price": 4999},
    "004": {"name": "路虎发现四", "price": 99999},
}

print('本店提供以下商品')
for name,value in goods_dict.items():
  print('(商品编号:{}、商品名称:{}、商品价格:{})'.format(name,value['name'],value.get('price')))

cart = []

while True:
  id = input('请输入购买的商品编号(结束按q):')
  if id == 'q':
    print('购买结束')
    break
  else:
    good = goods_dict.get(id,'error')
    if good == 'error':
      print('编号有误，需重新输入')
    else:
      while True:
        num = input('请输入购买的商品数量:')
        if num.isdigit():
          buy = {
            'id':id,
            'num':int(num)
          }
          cart.append(buy)
          break
        else:
          print('需要输入数字')
  
  all = 0
  for x in cart:
    id = x['id']
    num = x['num']
    value = goods_dict[id]['price']
    all += num*value

print('一共支付金额',all)
