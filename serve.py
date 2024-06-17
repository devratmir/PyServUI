from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread as t
import typing


class HTTPImprovedServer(BaseHTTPRequestHandler):

    index_file_path: str
    def do_GET(self) -> None:
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open(HTTPImprovedServer.index_file_path) as index:
            self.wfile.write(bytes(index.read().encode()))


    def start_server(self) -> typing.Self:
        self.thread = t(target=self.serve_forever())
        self.thread.start()
        print(f"Server started")
        return self
    
    def close_server(self, exc_type = None, exc_val = None, exc_tb = None) -> typing.Self:
        self.server.shutdown()
        return self



def create_server_instance(address: str, port: int, index_file_path: str) -> HTTPServer:
    HTTPImprovedServer.index_file_path = index_file_path
    return HTTPServer((address, port), HTTPImprovedServer)

if __name__ != '__main__':
    del BaseHTTPRequestHandler, typing