
# Define a class for menu items
class MenuItem:
    def __init__(self, name, price, description, category):
        self.name = name
        self.price = price
        self.description = description
        self.category = category

# Create an empty list to store menu items
menu = []

# Function to add a new menu item
def add_menu_item():
    name = input("Enter the name of the item: ")
    price = float(input("Enter the price of the item: "))
    description = input("Enter a description for the item: ")
    category = input("Enter the category of the item: ")
    menu.append(MenuItem(name, price, description, category))
    print("Menu item added successfully!")

# Function to remove a menu item
def remove_menu_item():
    name = input("Enter the name of the item to remove: ")
    for item in menu:
        if item.name == name:
            menu.remove(item)
            print("Menu item removed successfully!")
            return
    print("Item not found in the menu.")

# Function to update a menu item
def update_menu_item():
    name = input("Enter the name of the item to update: ")
    for item in menu:
        if item.name == name:
            item.name = input("Enter the new name for the item: ")
            item.price = float(input("Enter the new price for the item: "))
            item.description = input("Enter the new description for the item: ")
            item.category = input("Enter the new category for the item: ")
            print("Menu item updated successfully!")
            return
    print("Item not found in the menu.")

# Function to display the complete menu
def display_menu():
    for item in menu:
        print("Name:", item.name)
        print("Price:", item.price)
        print("Description:", item.description)
        print("Category:", item.category)
        print("---------------------")

# Function to filter items based on category
def filter_by_category():
    category = input("Enter the category to filter by: ")
    filtered_menu = [item for item in menu if item.category == category]
    if filtered_menu:
        for item in filtered_menu:
            print("Name:", item.name)
            print("Price:", item.price)
            print("Description:", item.description)
            print("--------------------")