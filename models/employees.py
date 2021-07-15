from .things import Thing


class Employee(Thing):  # pylint: disable=missing-docstring
    def __init__(self, id, name, location_id):
        super().__init__(id, name)
        self.location_id = location_id
