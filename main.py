data = []
amount = int(input('Enter the amount products in check:'))
for i in range(amount):
    name = input('Enter the name of products: ')
    price = float(input('Enter the price of products: '))
    amount_products = int(input('Enter the amount of products: '))
    data.append([name, price, amount_products])
suma = 0
for i in data:
    suma = i[1] * i[2]
print('The suma of all products is: ', suma)
print('Зведений реєстер податків: ', suma * 0.18)
for i in data:
    print(i[0], '-',  i[1], '-', i[2], '-', i[1] * i[2])
