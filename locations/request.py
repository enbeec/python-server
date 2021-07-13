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


def post_single_location(location):
    """Takes a location, adds it to LOCATIONS and returns it with it's shiny new id

    Args:
        location (dict): the location item

    Returns:
        dict: the location item with it's id in LOCATIONS
    """
    # Reverse index the LOCATIONS to get the highest id
    max_id = LOCATIONS[-1]["id"]

    new_id = max_id + 1
    location["id"] = new_id
    LOCATIONS.append(location)
    return location
