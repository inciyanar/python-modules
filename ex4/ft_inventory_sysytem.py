import sys


def colon_finder(text: str) -> int:
    i = 0
    while i < len(text):
        if text[i] == ":":
            return (i)
        i += 1
    return (-1)


def parse_argument(text: str):
    colon_placement = colon_finder(text)
    if colon_placement == -1 or colon_placement == 0 or colon_placement == len(text) - 1:
        return None
    name = text[:colon_placement]
    quantity_str = text[colon_placement + 1:]
    return (name, quantity_str)


def inventory_maker(args: list) -> dict:
    inventory: dict = {}
    for argument in args:
        parsed = parse_argument(argument)
        if parsed is None:
            print(f"Error - invalid parameter '{argument}'")
            continue
        name, quantity_str = parsed
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            quantity = int(quantity_str)
        except ValueError:
            print(f"Quantity error for '{name}': invalid literal for int() with base 10: '{quantity_str}'")
            continue
        inventory[name] = quantity
    return (inventory)


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    inventory: dict = inventory_maker(sys.argv[1:])
    print(f"Got inventory: {inventory}")

    item_list: list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_quantity: int = sum(inventory.values())
    print(f"Total quantity of the {len(item_list)} items: {total_quantity}")

    if total_quantity > 0:
        for item in item_list:
            percentage = round(inventory[item] / total_quantity * 100, 1)
            print(f"Item {item} represents {percentage}%")

        most_item = item_list[0]
        least_item = item_list[0]
        for item in item_list:
            if inventory[item] > inventory[most_item]:
                most_item = item
            if inventory[item] < inventory[least_item]:
                least_item = item
        print(f"Item most abundant: {most_item} with quantity {inventory[most_item]}")
        print(f"Item least abundant: {least_item} with quantity {inventory[least_item]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")
