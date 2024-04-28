class InventorySystem:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_name, quantity):
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
        else:
            self.inventory[item_name] = quantity
        print(f"{quantity} {item_name}(s) added to inventory.")

    def remove_item(self, item_name, quantity):
        if item_name in self.inventory:
            if self.inventory[item_name] >= quantity:
                self.inventory[item_name] -= quantity
                print(f"{quantity} {item_name}(s) removed from inventory.")
            else:
                print("Insufficient quantity in inventory.")
        else:
            print("Item not found in inventory.")

    def display_inventory(self):
        print("Inventory:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")

def main():
    inventory_system = InventorySystem()
    print("Welcome to the Inventory System!")

    while True:
        print("\nWhat would you like to do?")
        print("1. Add item to inventory")
        print("2. Remove item from inventory")
        print("3. Display inventory")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity to add: "))
            inventory_system.add_item(item_name, quantity)
        elif choice == '2':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity to remove: "))
            inventory_system.remove_item(item_name, quantity)
        elif choice == '3':
            inventory_system.display_inventory()
        elif choice == '4':
            print("Exiting Inventory System.")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
