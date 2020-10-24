product = []
i = 0

while True:
	name = input('請輸入商品名稱：' )
	if name == 'q':
		break
	price = input('請輸入商品價格：' )
	price = int(price)
	i = i + price
	n_p = []
	n_p.append(name)
	n_p.append(price)
	product.append(n_p)
	print('成功加入商品！！！') 
print('你總共買了', product)
print('總共是', i, '元')

