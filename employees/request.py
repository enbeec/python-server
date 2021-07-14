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
    return EMPLOYEES


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
    return requested_employee


def post_single_employee(employee):
    """Takes a employee, adds it to LOCATIONS and returns it with it's shiny new id

    Args:
        employee (dict): the employee item

    Returns:
        dict: the employee item with it's id in LOCATIONS
    """
    # Reverse index the LOCATIONS to get the highest id
    max_id = EMPLOYEES[-1]["id"]

    new_id = max_id + 1
    employee["id"] = new_id
    EMPLOYEES.append(employee)
    return employee


def delete_single_employee(id):  # pylint: disable=missing-docstring
    employees_index = -1
    for index, employees in enumerate(EMPLOYEES):
        if employees["id"] == id:
            employees_index = index

    if employees_index >= 0:
        EMPLOYEES.pop(employees_index)
