while True:

# 상품가격 입력받기
price = int(input("가격: "))
if price != 0000:

# 배송비 결정
if price > 20000:
    shipping_cost = 0
elif price > 10000:
    shipping_cost = 1000
elif price > 5000:
    shipping_cost = 500
else:
    shipping_cost = 3000

# 배송비 출력
print("배송비: ". shipping_cost)

#else:
#    print('Bye')
#    break