# products [[name],[price]]
# check file
products = []
import os
if os.path.isfile('products.csv'):
    print('Yes')
    with open('products.csv','r', encoding='utf-8') as f:
        for line in f:
            if 'Chinese,Chinesee' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    print(products)
else:
    print('No')

# user to input
while True:
    name = input('Please enter name of product: ')
    if name == 'q':
    	break
    price = input('Please enter price of product: ')
    price = int(price)
    products.append([name, price])
print(products)

for p in products:
	print('The price of', p[0], 'is', p[1])

# write file in csv
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('Chinese,Chinesee\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') # if one of it is integer, then cannot combine, need to change back to string


