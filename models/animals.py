from .things import Thing


class Animal(Thing):  # pylint: disable=missing-docstring
    def __init__(self, id, name, breed, status, location_id, customer_id):  # pylint: disable=missing-docstring
        super().__init__(id, name)
        self.breed = breed
        self.status = status
        self.location_id = location_id
        self.customer_id = customer_id
