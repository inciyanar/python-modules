import sys


def find_colon(param: str) -> int:
    i = 0
    while i < len(param):
        if param[i] == ":":
            return i
        i += 1
    return -1


def parse_param(param: str):
    colon_pos = find_colon(param)
    if colon_pos == -1 or colon_pos == 0 or colon_pos == len(param) - 1:
        return None
    name = param[:colon_pos]
    quantity_str = param[colon_pos + 1:]
    return name, quantity_str


def build_inventory(args: list) -> dict:
    inventory: dict = {}
    for param in args:
        parsed = parse_param(param)
        if parsed is None:
            print(f"Error - invalid parameter '{param}'")
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
    return inventory


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    inventory: dict = build_inventory(sys.argv[1:])
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
