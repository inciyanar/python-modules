from . import dark_validator


def dark_spell_allowed_ingredients() -> list[str]:
    ingredients: list[str] = ["bats", "frogs", "arsenic", "eyeball"]
    return (ingredients)


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    result: str = dark_validator.dark_validate_ingredients(ingredients)
    if "INVALID" in result:
        return (f"Spell rejected: {spell_name} ({result})")
    else:
        return (f"Spell recorded: {spell_name} ({result})")
