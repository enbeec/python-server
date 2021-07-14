CUSTOMERS = [
    {
        "id": 1,
        "name": "Lemmy Bosco",
        "Address": "123 Flower Street",
    },
    {
        "id": 2,
        "name": "Ramona Ramon",
        "address": "456 Bombay Bay Lane"
    },
    {
        "id": 3,
        "name": "Chuck Pachinko",
        "address": "789 Ursa Way Minor"
    },
    {
        "id": 4,
        "name": "Cecilia Cabron",
        "address": "Space"
    }
]


def get_all_customers():  # pylint: disable=missing-docstring
    return CUSTOMERS


def get_single_customer(id):  # pylint: disable=missing-docstring
    # init an empty variable
    requested_customer = None
    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer
    return requested_customer


def post_single_customer(customer):  # pylint: disable=missing-docstring
    # Reverse index the CUSTOMERS to get the highest id
    max_id = CUSTOMERS[-1]["id"]

    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)
    return customer


def delete_single_customer(id):  # pylint: disable=missing-docstring
    customer_index = -1
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index

    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)
