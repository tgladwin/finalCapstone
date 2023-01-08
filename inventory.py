# Hello
# Capstone project 4
# This project is a demonstration of OOP and classes

# ======== The beginning of the class ==========
class Shoe:  # This build the class Shoe and initialises 5 characteristics

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = int(cost)
        self.quantity = int(quantity)

    def get_cost(self):  # Returns the cost of the product
        return self.cost

    def get_quantity(self):  # Returns the quantity of the product
        return self.quantity

    def __str__(self):  # Returns a string containing the required information
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"


# ============= Shoe list ===========

shoe_list = []

# ========== Functions outside the class ==============


def read_shoes_data():  # Open text file and read to shoe list
    with open("inventory.txt", "r") as f:
        lines = f.readlines()
        for line in lines[1:]:
            data = line.split(",")
            country = data[0]
            code = data[1]
            product = data[2]
            cost = data[3]
            quantity = data[4]
            shoe = Shoe(country, code, product, cost, quantity)
            shoe_list.append(shoe)
    return shoe_list


def capture_shoes():  # Add new shoe data to shoe list, appends to list and then write to the text file
    country = input("Enter the country of origin: ")
    code = input("Enter the code for the shoes: ")
    product = input("Enter the name of the shoe: ")
    cost = int(input("Enter the cost of the shoe: "))
    quantity = int(input("Enter the quantity of shoe: "))
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)
    write_to_file()
    return shoe


def view_all():  # Views all shoes in the list
    for shoe in shoe_list:
        print(shoe)


def re_stock():
    min_quantity = 100000  # Sets an arbitrary to compare to
    min_quantity_shoe = None  # Sets the name of the lowest stock shoe to None - will be replaced with name later
    # Using the for loop below cycles through each line in the shoe list and compares quantity to 'min_quantity'
    # If the number being read is lower than min_quan then that shoes quantity and name is updated to the corresponding
    # variable
    for shoe in shoe_list:
        if shoe.get_quantity() < min_quantity:
            min_quantity = shoe.get_quantity()
            min_quantity_shoe = shoe
    update_stock = input(f"Do you want to add more stock for {min_quantity_shoe.product}? It has a quantity of"
                         f" {min_quantity_shoe.quantity} (y/n)?: ")  # Ask the user if they want to update the stock
    if update_stock.lower() == "y":
        update_quantity = int(input("Enter the new total quantity: "))
        min_quantity_shoe.quantity = update_quantity  # Updates the quantity of the shoe object
        write_to_file()


def search_shoe():  # Search for a shoe via a product code
    shoe_code = input("Enter the code of the desired shoe: ")
    for shoe in shoe_list:
        if shoe.code == shoe_code:
            print(shoe)
            return shoe
    return None


def value_per_item():  # Calculates the value of the stock, iterates through every shoe item and prints all
    for shoe in shoe_list:
        value = int(shoe.get_cost()) * int(shoe.get_quantity())
        print(f"Value for {shoe.product} from {shoe.country} with code {shoe.code}: £{value}")


def highest_qty():
    max_quantity = 0
    max_quantity_shoe = None
    # This section uses the same logic as the re stock function. The max stock is set to 0 and any shoe that has a
    # stock greater than this number is saved to the 2 variables above
    # The statement is printed to the terminal
    for shoe in shoe_list:
        if shoe.get_quantity() > max_quantity:
            max_quantity = shoe.get_quantity()
            max_quantity_shoe = shoe
    print(f"{max_quantity_shoe} has {max_quantity} in stock. You should put this shoe on sale.")


def write_to_file():  # Writes the shoe list back to the inventory file
    open_inventory = open("inventory.txt", "w")
    for shoe in shoe_list:
        open_inventory.write(str(shoe) + "\n")
    open_inventory.close()

# ========== Main Menu =============


read_shoes_data()  # Opens and reads the inventory to the list ready for use


while True:
    # Generates options menu for the user to read
    print('''
    Menu Options:
    - View all stock =          1
    - Add new shoe =            2
    - Re-Stock item =           3
    - Search product code =     4
    - Show stock value =        5
    - Most in stock =           6
    ''')
    try:
        menu_input = int(input("Enter menu choice: "))
        if menu_input > 6:  # Tells user input is out of range
            menu_input = int(input("Entered number too high, try again: "))

        if menu_input == 1:  # View all stock items
            print("Printing all stock items \n")
            view_all()

        if menu_input == 2:  # Add a new shoe and data to the list
            print("Adding new shoe to stock list \n")
            capture_shoes()

        if menu_input == 3:  # Restocks the lowest stock item to the users value
            print("Updating the lowest item stock \n")
            re_stock()

        if menu_input == 4:  # Searches the database for a specific product code
            print("Searching for a product via the product code \n")
            search_shoe()

        if menu_input == 5:  # Displays the value of every item in the inventory
            print("Displaying the value per item \n")
            value_per_item()

        if menu_input == 6:  # Shows the item with the highest quantity of stock and recommends they go on sale
            print("Displaying the item with the most stock \n")
            highest_qty()

    except ValueError:  # Allows for user to enter an unexpected input and not fall over
        print("That was not an option")

# Complete
