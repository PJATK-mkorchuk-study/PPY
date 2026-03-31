name = input("Enter the names of the products: ")
quantity = input("Enter the quantity of each product respectively: ")
unit_price = input("Enter the price of each product respectively: ")

result_price = 0
product = name.split()
order = tuple(x for x in product)



q_split = quantity.split()
p_split = unit_price.split()

for i in range(len(q_split)):
    result_price += int(q_split[i]) * int(p_split[i])
shopping_cart = list(order)

print("Your final order: ", shopping_cart)
print("Final price: ", result_price)
