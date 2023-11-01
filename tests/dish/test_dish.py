from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


def test_dish():
    dish_food = Dish("DishName", 99.0)
    assert dish_food.name == "DishName"
    assert dish_food.price == 99.0
    assert dish_food.recipe == {}
    assert repr(dish_food) == "Dish('DishName', R$99.00)"
    assert hash(dish_food) == hash("Dish('DishName', R$99.00)")

    ingredient_food = Ingredient("queijo_mussarela")
    dish_food.add_ingredient_dependency(ingredient_food, 1)

    assert dish_food.get_restrictions() == ingredient_food.restrictions
    assert dish_food.get_ingredients() == {ingredient_food}

    dish_dessert = Dish("DishDoce", 7.99)

    assert dish_food != dish_dessert
    assert dish_food == dish_food

    with pytest.raises(TypeError):
        Dish("DishName", "99.0")
    with pytest.raises(ValueError):
        Dish("DishName", -99)
