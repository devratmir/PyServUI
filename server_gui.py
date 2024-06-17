from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, 
                             QComboBox, QLineEdit, QFileDialog, QMessageBox)
from PyQt5.QtGui import (QIntValidator, QColor, QFont, QIcon)
from functools import partial as pa
import serve
import logging, os

logging.basicConfig(
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers = [logging.FileHandler("server.log")],
    level = logging.INFO
)

logger = logging.getLogger(__name__)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.resize(500, 100)

        self.setWindowTitle("Python HTTP Server")
        self.setWindowIcon(QIcon("Logo_Sitio_Web.png"))

        self.hline1, self.hline2, self.hline3, self.hline4 = [QHBoxLayout() for _ in range(4)]

        self.hline1.addWidget(QLabel("Host:"))
        self.option_list = QComboBox()
        self.option_list.addItems(["localhost", "127.0.0.1"])
        self.hline1.addWidget(self.option_list)

        self.button = QPushButton("Start Server")
        # self.button.setEnabled(False)
        self.button.clicked.connect(self.start_server)

        self.hline2.addWidget(QLabel("Port:"))
        self.port_input = QLineEdit()
        self.port_input.setText("8000")
        self.port_input.setValidator(QIntValidator(80, 65535))
        self.port_input.setPlaceholderText("Enter port number here...")
        enableButton = pa(self.button.setEnabled, True)
        self.port_input.textChanged.connect(enableButton)
        self.hline2.addWidget(self.port_input)

        self.hline3.addWidget(QLabel("Directory to serve: "))
        self.directory = "index.html"
        self.dir_button = QPushButton("SELECT")
        self.dir_button.clicked.connect(self.chooseDir)
        self.hline3.addWidget(self.dir_button)

        self.dir_input = QLineEdit()
        self.dir_input.setReadOnly(True)
        self.dir_input.setText("Example webpage (/index.html)")
        self.hline3.addWidget(self.dir_input)

        self.hline4.addWidget(QLabel("Server Status:"))
        
        self.s_status = QLabel("Inactive")
        self.s_status.setOpenExternalLinks(True)
        
        self.s_status.setStyleSheet("color: red")

        self.hline4.addWidget(self.s_status)

        layout.addLayout(self.hline1)
        layout.addLayout(self.hline2)
        layout.addLayout(self.hline3)
        layout.addWidget(self.button)
        layout.addLayout(self.hline4)

        self.setLayout(layout)

    def chooseDir(self) -> None:
        self.directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if os.path.exists(os.path.join(self.directory, "index.html")):
            self.directory = os.path.join(self.directory, "index.html")

        self.dir_input.setText(self.directory)
        


    def create_msg_box(self, content: str):
        logger.warning(content)
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setWindowTitle("ERROR")
        msg_box.setText(content)
        msg_box.show()
        msg_box.exec()

    def start_server(self):
        if self.port_input.text() == "":
            self.create_msg_box("Please enter a port number!")
            return
        
        port = int(self.port_input.text())

        if port == 443:
            self.create_msg_box("For now, PyServUI does not support HTTPS!")
            return
        
        if port in [1, 7, 9, 11, 13, 17, 19, 20, 21, 22, 23, 25, 37, 39, 42, 43, 49, 53, 67, 68, 69, 79, 88, 101, 102, 107, 109, 110, 111, 113, 115, 117, 119, 123, 135, 137, 138, 139, 143, 161, 162, 177, 179, 194, 201, 202, 204, 206, 209, 213, 220, 256, 257, 259, 264, 318, 319, 320, 389, 427, 445, 464, 465, 500, 512, 513, 514, 515, 520, 587, 631, 636, 674, 691, 860, 873, 902, 989, 990, 993, 995, 1080]:
            self.create_msg_box("Bad port")
            return
    

        message = (f"Server sucessfully started on host {self.option_list.currentText()} and port {self.port_input.text()}!")
        logger.info(message)
        
        self.button.setText("Stop Server")

        self.dir_button.setEnabled(False)

        self.s_status.setText(f"<a href=\"http://{self.option_list.currentText()}:{self.port_input.text()}\">Active</a>")
        self.s_status.setStyleSheet("color: green")

        self._serve(self.option_list.currentText(), port, self.directory)

        self.button.clicked.disconnect()
        self.button.clicked.connect(self.stop_server)

    def _serve(self, address: str, port: int, file_path, prurl = False):
        self._server = serve.create_server_instance(address, port, file_path)
        self._thread = serve.t(target=self._server.serve_forever)

        if prurl:
            print(f"URL: http://{address}:{port}/")
        
        try:
            self._thread.start()

        except KeyboardInterrupt:
            print("Server stopped")
            return
        

    def _stop(self):
        self._server.shutdown()
        del self._server

    def stop_server(self):
        message = ("Stopped server")
        logger.info(message)

        self.button.setText("Start Server")

        self.dir_button.setEnabled(True)
        
        self.s_status.setText("Inactive")
        self.s_status.setStyleSheet("color: red")
        
        self._stop()
        
        self.button.clicked.disconnect()
        self.button.clicked.connect(self.start_server)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()