import pprint

class Person:
    def __init__(self, age, gender, weight):
        self.age = age
        self.gender = gender
        self.weight = weight

    def __repr__(self):
        return f"Person(age={self.age}, gender='{self.gender}', weight={self.weight})"


# Task: Show men in descending order of age
people = [
    Person(32, "M", 140),
    Person(32, "F", 132),
    Person(65, "M", 160),
    Person(12, "F", 95),
    Person(42, "M", 150),
]

# Show people with gender "M"
people = list(filter(lambda person: person.gender == "M", people))
#OR
people = [person for person in people if person.gender == "M"]

# Sort in-place
people.sort(key=lambda person: person.age, reverse=True)
# OR
people.sort(key=lambda person: -person.age)

pprint.pprint(people)

print('\n')

# Task: Show all people, first sorted by age descending, and if age is equal, 
# sort by weight descending.
people = [
    Person(32, "M", 140),
    Person(32, "F", 132),
    Person(65, "M", 160),
    Person(12, "F", 95),
    Person(42, "M", 150),
    Person(60, "M", 175),
    Person(60, "M", 189),
    Person(60, "M", 192),
    Person(60, "M", 130)
]

people.sort(key=lambda person: (-person.age, -person.weight))
pprint.pprint(people)