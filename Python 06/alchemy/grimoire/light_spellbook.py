from . import light_validator


def light_spell_allowed_ingredients() -> list[str]:
    ingredients: list[str] = ["earth", "air", "fire", "water"]
    return (ingredients)


def light_spell_record(spell_name: str, ingredients: str) -> str:
    result: str = light_validator.validate_ingredients(ingredients)
    if "INVALID" in result:
        return (f"Spell rejected: {spell_name} ({result})")
    else:
        return (f"Spell recorded: {spell_name} ({result})")
