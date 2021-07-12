from json import dumps

EMPLOYEES = [
    {
        "id": 1,
        "name": "Tim",
        "locationId": 1
    },
    {
        "id": 2,
        "name": "Tom",
                "locationId": 2
    },
    {
        "id": 3,
        "name": "Steve",
                "locationId": 3
    }
]


def get_all_employees():
    """Returns the entire EMPLOYEES list as a json string.
    """
    return dumps(EMPLOYEES)


def get_single_employee(id):
    """Finds a single employee in EMPLOYEES using an integer id and returns it as a json string

    Args:
            id (int): the integer id we are looking for in EMPLOYEES

    Returns:
            dict: the requested employee
    """
    requested_employee = None
    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee
    return dumps(requested_employee)
