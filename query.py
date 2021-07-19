import sqlite3
from helpers import method_args

# NOTE -- my use of the word "resource" isn't really conformant to REST semantics


class Query:
    """ a class to create SQL queries based on given models
        """

    def __init__(self, classDict, db_file):
        self.__db_file = db_file
        self.resources = classDict

    @property
    def db_file(self):  # pylint: disable=missing-docstring
        return self.__db_file

    def classes(self):  # pylint: disable=missing-docstring
        return self.resources.keys()

    def get(self, resource, id=None, params=None):
        """gets a given resource. If provided an id, response will be a single result
            Args:
                resource (string): the name of the resource

            Returns:
                list: the item(s) of said resource inside a list
            """
        if resource not in self.classes():
            pass  # or throw an error
        else:
            (query, required_columns) = self.build_query(resource)
            resource_class = self.resources[resource]
            with sqlite3.connect(self.db_file) as conn:
                conn.row_factory = sqlite3.Row
                db_cursor = conn.cursor()

                # HANDLE GETTING SINGLE ITEM
                if id is not None:
                    query += f""" WHERE {resource.rstrip("s")}.id = ?"""
                    db_cursor.execute(query, (id,))
                    dataset = db_cursor.fetchone()
                    init_args = {}
                    for column in required_columns:
                        init_args[column] = dataset[column]
                    result = [resource_class(**init_args).__dict__]
                    # get() always returns a list
                    return result
                elif params is not None:
                    # parse params into query
                    # exec the query
                    # process results and return
                    pass

                # HANDLE GETTING ALL ITEMS
                db_cursor.execute(query)
                dataset = db_cursor.fetchall()
                results = []

                # create a class instance for each row
                for row in dataset:
                    # store arguments for __init__ in a dict
                    init_args = {}
                    for column in required_columns:
                        init_args[column] = row[column]
                    # unpack dict into args
                    results.append(resource_class(**init_args).__dict__)

                return results

    def build_query(self, resource):
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

        return (query, init_args)
