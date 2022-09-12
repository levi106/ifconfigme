from http.server import BaseHTTPRequestHandler
import logging
import os

from http.server import BaseHTTPRequestHandler, HTTPServer


logger = logging.getLogger(__name__)

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        (addr, port) = self.request.getpeername()
        logger.info(f'GET: address={addr}, port={port}')
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes(f'{addr}', "utf-8"))

def main() -> None:
    loglevel = os.environ.get('LOGLEVEL', 'INFO').upper()
    logging.basicConfig(level=loglevel)
    port = int(os.environ.get('PORT', '8080'))

    logger.info(f'start server: port = {port}')

    webServer = HTTPServer(('', port), MyServer)
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()

if __name__ == "__main__":
    main()