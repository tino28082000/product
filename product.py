#讀取檔案

with open('product.csv', 'r', encoding = 'utf-8') as d:
	for line in d:
		name, price = line.strip().split(',')
		print(name, price)
#輸入檔案
i = 0
product = []
while True:
	name = input('請輸入商品名稱：' )
	if name == 'q':
		break
	price = input('請輸入商品價格：' )
	price = int(price)
	i = i + price
	price = str(price)
	n_p = []
	n_p.append(name)
	n_p.append(price)
	product.append(n_p)
	print('成功加入商品！！！') 

for p in product:
	print(p[0], '的價格是', p[1])

print('你總共買了', product)
print('總共是', i, '元')

with open('product.csv', 'w', encoding = 'utf-8') as d:
	d.write('商品' + ',' + '價格' + '\n')
	for p in product:
		d.write(p[0] + ',' + p[1] + '\n')

