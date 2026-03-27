# Save inventory to a CSV file
def save_csv(inventory, path):

    # Check if inventory is empty
    if not inventory:
        print("Inventory is empty")
        return
    
    try:
        # Open file in write mode
        file = open(path, "w")

        # Write header (column names)
        file.write("name,price,quantity\n")

        # Write each product as a line
        for product in inventory:
            line = product["name"] + "," + str(product["price"]) + "," + str(product["quantity"]) + "\n"
            file.write(line)

        # Close file
        file.close()

        print("Inventory saved in:", path)

    except:
        print("Error saving file")


# Load inventory from CSV file
def load_csv(path):

    inventory = []   # List to store products
    errors = 0       # Counter for invalid rows

    try:
        # Open file in read mode
        file = open(path, "r")

        # Read all lines
        lines = file.readlines()
        file.close()

        # Get and clean header
        header = lines[0].strip()

        # Validate header
        if header != "name,price,quantity":
            print("Invalid header")
            return []
        
        # Loop through data rows (skip header)
        for line in lines[1:]:
            parts = line.strip().split(",")

            try:
                # Validate number of columns
                if len(parts) != 3:
                    raise ValueError
                
                name = parts[0]
                price = float(parts[1])
                quantity = int(parts[2])
                
                # Validate non-negative values
                if price < 0 or quantity < 0:
                    raise ValueError
                
                # Create product dictionary
                product = {
                    "name": name,
                    "price": price,
                    "quantity": quantity
                }

                inventory.append(product)

            except:
                errors += 1  # Count invalid rows

        print(errors, "invalid rows skipped")
        return inventory

    except FileNotFoundError:
        print("File not found")
    except:
        print("Error reading file")

    return []