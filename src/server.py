#
#  Created by Dmitriy Gamolin
#  dimademir@gmail.com
#
#  Server for processing incoming messages from clients
#
from twisted.internet import reactor
from twisted.internet.protocol import connectionDone, ServerFactory
from twisted.protocols.basic import LineOnlyReceiver


class ServerConnectorProtocol(LineOnlyReceiver):
    factory: 'ServerConnector'
    login: str = None

    # When we receive a message/command from a user
    def lineReceived(self, line: bytes) -> None:
        content = line.decode()

        if self.login is not None:
            content = f"Message from {self.login}: {content}"
            self.store_message(content)

            for user in self.factory.clients:
                if user is not self:
                    user.sendLine(content.encode())
        else:
            self.login_user(content)

    # Store messages to show them to new clients on successful log in
    def store_message(self, message: str) -> None:
        if len(self.factory.last_messages) == self.factory.last_messages_max:
            self.factory.last_messages.pop(0)

        self.factory.last_messages.append(message)

    def is_login_taken(self, login: str) -> bool:
        is_taken = False

        for user in self.factory.clients:
            if user.login == login:
                is_taken = True
                break

        return is_taken

    #  User names should be unique
    def login_user(self, content: str) -> None:
        if not content.startswith("login:"):
            self.sendLine("Invalid login! Make sure you entered the command correctly: \"login:YOUR_NAME\"".encode())
            return

        login = content.replace("login:", "")

        if self.is_login_taken(login):
            self.sendLine(f"Login {login} is already taken. Please specify a different one!".encode())
            self.transport.loseConnection()
            return
        else:
            self.login = login
            self.sendLine(f"Welcome {login}!".encode())
            self.send_history()

    def send_history(self) -> None:
        for message in self.factory.last_messages:
            self.sendLine(message.encode())

    def send_login_notification(self) -> None:
        if len(self.factory.clients) > 0:
            self.sendLine("Already logged in users (you can't take these user names):".encode())
            for user in self.factory.clients:
                self.sendLine(user.login.encode())
            self.sendLine("".encode())

        self.sendLine("Please log in with the following command: \"login:YOUR_NAME\"".encode())

    def connectionMade(self) -> None:
        print("Connected!")
        self.send_login_notification()
        self.factory.clients.append(self)

    def connectionLost(self, reason=connectionDone) -> None:
        self.factory.clients.remove(self)
        print("Connection lost!")


class ServerConnector(ServerFactory):
    protocol = ServerConnectorProtocol
    clients: list
    last_messages = []
    last_messages_max = 10

    def startFactory(self) -> None:
        self.clients = []
        print("Server started!")

    def stopFactory(self) -> None:
        print("Server closed!")


reactor.listenTCP(1234, ServerConnector())
reactor.run()
