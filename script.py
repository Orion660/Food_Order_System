italian_food = [
  "Pasta Bolognese", "Pepperoni pizza", "Margherita pizza", "Lasagna"
]

indian_food = [
  "Curry", "Chutney", "Samosa", "Naan"
]
def find_meal(name, menu):
  return name if name in menu else None

def select_meal(name, food_type):
  if food_type == "Italian":
    return find_meal(name, italian_food)
  elif food_type == "Indian":
    return find_meal(name, indian_food)
  else:
    return None    

def display_available_meals(food_type):
  if food_type == "Italian":
    print("Available Italian Meals:") 
    for meal in italian_food:
      print(meal)
  elif food_type == "Indian":
    print("Available Indian Meals")
    for meal in indian_food:
      print(meal)
  else:
    print("Invalid food type")
  
def create_summary(name, amount, food_type):
  order = select_meal(name, food_type)
  if order:
    return f"{amount}, {order}"
  else:
    return "Meal not found"

print("Welcome to the Food Order System!")

type_input = input("What type of food do you want to order:")
display_available_meals(type_input)
name_input = input("What is your meal choice:")
amount_input = int(input("Order quantity:"))
result = create_summary(name_input, amount_input, type_input)
print(result)


