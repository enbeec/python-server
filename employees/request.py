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


def get_all_employees():  # pylint: disable=missing-docstring
    return EMPLOYEES


def get_single_employee(id):  # pylint: disable=missing-docstring
    requested_employee = None
    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee
    return requested_employee


def post_single_employee(employee):  # pylint: disable=missing-docstring
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
