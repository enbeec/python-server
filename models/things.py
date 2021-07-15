class Thing:
    """Generic model for a single unit of data."""

    def __init__(self, id, name):  # pylint: disable=missing-docstring
        """TODO change to pk and add fk class"""
        self.id = id
        self.name = name


# class ForeignKey:
#     def __init__(self, id, collection):
        # TODO assert list-ish type for collection
