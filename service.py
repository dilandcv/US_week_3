def add_product(inventory,name,price,quantity):
    product={"name":name,
             "price":price,
             "quantity":quantity}
    inventory.append(product)

def show_product(inventory):
    if not inventory:
        print("inventory is empty")
        return
    
    for product in inventory:
        print(f"{product["name"]} | {product["price"]} | {product["quantity"]}")

def search_product(inventory, name):
    for product in inventory:
        if product["name"] == name:
            return product
        return None
    
def update_product(inventory, name):
    new_price = None,  new_quantity = None
    product = search_product(inventory, name)

    if product:
        if new_price is not None:
            product["price"] = new_price
        if new_quantity is not None:
            product["quantity"] = new_quantity
    else:
        print("product not found")

def remove_product(inventory, name):
    product = search_product(inventory, name)

    if product:
        inventory.remove(product)
    else:
        print("product not found")

def calculate_staticts(inventory):
    if not inventory:
        print("inventory empty")
        return None
    
    total_units =0
    total_value=0

    most_expensive=inventory[0]
    highest_stock=inventory[0]

    for product in inventory:
        total_units += product["quantity"]
        total_value += product["price"] * product["quantity"]

        if product["price"] > most_expensive["price"]:
            most_expensive=product

        if product["quantity"] > highest_stock["quantity"]:
            highest_stock=product

    return {
            "total_units":total_units,
            "total_value":total_value,
            "most_expensive": most_expensive,
            "highest_stock":highest_stock}

