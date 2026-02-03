prices = {
    "apple": 5.00,
    "banana": 6.00,
    "milk": 7.00,
    "bread": 8.00,
    "cheese": 9.00,
}

item1_name = input("Enter the name of the first item: ").lower()
item1_quantity = int(input(f"Enter the quantity of {item1_name}: "))

item2_name = input("Enter the name of the second item: ").lower()
item2_quantity = int(input(f"Enter the quantity of {item2_name}: "))

item3_name = input("Enter the name of the third item: ").lower()
item3_quantity = int(input(f"Enter the quantity of {item3_name}: "))

item1_price = prices.get(item1_name,0)
item2_price = prices.get(item2_name,0)
item3_price = prices.get(item3_name,0)

item1_total = item1_price * item1_quantity
item2_total = item2_price * item2_quantity
item3_total = item3_price * item3_quantity

subtotal = item1_total + item2_total + item3_total
tax = subtotal * 0.085
total = subtotal + tax

print("\n----------Receipt----------")
print(f"{item1_name.capitalize()} : {item1_quantity} @  ${item1_price :2f} each = ${item1_total:.2f}")
print(f"{item2_name.capitalize()} : {item2_quantity} @  ${item2_price :2f} each = ${item2_total:.2f}")
print(f"{item3_name.capitalize()} : {item3_quantity} @  ${item3_price :2f} each = ${item3_total:.2f}")

print(f"Subtotal : ${subtotal:.2f}")
print(f"Tax (8.5%) : ${tax:.2f}")
print(f"Total : ${total:.2f}")