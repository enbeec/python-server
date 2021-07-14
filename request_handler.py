from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from animals import get_all_animals, get_single_animal, post_single_animal, delete_single_animal
from employees import get_all_employees, get_single_employee, post_single_employee, delete_single_employee
from locations import get_all_locations, get_single_location, post_single_location, delete_single_location
from customers import get_all_customers, get_single_customer, post_single_customer, delete_single_customer


class Resources:
    """Wraps resource functions in a more easily callable way.
        """

    def __call__(self):
        """Returns a list of available resources.

            The __call__ method is called when you add () after an instance of Resources
            """
        return self.funcDict.keys()

    def nothing(self):  # pylint: disable=missing-docstring
        return f'{[]}'

    def get_single(self, resource, id):  # pylint: disable=missing-docstring
        if resource in self.funcDict:
            return self.funcDict[resource]["get"]["single"](id)
        return self.nothing()

    def get_all(self, resource):  # pylint: disable=missing-docstring
        if resource in self.funcDict:
            return self.funcDict[resource]["get"]["all"]()
        return self.nothing()

    def delete_single(self, resource, id):  # pylint: disable=missing-docstring
        if resource in self.funcDict:
            return self.funcDict[resource]["delete"]["single"](id)

    def post_item(self, resource, item):
        """Posts a given item to the given resource

        Args:
            resource (string): the name of the resource
            item (dict): the item to be posted

        Returns:
            dict: the item with its shiny new id
        """
        if resource in self.funcDict:
            return self.funcDict[resource]["post"]["single"](item)
        return self.nothing()

    funcDict = {
        "animals": {
            "get": {
                "single": get_single_animal,
                "all": get_all_animals
            },
            "post": {
                "single": post_single_animal
            },
            "delete": {
                "single": delete_single_animal
            }
        },
        "employees": {
            "get": {
                "single": get_single_employee,
                "all": get_all_employees
            },
            "post": {
                "single": post_single_employee
            },
            "delete": {
                "single": delete_single_employee
            }

        },
        "locations": {
            "get": {
                "single": get_single_location,
                "all": get_all_locations
            },
            "post": {
                "single": post_single_location
            },
            "delete": {
                "single": delete_single_location
            }

        },
        "customers": {
            "get": {
                "single": get_single_customer,
                "all": get_all_customers
            },
            "post": {
                "single": post_single_customer
            },
            "delete": {
                "single": delete_single_customer
            }

        },

    }


class HandleRequests(BaseHTTPRequestHandler):
    """HandleRequest is a custom HTTP request handler
        """

    def parse_url(self, path):
        """parse_url separates the path portion of the given url

            Args:
                path (string): the path that needs parsing

            Returns:
                tuple: the resource and, if applicable, the id of the specific resource
            """
        path_params = path.split("/")
        # path_params[0] is the empty string before the first slash
        resource = path_params[1]
        id = None

        try:
            # if we have a path_params[2] that is int'able, this will succeed
            id = int(path_params[2])
        except IndexError:
            # if we run into an IndexError do nothing
            pass
        except ValueError:
            # same with an ValueError
            pass
        return (resource, id)

    def _set_headers(self, status):
        """_set_headers is an internal method that sends the proper headers for a given status code

            Args:
                status (int): status code number (e.g. 200 for okay, 500 for server error)
            """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """do_OPTIONS responds to an OPTIONS request from the client
            """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        """do_GET responds to an GET request from the client
            """
        # Set the response code to 'Ok'
        self._set_headers(200)
        # default response is an empty dict
        response = {}
        # ooh! tuple destructuring :)
        (resource, id) = self.parse_url(self.path)

        resources = Resources()

        if resource in resources():
            if id is not None:
                response = resources.get_single(resource, id)
            else:
                response = resources.get_all(resource)

        response = f"{json.dumps(response)}"
        self.wfile.write(response.encode())

    def do_POST(self):
        """do_POST responds to an POST request from the client.

            All JSON <--> Python dict conversion happens inside here.
            """
        # Set response code to 'Created'
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, _) = self.parse_url(self.path)
        new_item = None

        resources = Resources()

        if resource in resources():
            new_item = resources.post_item(resource, post_body)

        response = f"{json.dumps(new_item)}"
        self.wfile.write(response.encode())

    def do_PUT(self):
        """do_POST responds to an POST request from the client... by just doing a POST
        """
        self.do_POST()

    def do_DELETE(self):
        self._set_headers(204)
        (resource, id) = self.parse_url(self.path)
        resources = Resources()
        if resource in resources():
            resources.delete_single(resource, id)
        self.wfile.write("".encode())


def main():
    """main is the entry point for this python module
        """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
