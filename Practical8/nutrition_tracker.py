# nutrition_tracker.py
# Track daily nutrition intake using a food_item class.
# Summarises total calories, protein, carbs, and fat over 24 hours,
# and warns if limits are exceeded.

import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


class food_item:
    """Represents a single food item with its nutritional values."""

    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat


def daily_summary(food_list):
    """
    Calculate total nutrition from a list of food_item objects.

    Prints the totals for calories, protein, carbohydrates, and fat.
    Issues a warning if calories exceed 2500 or fat exceeds 90 g.

    Args:
        food_list (list): list of food_item instances consumed in 24 hrs
    """
    total_cal = 0
    total_protein = 0
    total_carbs = 0
    total_fat = 0

    for food in food_list:
        total_cal += food.calories
        total_protein += food.protein
        total_carbs += food.carbs
        total_fat += food.fat

    print("--- Daily Nutrition Summary ---")
    print(f"Calories:      {total_cal} kcal")
    print(f"Protein:       {total_protein} g")
    print(f"Carbohydrates: {total_carbs} g")
    print(f"Fat:           {total_fat} g")

    if total_cal > 2500:
        print("WARNING: Calorie intake exceeds 2500 kcal!")
    if total_fat > 90:
        print("WARNING: Fat intake exceeds 90 g!")


# ---- example usage ----
if __name__ == "__main__":
    # create some food items
    apple = food_item("Apple", 60, 0.3, 15, 0.5)
    chicken = food_item("Chicken breast", 165, 31, 0, 3.6)
    rice = food_item("Rice (1 cup)", 206, 4.3, 45, 0.4)
    egg = food_item("Egg", 78, 6, 0.6, 5)

    # a normal day
    normal_day = [apple, chicken, rice, egg]
    daily_summary(normal_day)

    print()

    # a heavy day that triggers warnings
    pizza = food_item("Pizza (large)", 2500, 100, 300, 95)
    burger = food_item("Burger", 800, 40, 60, 45)
    heavy_day = [pizza, burger]
    daily_summary(heavy_day)
