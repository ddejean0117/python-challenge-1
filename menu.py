# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
customer_order = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            menu_selection = input("Please enter a menu item number: ")

            # 3. Check if the customer typed a number
            if menu_selection.isdigit():
                print("Thank you for selecting a number.")

                # Convert the menu selection to an integer
                menu_selection = int(menu_selection)
                print(f'customer input is now an {type(menu_selection)}')

                # 4. Check if the menu selection is in the menu items
                if menu_selection in menu_items.keys():
                    
                    # Store the item name as a variable
                    print(menu_items)
                    menu_value = menu_items[menu_selection]["Item name"]
                    print(f"Thanks for choosing {menu_value} from the menu. ")

                    # Ask the customer for the quantity of the menu item
                    quantity = input("Please enter how many you would like. Your quantity will default to 1 if your input is invalid. ")

                    # Check if the quantity is a number, default to 1 if not
                    if quantity.isdigit():
                        quantity = int(quantity)
                        print(f"Thank you for selecting quantity {quantity}.")

                    # Tell the customer that their input isn't valid
                    else:
                        print(f"Sorry, {quantity} is not a valid number. I'll assume you meant 1. ")
                        quantity = 1

                        # Add the item name, price, and quantity to the order list
                        # for item in customer_order:
                    customer_order.append(
                        {"Item name": menu_value,
                        "Price": float(menu_items[menu_selection]["Price"]),
                        "Quantity": int(quantity)
                        })
                    print(customer_order)
                    
                # Tell the customer they didn't select a menu option
                else:
                    print(f"Sorry, your entry, {menu_selection}, is not on the menu." )
            else:
                # Tell the customer they didn't select a number
                print(f"'{menu_selection}' is not a number. Please try again. ")  
        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_selection} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print(f"'{menu_category}' is not a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input
        match keep_ordering.lower():
            # Customer chose yes
            case 'y':
                # Keep ordering
                place_order = True
                # Exit the keep ordering question loop
                break
            # Customer chose no
            case 'n':
                # Complete the order
                place_order = False
                # Since the customer decided to stop ordering, thank them for
                # their order
                print("Thank you for your order.")
                # Exit the keep ordering question loop
                break
            case _:
                # Tell the customer to try again
                print("I didn't understand your response. Please try again. ")

# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

##print(customer_order)

# 6. Loop through the items in the customer's order
order_sum = 0

for order_index in range(len(customer_order)):
    # 7. Store the dictionary items as variables

    order_item_name = customer_order[order_index]["Item name"]
    # print(order_item_name)
    order_item_price = customer_order[order_index]["Price"]
    #price_length = len(str(order_item_price))
    # print(order_item_price)
    order_item_qty = customer_order[order_index]["Quantity"]
    # print(order_item_qty)


    # 8. Calculate the number of spaces for formatted printing
    num_item_spaces_1 = 24 - len(order_item_name)
    item_spaces_1 = " " * num_item_spaces_1
    num_item_spaces_2 = 5 - len(str(order_item_price))
    item_spaces_2 = " " * num_item_spaces_2


    # 9. Create space strings
    # This task was completed above in #8

    # 10. Print the item name, price, and quantity
    print(f"{order_item_name} {item_spaces_1} | ${order_item_price}{item_spaces_2} |    {order_item_qty}")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.

item_totals = []
item_totals = [x["Price"] * x["Quantity"] for x in customer_order]
print(item_totals)
order_sum = sum([round(float_num,2) for float_num in item_totals])
print(f"Your order total comes to ${order_sum}. ")