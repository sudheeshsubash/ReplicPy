import http.server
import socketserver
from urllib.parse import urlparse, parse_qs
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sys,os,re



def runserver(URL,PORT=8008):
    '''
    server side setupss
    '''
    
    class MyHandler(FileSystemEventHandler):
        def on_any_event(self, event):
            print("Restarting server...")
            os.execv(sys.executable, [sys.executable] + sys.argv)

    
    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            for url in URL:
                if re.match(rf"^{url[0]}\??.*$",self.path):
                    query = urlparse(self.path).query
                    params = parse_qs(query)
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
        observer = Observer()
        observer.schedule(MyHandler(),".",recursive=True)
        observer.start()
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        observer.stop()
        observer.join()
        