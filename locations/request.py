LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
                "address": "<address for Nashville North>"
    },
    {
        "id": 2,
        "name": "Nashville South",
                "address": "<address for Nashville South>"
    },
    {
        "id": 3,
        "name": "Nashville West",
                "address": "<address for Nashville West>"
    },
]


def get_all_locations():
    """Returns the entire LOCATIONS list as a json string.
    """
    return LOCATIONS


def get_single_location(id):
    """Finds a single location in LOCATIONS using an integer id and returns it as a json string

    Args:
            id (int): the integer id we are looking for in LOCATIONS

    Returns:
            dict: the requested location
    """
    requested_location = None
    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location
    return requested_location
