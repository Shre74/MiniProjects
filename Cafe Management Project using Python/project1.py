#Define-the menu of resturant
menu = {
    'Pizza':40,
    'Pasta':50,
    'Burger':60,
    'Salad':70,
    'Coffee':80,
}

print(menu)

#Great 
print("Welcome to Sunita's Resturant")
print("Pizza: Rs40\nPasta: Rs50\nBurger: Rs60\nSalad: Rs70\nCoffee: Rs80\n")

order_total = 0
item_1 = input("Enter the name of the item you want to order = ")
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not avaliable yet!")

another_order = input("Do you want to add another item?(Yes/No)") 
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"Item{item_2}has been added to order")
    else:
        print("Ordered item {item_2} is not avaliable!")
print(f"The total amount of items to pay is {order_total}")               

