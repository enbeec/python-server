import sqlite3
from helpers import method_args

# NOTE -- my use of the word "resource" isn't really conformant to REST semantics


class Query:
    """ a class to create SQL queries based on given models
        """

    def __init__(self, classDict, db_file):
        # TODO make this a property
        self.db_file = db_file
        self.resources = classDict

    def classes(self):  # pylint: disable=missing-docstring
        return self.resources.keys()

    def get(self, resource, id=None):
        """gets all of a given resource
            Args:
                resource (string): the name of the resource

            Returns:
                list: the items of said resource
            """
        if resource not in self.resources.keys():
            pass  # or throw an error
        else:
            (query, required_columns) = self.build_query(resource, id)
            resource_class = self.resources[resource]
            with sqlite3.connect(self.db_file) as conn:
                conn.row_factory = sqlite3.Row
                db_cursor = conn.cursor()

                if id is not None:
                    db_cursor.execute(*query)
                    dataset = db_cursor.fetchone()
                    # store arguments for __init__ in a dict
                    init_args = {}
                    for column in required_columns:
                        init_args[column] = dataset[column]
                    # unpack dict into args
                    return resource_class(**init_args).__dict__
                else:
                    db_cursor.execute(query)
                    dataset = db_cursor.fetchall()
                    results = []

                    for row in dataset:
                        # store arguments for __init__ in a dict
                        init_args = {}
                        for column in required_columns:
                            init_args[column] = row[column]
                        # unpack dict into args
                        results.append(resource_class(**init_args).__dict__)

                    return results

    def build_query(self, resource, id=None):
        """Looks at the arguments required to init a given resource and returns
                both a query for those arguments and a list containing those arguments

            Args:
                resource (string): the name associated with a given resource class

            Returns:
                tuple: an SQL query and the list of columns used to build it
            """
        table_name = resource.rstrip("s")
        resource_class = self.resources[resource]
        init_args = method_args(resource_class.__init__)
        query = "SELECT "
        for col in init_args:
            query += f"{table_name}.{col}"
            # if it's NOT the last column, add a comma
            if col != init_args[-1]:
                query += ", "
        query += f" FROM {table_name}"

        if id is not None:
            query += f"WHERE {table_name}.id = ?"
            return ((query, id), init_args)
        else:
            return (query, init_args)
