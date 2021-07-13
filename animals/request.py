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


def get_all_animals():
    """Returns the entire ANIMALS list as a json string.
    """
    return ANIMALS


def get_single_animal(id):
    """Finds a single animal in ANIMALS using an integer id and returns it as a json string.

    Args:
        id (int): the integer id we are looking for in ANIMALS

    Returns:
        dict: the requested animal
    """
    # init an empty variable
    requested_animal = None
    for animal in ANIMALS:
        if animal["id"] == id:
            requested_animal = animal
    return requested_animal


def post_single_animal(animal):
    """Takes a animal, adds it to ANIMALS and returns it with it's shiny new id

    Args:
        animal (dict): the animal item

    Returns:
        dict: the animal item with it's id in ANIMALS
    """
    # Reverse index the ANIMALS to get the highest id
    max_id = ANIMALS[-1]["id"]

    new_id = max_id + 1
    animal["id"] = new_id
    ANIMALS.append(animal)
    return animal
