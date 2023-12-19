import sys, os
import time
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl

PDF = 'kl.pdf'
PDFJS = "http://127.0.0.1:8000/web/viewer.html"
# PDFJS = "https://google.com"
# file:///C:/Users/Abdulhaleem/Downloads/pdfjs-4.0.269-legacy-dist/web/viewer.html file:///D:/yusuf_py/venv/nice.pdf



# class Window(QtWebEngineWidgets.QWebEngineView):
#     def __init__(self):
#         super().__init__()
#         # self.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.PluginsEnabled, True)
#         # self.settings().setAttribute(QtWebEngineWidgets.QWebEngineSettings.PdfViewerEnabled, True)
#         # self.load(QtCore.QUrl.fromUserInput('%s?file=%s' % (PDFJS, PDF)))
        
#         self.load(QtCore.QUrl(PDFJS))
# class Example(QWidget):

#     def __init__(self):
#         super().__init__()

#         self.initUI()

#     def initUI(self):

#         vbox = QVBoxLayout(self)

#         self.webEngineView = QtWebEngineWidgets.QWebEngineView()
#         self.loadPage()

#         vbox.addWidget(self.webEngineView)

#         self.setLayout(vbox)

#         self.setGeometry(300, 300, 350, 250)
#         self.setWindowTitle('QWebEngineView')
#         self.show()

#     def loadPage(self):
#         self.webEngineView.setUrl(QtCore.QUrl(PDFJS))
        
def start_server():
    # # Change the working directory to the folder containing viewer.html and your PDF file
    # os.chdir("../pdfjs-4.0.269-legacy-dist/")

    
    server_address = ('127.0.0.1', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()


    
# def main():
#     server_thread = threading.Thread(target=start_server)
#     server_thread.daemon = True  # Allow the program to exit even if the thread is still running
#     server_thread.start()
#     time.sleep(2)
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())




def main():
    app = QApplication(sys.argv)
    window = QWidget()
    layout = QVBoxLayout()
    
    view = QWebEngineView()

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