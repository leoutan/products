import os
products = []

if os.path.isfile('products.csv'):
	print('找到檔案')
	#讀取檔案
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品, 價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
else:
	print('找不到檔案')

print(products)

#輸入新加入的名稱價格
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	p = []
	p = [name, price]
	products.append(p)

# 印出商品價格
print(products)
for p in products:
	print(p[0], '的價格為', p[1])

#寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品, 價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')

# data = [1, 3, 5, 7, 9]
# with open('test.txt', 'w') as f:
# 	for d in data:
# 		f.write(str(d) + '\n')

