import os #operating system
product = []
#讀取檔案#判斷檔案是否存在
def read_file(filename):
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f :
			if '商品,價格' in line :
				continue # 等於skip掉商品價格這一欄
			name, price = line.strip().split(',') #strip忽略換行 split（','）用逗號切割
			product.append([name, price])
		print('你目前已經買了：', product)
	return product
#輸入檔案
def write(product):
	while True:
		name = input('請輸入商品名稱：' )
		if name == 'q':
			break
		price = input('請輸入商品價格：' )
		n_p = []
		n_p.append(name)
		n_p.append(price)
		product.append(n_p)
		print('成功加入商品！！！') 
	return product
#存入資料
def save_file(filename, product):
	with open(filename, 'w', encoding = 'utf-8') as d:
		d.write('商品' + ',' + '價格' + '\n' )
		for p in product:
			d.write(p[0] + ',' + p[1] + '\n')
#主程式
def main():
	if os.path.isfile('product.csv'):
			print('已找到檔案！')#判斷檔案是否存在
			product = read_file('product.csv')
	else:
			print('找不到相應檔案...')
	product = write(product)
	for p in product:
			print(p[0], '的價格是', p[1])

	print('你這次總共買了', product)
	save_file('product.csv', product)
#執行主程式
main()




