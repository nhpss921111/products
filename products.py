products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品的價格: ')
    p = [name, price] # 小清單裡存 name 和 price
    products.append(p) # 把小清單(p)存進大清單(products)
print(products)

for p in products:
    print(p[0], '的價格是', p[1])