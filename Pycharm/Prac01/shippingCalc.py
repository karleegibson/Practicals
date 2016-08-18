item_number = int(input("Number of items: "))
while item_number < 0:
    print("Invalid number of items!")
    item_number = int(input("Number of items: "))
total_shipping_cost = 0
for i in range(item_number):
    item_cost = float(input('Price of item: '))
    total_shipping_cost += item_cost
if total_shipping_cost > 100:
    total_price = 0.9*total_shipping_cost
else:
    total_price = total_shipping_cost
print("Total price for", str(item_number), "items is $", str(total_price))
