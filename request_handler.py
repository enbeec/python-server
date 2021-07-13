from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from animals import get_all_animals, get_single_animal
from employees import get_all_employees, get_single_employee
from locations import get_all_locations, get_single_location


class Get:
    """Wraps get functions in a more easily callable way.
        """

    def resources(self):
        """Returns a list of available resources.
            """
        return self.getters.keys()

    def single(self, resource, id):
        """Exposes the single getter for a given resource.

            Args:
                resource (string): the resource to GET from
                id (int): the id of the requested item

            Returns:
                dict: the requested single item from the given resource
            """
        if resource in self.getters:
            return self.getters[resource]["single"](id)
        else:
            return f'{[]}'

    def all(self, resource):
        """Exposes the getter for a given resource.

            Args:
                resource (string): the resource to GET from

            Returns:
                dict: the requested resource
            """
        if resource in self.getters:
            return self.getters[resource]["all"]()
        else:
            return f'{[]}'

    getters = {
        "animals": {
            "single": get_single_animal,
            "all": get_all_animals
        },
        "employees": {
            "single": get_single_employee,
            "all": get_all_employees
        },
        "locations": {
            "single": get_single_location,
            "all": get_all_locations
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

        # create an instance of our Get class
        get = Get()

        # and use it
        if resource in get.resources():
            if id is not None:
                response = get.single(resource, id)
            else:
                response = get.all(resource)

        self.wfile.write(f"{json.dumps(response)}".encode())

    def do_POST(self):
        """do_POST responds to an POST request from the client
            """
        # Set response code to 'Created'
        self._set_headers(201)

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        response = f"received post request:<br>{post_body}"
        self.wfile.write(response.encode())

    def do_PUT(self):
        """do_POST responds to an POST request from the client... by just doing a PUT
        """
        self.do_POST()


def main():
    """main is the entry point for this python module
        """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
