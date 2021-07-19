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


def get_all_locations():  # pylint: disable=missing-docstring
    return LOCATIONS


def get_single_location(id):  # pylint: disable=missing-docstring
    requested_location = None
    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location
    return requested_location


def post_single_location(location):  # pylint: disable=missing-docstring
    # Reverse index the LOCATIONS to get the highest id
    max_id = LOCATIONS[-1]["id"]

    new_id = max_id + 1
    location["id"] = new_id
    LOCATIONS.append(location)
    return location


def delete_single_location(id):  # pylint: disable=missing-docstring
    locations_index = -1
    for index, locations in enumerate(LOCATIONS):
        if locations["id"] == id:
            locations_index = index

    if locations_index >= 0:
        LOCATIONS.pop(locations_index)
