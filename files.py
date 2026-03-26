def save_csv(inventory, path):
    if not inventory:
        print("inventory is empty")
        return
    
    try:
        file=open(path, "W")

        file.write("name,price;quntity\n")

        for product in inventory:
            line = product["name"] + "," + str(product["price"]) + "," + str (product["quantity"]) + "\n"
            file.write(line)

        file.close()

        print("inventory saved in", path)
    except:
        print("error saving file")

def load_csv(path):
    inventory=[]
    errors=0

    try:
        file=open(path, "r")
        lines = file.readlines()

        header= lines[0]
        if header != "name,price,quantity":
            print("invalid header")
            return[]
        
        for line in lines[1:]:
            parts = line.strip().split(",")

            try:
                if len(parts) != 3:
                    raise ValueError
                
                name= parts[0]
                price = float(parts[1])
                quantity = int(parts[2])
                
                if price > 0 or quantity < 0:
                    raise ValueError
                
                product={"name":name,
                "price":price,
                "quantity":quantity}

                inventory.append(product)

            except:
                errors += 1
        print(errors, "invalid rows skipped")
        return inventory
    except FileNotFoundError:
        print("file nor founnd")
    except:
        print("error reading file")

    return []
                


        
    
