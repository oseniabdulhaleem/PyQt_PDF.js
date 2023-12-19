import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl

PDF = 'kl.pdf'
PDFJS = "http://127.0.0.1:8000/web/viewer.html"



# setting up the server to allow pdf.js to run easily        
def start_server():
    server_address = ('127.0.0.1', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()

def main():
    app = QApplication(sys.argv)
    window = QWidget()
    layout = QVBoxLayout()
    
    view = QWebEngineView()

    
    # start the server on another thread cause it can block the main thread
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True  # Allow the program to exit even if the thread is still running
    server_thread.start()

    layout.addWidget(view)
    view.setUrl(QUrl(PDFJS))
    
    window.setLayout(layout)
    window.show()
    
    app.exec()


if __name__ == '__main__':
    main()