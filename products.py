# 讀取檔案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
    for line in f:
        if '商品,價格' in line:
            continue # 繼續
        name, price = line.strip().split(',')
        products.append([name, price])
print(products)

# 讓使用者輸入
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品的價格: ')
    price = int(price)
    p = [name, price] # 小清單裡存 name 和 price
    products.append(p) # 把小清單(p)存進大清單(products)
print(products)

# 印出所有商品購買紀錄
for p in products:
    print(p[0], '的價格是', p[1])

# 把名稱和價格寫成txt檔
with open('products.txt','w') as f:
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')

# 把名稱和價格寫成csv檔，可以用excel打開
with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n') # csv檔用'，'區隔

