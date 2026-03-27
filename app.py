from services import *
from files import *
#The code should be executed here in app.py

inventory = []   # Main list of products
running = True   # Control variable for the loop

print("========")
print("WELCOME")
print("========")

# Main loop
while running:
    print("""
1 - Add product
2 - Show products
3 - Search product
4 - Update product
5 - Remove product
6 - Statistics
7 - Save CSV
8 - Load CSV
9 - Exit    
    """)

    try:
        # Ask user for option
        option = int(input("Choose an option: "))

        # ADD PRODUCT
        if option == 1:
            name = input("Insert product name: ")
            price = float(input("Insert price: "))
            quantity = int(input("Insert quantity: "))
            add_product(inventory, name, price, quantity)

        # SHOW INVENTORY
        elif option == 2:
            show_inventory(inventory)

        # SEARCH PRODUCT
        elif option == 3:
            name = input("Insert name: ")
            product = search_product(inventory, name)

            if product:
                print(product)
            else:
                print("Product not found")

        # UPDATE PRODUCT
        elif option == 4:
            name = input("Insert product name: ")

            # Allow skipping values
            price = input("New price (enter to skip): ")
            quantity = input("New quantity (enter to skip): ")

            update_product(
                inventory,
                name,
                float(price) if price else None,
                int(quantity) if quantity else None
            )

        # DELETE PRODUCT
        elif option == 5:
            name = input("Product name: ")
            delete_product(inventory, name)

        # SHOW STATISTICS
        elif option == 6:
            stats = calculate_statistics(inventory)

            if stats:
                print("Total units:", stats["total_units"])
                print("Total value:", stats["total_value"])
                print("Most expensive:", stats["most_expensive"])
                print("Highest stock:", stats["highest_stock"])

        # SAVE CSV
        elif option == 7:
            path = input("File path: ")
            save_csv(inventory, path)

        # LOAD CSV
        elif option == 8:
            path = input("File path: ")
            new_data = load_csv(path)

            if new_data:
                decision = input("Overwrite inventory? (Y/N): ").upper()

                # Replace inventory
                if decision == "Y":
                    inventory = new_data
                    print("Inventory replaced")

                # Merge inventory
                else:
                    for new in new_data:
                        existing = search_product(inventory, new["name"])

                        if existing:
                            existing["quantity"] += new["quantity"]
                            existing["price"] = new["price"]
                        else:
                            inventory.append(new)

                    print("Inventory merged")

        # EXIT PROGRAM
        elif option == 9:
            print("THANKS FOR USING")
            running = False  # End loop

        else:
            print("Invalid option")

    except:
        print("Invalid input, try again")
                                  