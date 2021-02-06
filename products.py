products = []
while True:
    name = input('Please enter name of product: ')
    if name == 'q':
    	break
    price = input('Please enter price of product: ')
    price = int(price)
    p = []
    p.append(name) # easier: p = [name, price]
    p.append(price)
    products.append(p) # easier: products.append([name, price]) then no need above 3 rows
print(products)

products[0][0]

for p in products:
	print('The price of', p[0], 'is', p[1])


with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品, 價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') # if one of it is integer, then cannot combine, need to change back to string


