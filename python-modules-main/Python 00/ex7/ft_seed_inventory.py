def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit != "packets" and unit != "grams" and unit != "area":
        print("Unknown unit type")
    else:
        if seed_type == "tomato":
            print(f"{seed_type.capitalize()} seeds:", end=" ")
            print(f"{quantity} {unit} avaliable")
        if seed_type == "carrot":
            print(f"{seed_type.capitalize()} seeds: {quantity} {unit} total")
        if seed_type == "lettuce":
            print(f"{seed_type.capitalize()} seeds: {quantity} square meters")
