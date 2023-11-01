from models.dish import Dish
from models.ingredient import Ingredient
import csv


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        with open(source_path, "r") as file:
            recipes = list(csv.DictReader(file))

        for recipe in recipes:
            dish = Dish(recipe["dish"], float(recipe["price"]))
            self.dishes.add(dish)

        for dish in self.dishes:
            for recipe in recipes:
                if dish.name == recipe["dish"]:
                    dish.add_ingredient_dependency(
                        Ingredient(recipe["ingredient"]),
                        int(recipe["recipe_amount"]),
                    )
