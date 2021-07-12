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
    """get_all_animals returns the entire ANIMALS list"""
    return ANIMALS

def get_single_animal(id):
    """get_single_animal finds a single animal in ANIMALS using an id

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
