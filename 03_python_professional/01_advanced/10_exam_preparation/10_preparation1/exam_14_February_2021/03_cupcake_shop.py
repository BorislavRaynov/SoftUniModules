def stock_availability(lst, line, *args):
    inventory = lst
    command = line
    if command == "delivery":
        inventory.extend(args)
        return inventory
    else:
        if args:
            if str(args[0]).isdigit():
                return inventory[int(args[0])::]
            else:
                for el in args:
                    if el in inventory:
                        inventory = [x for x in inventory if x != el]
                return inventory
        else:
            inventory.pop(0)
            return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))



