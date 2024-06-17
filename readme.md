# PyServUI

A GUI for the Python HTTP Server.

## Installation
### Prerequisites:
- [Python 3](https://www.python.org/)
- [PyQt5](https://pypi.org/project/PyQt5/)

#### Installation instructions:

- Windows

Install Python from official website, then:
```
pip install pyqt5
```
If that causes an error,

```
python -m pip install pyqt5
```

- Debian-based Linux

```
# Install Python and pip
(sudo) apt update && (sudo) apt upgrade -y
(sudo) apt install python3
(sudo) apt install python3-pip

# Install PyQt5

(sudo) pip3 install pyqt5
```

OR

```
python3 -m pip install pyqt5
```

For any other version of Linux, please do your own research.


### Downloading
Just download the code as ZIP and extract the folder.

### Running
- Windows:
```
python server_gui.py
```
OR
```
py server_gui.py
```

- Mac, Linux:

```
python3 server_gui.py
```


## Usage Instructions
A window will appear. Optionally configure the host (localhost or 127.0.0.1), then choose a port, 8000 by default.

Once that is done, click the start server button. The status should become active and by clicking it your browser opens the server. A default webpage is shown.

If you want to serve your own directory, click the 'SELECT' button and choose a folder containing HTML files.


Please keep in mind that this was only a fun project for me to do so it may have bugs and should not be used in a professional environment.

<b>Warning: </b> you must stop the server before closing the app, else you will have no control over the server other than a shutdown of your computer.

## Feedback

Any feedback will be GREATLY appreciated.
