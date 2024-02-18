"""

Your task is to write a set of classes modeling food ingredients, meals, and a daily plan. They will make it possible to easily count how much protein, carbohydrates, fats and calories are provided in each plan.

Ingredient
Write a class representing an ingredient of a meal. Its __init__ method should take:

name (str)
amount of protein in 100g of product (float or int)
amount of carbohydrates in 100g of product (float or int)
amount of fats in 100g of product (float or int)
Meal
Write a class representing meals. Its __init__ method should take one argument: the name of a meal.

Write a method for it that will enable adding a specific amount of ingredients (in grams).

Daily plan
Write a class representing a daily plan. It should have a method to add new meals and another method printing the summary (see example below)

"""
from collections import namedtuple


class Ingredient:
    def __init__(self, name: str, proteins: float, carbs: float, fats: float):
        self.name = name
        self.proteins = proteins
        self.carbs = carbs
        self.fats = fats

    def calculate_nutrition_values(self, grams):
        proteins = grams / 100 * self.proteins
        carbs = grams / 100 * self.carbs
        fats = grams / 100 * self.fats
        kcal = proteins * 4 + carbs * 4 + fats * 9
        return proteins, carbs, fats, kcal

    def __repr__(self):
        return f"{self.name}"


class Meal:
    def __init__(self, name: str):
        self.name = name
        self.ingredients = {}

    def add_ingredient(self, ingredient: Ingredient, grams: float):
        self.ingredients[ingredient] = grams

    def calculate_nutrition_values(self):
        proteins_per_meal, carbs_per_meal, fats_per_meal, kcal_per_meal = 0, 0, 0, 0
        for ingredient, grams in self.ingredients.items():
            proteins, carbs, fats, kcal = ingredient.calculate_nutrition_values(grams)
            proteins_per_meal += proteins
            carbs_per_meal += carbs
            fats_per_meal += fats
            kcal_per_meal += kcal

        return proteins_per_meal, carbs_per_meal, fats_per_meal, kcal_per_meal

    def print_details(self):
        print(f"Meal: {self.name}")
        for ingredient, grams in self.ingredients.items():
            protein, carbs, fats, calories = ingredient.calculate_nutrition_values(grams)
            print(f"\t - {grams}g {ingredient} ({protein=}g, {carbs=}g, {fats=}g {calories=}")

        proteins_per_meal, carbs_per_meal, fats_per_meal, kcal_per_meal = self.calculate_nutrition_values()
        print(f"Total: {proteins_per_meal=}g, {carbs_per_meal=}g, {fats_per_meal=}g {kcal_per_meal=}\n")


class DailyPlan:
    def __init__(self):
        self.meals: list[Meal] = []

    def add_meal(self, meal: Meal):
        self.meals.append(meal)

    def print_summary(self):
        daily_proteins, daily_carbs, daily_fats, daily_kcal = 0, 0, 0, 0

        for meal in self.meals:
            meal.print_details()

            proteins, carbs, fats, kcal = meal.calculate_nutrition_values()
            daily_proteins += proteins
            daily_carbs += carbs
            daily_fats += fats
            daily_kcal += kcal
        print(f"DAILY TOTAL: {daily_proteins=}g, {daily_carbs=}g, {daily_fats=}g {daily_kcal=}")


if __name__ == "__main__":
    egg = Ingredient("egg", proteins=13, carbs=1.1, fats=11)
    tomato = Ingredient("tomato", proteins=0.9, carbs=3.9, fats=0.2)
    bread = Ingredient("bread", proteins=9, carbs=49, fats=3.2)

    scrambled_eggs = Meal("scrambled eggs")
    scrambled_eggs.add_ingredient(egg, 200)
    scrambled_eggs.add_ingredient(tomato, 50)

    sandwich = Meal("sandwich")
    sandwich.add_ingredient(bread, 25)
    sandwich.add_ingredient(tomato, 50)

    minimal_menu = DailyPlan()
    minimal_menu.add_meal(scrambled_eggs)
    minimal_menu.add_meal(sandwich)

    minimal_menu.print_summary()

