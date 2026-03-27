# Add a new product to the inventory
def add_product(inventory, name, price, quantity):
    # Create a dictionary with product data
    product = {
        "name": name,
        "price": price,
        "quantity": quantity}
    
    # Add product to the list
    inventory.append(product)


# Show all products in the inventory
def show_inventory(inventory):
    # Check if inventory is empty
    if not inventory:
        print("Inventory is empty")
        return
    
    # Loop through each product and print its data
    for product in inventory:
        print(f'Product: {product["name"]} | Price: {product["price"]} | Quantity: {product["quantity"]}')


# Search for a product by name
def search_product(inventory, name):
    # Loop through products
    for product in inventory:
        if product["name"] == name:
            return product  # Return product if found
    return None  # Return None if not found


# Update product price or quantity
def update_product(inventory, name, new_price=None, new_quantity=None):
    # Find the product
    product = search_product(inventory, name)

    if product:
        # Update price if provided
        if new_price is not None:
            product["price"] = new_price
        # Update quantity if provided
        if new_quantity is not None:
            product["quantity"] = new_quantity
    else:
        print("Product not found")


# Delete a product from inventory
def delete_product(inventory, name):
    # Find the product
    product = search_product(inventory, name)

    if product:
        inventory.remove(product)  # Remove from list
    else:
        print("Product not found")


# Calculate inventory statistics
def calculate_statistics(inventory):
    # Check if inventory is empty
    if not inventory:
        print("Inventory empty")
        return None
    
    total_units = 0      # Total quantity of products
    total_value = 0      # Total value (price * quantity)

    # Assume first product as initial reference
    most_expensive = inventory[0]
    highest_stock = inventory[0]

    # Loop through products
    for product in inventory:
        total_units += product["quantity"]
        total_value += product["price"] * product["quantity"]

        # Check most expensive product
        if product["price"] > most_expensive["price"]:
            most_expensive = product

        # Check product with highest stock
        if product["quantity"] > highest_stock["quantity"]:
            highest_stock = product

    # Return results in a dictionary
    return {
        "total_units": total_units,
        "total_value": total_value,
        "most_expensive": most_expensive,
        "highest_stock": highest_stock}