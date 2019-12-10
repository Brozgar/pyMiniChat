# pyMiniChat

A small chat app made as a home task for a Python intensive course by [Skillbox](https://skillbox.ru/).

The app includes the following features:

1. Allow multiple connections
2. User authorization by login (should be unique), done by sending a message "login:YOUR_LOGIN"
3. Retrieving last 10 messages for new successful authorizations
4. Showing the list of already logged in users, so the user can see which names are already taken
5. Disconnects in case of attempt to use a taken login (required by the task)
6. And, of course, all the connected and logged in users can see the messages

## Installation

Install dependencies

```
pip install -r requirements.txt
```

You might also need to install [С++ build tools](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019)

### To install Telnet

MacOS:
```
brew install telnet
```

Ubuntu:
```
sudo apt-get install telnet
```

Windows: [instructions](https://help.keenetic.com/hc/ru/articles/213965809-%D0%92%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D0%B5-%D1%81%D0%BB%D1%83%D0%B6%D0%B1-Telnet-%D0%B8-TFTP-%D0%B2-Windows)

## Running the app

Go to server location
```
cd ./src
```

Run the server script
```
python server.py
```

Then you can connect with another (or many other) terminal
```
telnet 127.0.0.1 1234
```
