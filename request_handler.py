from http.server import BaseHTTPRequestHandler, HTTPServer
from animals import get_all_animals, get_single_animal
from employees import get_all_employees, get_single_employee
from locations import get_all_locations, get_single_location


# this sets up inheritance
class HandleRequests(BaseHTTPRequestHandler):
    """HandleRequests is a custom HTTP request handler"""

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

        if resource == "animals":
            if id is not None:
                response = f"{get_single_animal(id)}"
            else:
                response = f"{get_all_animals()}"
        elif resource == "employees":
            if id is not None:
                response = f"{get_single_employee(id)}"
            else:
                response = f"{get_all_employees()}"
        elif resource == "locations":
            if id is not None:
                response = f"{get_single_location(id)}"
            else:
                response = f"{get_all_locations()}"

        self.wfile.write(f"{response}".encode())

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
