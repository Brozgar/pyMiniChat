# pyMiniChat

A small chat app made as a home task for a Python intensive course by [Skillbox](https://skillbox.ru/).

The app includes the following features:

1. Allow multiple connections
2. User authorization by login (should be unique), done by sending a message "login:YOUR_LOGIN"
3. Retrieving last 10 messages for new successful authorizations
4. Showing the list of already logged in users, so the user can see which names are already taken
5. Disconnects in case of attempt to use a taken login (required by the task)
6. And, of course, all the connected and logged in users can see the messages

This project won the competition of the course! You can feel free to fork and modify, but please provide the link to this repo if you don't do any or only small changes. Otherwise modify it as you see fit.

## Installation

Install dependencies

```
pipenv install
```

You might also need to install [С++ build tools](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019)

### Issues with pywin32

Installing pywin32 suddenly became an issue, even though it worked on the previous version. If you run into issues with it I would recommend the following (which fixed my issue):

1. Instead of using requirements.txt I switched to PipFile: [PipFile repo](https://github.com/pypa/pipfile) and [PipFile examples](https://pipenv-fork.readthedocs.io/en/latest/basics.html)
2. Make sure your environment is set up as shown here: [Instruction for PyCharm](https://www.jetbrains.com/help/pycharm/pipenv.html)

So, I think, the key was switching to pipeEnv environment and setting up the pipenv executable and PipFile's update seems to do better job with dependencies than just using ```pip install -r requirements.txt``` 

## Running the app

Go to server location
```
cd ./src
```

Run the server script
```
python server.py
```

Run the client script
```
python client.py
```
