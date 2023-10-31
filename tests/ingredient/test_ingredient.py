from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredients = Ingredient("queijo mussarela")
    print(ingredients.restrictions)
    assert ingredients.name == "queijo mussarela"
    assert ingredients.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
    assert repr(ingredients) == "Ingredient('queijo mussarela')"

    ingredients2 = Ingredient("ovo")
    ingredients3 = Ingredient("queijo mussarela")
    assert ingredients != ingredients2
    assert ingredients == ingredients3

    assert hash(ingredients) == hash(ingredients.name)
