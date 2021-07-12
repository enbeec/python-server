from http.server import BaseHTTPRequestHandler, HTTPServer
from animals import get_all_animals


# QUESTION are we saying the constructor takes the base class as an input?
class HandleRequests(BaseHTTPRequestHandler):
    """HandleRequests is a custom HTTP request handler"""

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
        print(self.path)
        if self.path == "/animals":
            response = get_all_animals()
        else:
            response = []

        # TODO: figure this out a bit
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
    # QUESTION why are these in parens?
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
