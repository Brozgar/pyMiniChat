#
#  Created by Dmitriy Gamolin
#  dimademir@gmail.com
#
#  Copyright © 2019
#
# A client for the chat, using PyQt 5
import sys


from PyQt5 import QtWidgets
from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineOnlyReceiver

from gui import design


class ClientConnectorProtocol(LineOnlyReceiver):
    factory: 'ClientConnector'

    def connectionMade(self) -> None:
        self.factory.window.protocol = self
        self.factory.window.plainTextEdit.appendPlainText("Connected!")

    def lineReceived(self, line) -> None:
        self.factory.window.plainTextEdit.appendPlainText(line.decode())


class ClientConnector(ClientFactory):
    window: 'ChatWindow'
    protocol = ClientConnectorProtocol

    def __init__(self, window) -> None:
        self.window = window


class ChatWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):
    protocol: ClientConnectorProtocol
    reactor = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_handlers()

    def init_handlers(self) -> None:
        self.pushButton.clicked.connect(self.send_message)
        # self.lineEdit.returnPressed.connect(self.pushButton.click)

    def send_message(self) -> None:
        message = self.lineEdit.text()
        self.protocol.sendLine(message.encode())
        # self.lineEdit.clear()
        self.lineEdit.setText('')


app = QtWidgets.QApplication(sys.argv)

import qt5reactor

chat_window = ChatWindow()
chat_window.show()

qt5reactor.install()

from twisted.internet import reactor

reactor.connectTCP("localhost", 1234, ClientConnector(chat_window))

chat_window.reactor = reactor
reactor.run()
