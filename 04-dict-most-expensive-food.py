from typing import Dict

starters = {
    "Potato Pancakes": 7.99,
    "Salami Platter": 10.29,
    "Brezel": 6.99,
    "Maultaschen": 9.99,
    "Fried Potatoes": 4.99
}

mains = {
    "Braised Beef Short Ribs": 18.99,
    "Paprika Beef Goulash": 15.5,
    "Jager Schnitzel": 16.99,
    "House-mase Bratwurst": 11.99,
    "Kasespatzle": 14.99,
    "German Ravioli": 12.79,
    "Curry Wurst": 10.99
}

desserts = {
    "Chilled Chocolate Fondant": 7.9,
    "Pepermint Crisp Tart": 5.9,
    "Ginger Cobbler": 6.9,
    
}

beers = {
    "Stigel Radler": 6.9,
    "Munich Lager": 7.9,
    "Kong Ludwig Weissbier": 8.9,
    "Warsteiner Punkel": 7.5,
}

courses = [starters, mains, desserts, beers]

def get_most_expensive(course: Dict[str, float]) -> str:
    return max(course, key=course.get)


# choices = {
#     get_most_expensive(course): course[get_most_expensive(course)]
#     for course in courses
# }
# print(choices)

choices = {}
for course in courses:
    choice = get_most_expensive(course)
    choices[choice] = course[choice]
    

cost = sum(choices.values())

tip = cost * 0.1

print(tip)

