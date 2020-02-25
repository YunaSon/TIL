number_of_pizzas = eval(input("피자 몇판을 주문하겠습니까?: "))

cost_per_pizza = eval(input("피자 한 판은 얼마 입니까?"))
print(number_of_pizzas, type(number_of_pizzas))
print(cost_per_pizza, type(cost_per_pizza))

subtotal = number_of_pizzas * cost_per_pizza

tax_rate = 0.08

sales_tax = subtotal * tax_rate

total = subtotal + sales_tax

print("최종 가격은 ", total)
print("이 가격에는 피자 가격", subtotal, "과 함께 세금")
print(sales_tax, "이 포함돼 있습니다. ")
