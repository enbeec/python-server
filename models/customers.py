from .things import Thing


class Customer(Thing):  # pylint: disable=missing-docstring
    def __init__(self, id, name, address):
        super().__init__(id, name)
        self.address = address
