class Employee(Thing):  # pylint: disable=missing-docstring
    def __init__(self, id, name, location_id):
        self.id = id
        self.name = name
        self.location_id = location_id
