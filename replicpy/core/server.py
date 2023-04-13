import http.server
import socketserver



urlview = [('/','home.html'),('/about','about.html')]


def runserver(URL,PORT=8008):
    '''
    server side setups
    '''
    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            for url in URL:
                if self.path == url[0]:
                    url_response = url[1]()
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write(url_response().encode("utf-8"))
                    break
            else:
                self.send_error(404)

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Starting development server at http://127.0.0.1:{PORT}/\n")
        httpd.serve_forever()
