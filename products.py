products = []
while True:
    name = input('Please enter name of product: ')
    if name == 'q':
    	break
    price = input('Please enter price of product: ')
    p = []
    p.append(name) # easier: p = [name, price]
    p.append(price)
    products.append(p) # easier: products.append([name, price]) then no need above 3 rows
print(products)

products[0][0]

for p in products:
	print('The price of', p[0], 'is', p[1])