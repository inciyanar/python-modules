def validate_ingredients(ingredients: str) -> str:
    check_list: list[str] = ["earth", "air", "fire", "water"]
    for item in check_list:
        if item in ingredients.lower():
            return (f"{ingredients} - VALID")
    return (f"{ingredients} - INVALID")
