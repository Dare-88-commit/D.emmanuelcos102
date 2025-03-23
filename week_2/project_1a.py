total_cost = 0
purchase = int(input("Number of items purchased: "))
for items in range(purchase):
    name = input("Name of item purchased: ")
    price = int(input("Price of item purchased: "))
    quant = int(input("Quantity purchased: "))
    cost = price * quant
    total_cost += cost
    print(f"You purchased {quant} {name} at {price}, cost is: {cost}")

print(f"Total cost of all items is {total_cost}")
