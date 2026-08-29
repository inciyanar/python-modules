def light_spell_allowed_ingredients() -> list[str]:
    str_list: list[str] = ["earth", "air", "fire", "water"]
    return (str_list)

def light_spell_record(spell_name: str, ingredients: str) -> str:
    validate_ingredients()
