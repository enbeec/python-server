CUSTOMERS = [{
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


def get_all_customers():
    """Returns the entire CUSTOMERS list as a json string.
    """
    return CUSTOMERS


def get_single_customer(id):
    """Finds a single customer in CUSTOMERS using an integer id and returns it as a json string.

    Args:
        id (int): the integer id we are looking for in CUSTOMERS

    Returns:
        dict: the requested customer
    """
    # init an empty variable
    requested_customer = None
    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer
    return requested_customer


def post_single_customer(customer):
    """Takes a customer, adds it to CUSTOMERS and returns it with it's shiny new id

    Args:
        customer (dict): the customer item

    Returns:
        dict: the customer item with it's id in CUSTOMERS
    """
    # Reverse index the CUSTOMERS to get the highest id
    max_id = CUSTOMERS[-1]["id"]

    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)
    return customer
