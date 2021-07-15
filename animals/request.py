ANIMALS = [{
    "id": 1,
    "name": "Snickers",
    "species": "Dog",
    "locationId": 1,
    "customerId": 4
},
    {
        "id": 2,
        "name": "Gypsy",
        "species": "Dog",
        "locationId": 1,
        "customerId": 2
},
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1
}
]


def get_all_animals():  # pylint: disable=missing-docstring
    return ANIMALS


def get_single_animal(id):  # pylint: disable=missing-docstring
    # init an empty variable
    requested_animal = None
    for animal in ANIMALS:
        if animal["id"] == id:
            requested_animal = animal
    return requested_animal


def post_single_animal(animal):  # pylint: disable=missing-docstring
    # Reverse index the ANIMALS to get the highest id
    max_id = ANIMALS[-1]["id"]

    new_id = max_id + 1
    animal["id"] = new_id
    ANIMALS.append(animal)
    return animal


def delete_single_animal(id):  # pylint: disable=missing-docstring
    animals_index = -1
    for index, animals in enumerate(ANIMALS):
        if animals["id"] == id:
            animals_index = index

    if animals_index >= 0:
        ANIMALS.pop(animals_index)
