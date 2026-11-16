#0.8 Pet Shop
DOG_FOOD_PRICE = 2.50
CAT_FOOD_PRICE = 4

dogFoodCount = float(input())
catFoodCount = float(input())

dogFood = dogFoodCount * DOG_FOOD_PRICE
catFood = catFoodCount * CAT_FOOD_PRICE

sum = dogFood + catFood

print(f"{sum} lv.")