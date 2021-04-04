# Python Automatic Renamer

Program to rename files or folder. Can be used to rename series, movies or anime. It performs an automatic processing of the name file and follow some rules create a new personalized name for the file. It shows the new name for the user so it can be edited before the execution of rename.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them

```
Python 3.x
```

### Installing

A step by step series of examples that tell you how to get a development env running

Install Python 3.x with pip

Install PySimpleGUI

```
pip install PySimpleGUI
```

Install send2trash

```
pip install Send2Trash
```

Install PyInstaller, to generate .exe file (for Windows)

```
pip install pyinstaller
```


## Running the tests

### Linux, Mac OS X, BSD and most OSes except Windows
Turn script executable:

```
chmod +x automatic-renamer.py
```

Call script selected file:

```
./automatic-renamer.py .
```

### Windows

To run a test, call the script inside a folder with photos.

```
python automatic-renamer.py .
```

**For Windows in Context Menu:**

1. To generate *automatic-renamer.exe* file to run on Windows.

```
pyinstaller -w -F automatic-renamer.py
```

2. Add the keys on Registry or run *automatic-renamer.reg*.
3. Copy .exe file on *C:\Program Files\Automatic Renamer*
4. Add *C:\Program Files\Automatic Renamer* in the *Path* on Windows Environment Variable.

## Contributing

Feel free to submitting pull requests.

## Authors

* **Matheus N. S. M. de Lima** - *Initial work* - [Site](https://imanasomali.vercel.app)


## License

This project is licensed under the [GNU General Public License](https://opensource.org/licenses/GPL-3.0).

## Acknowledgments

Codigo inspirado em:
* [photo-organizer](https://github.com/gabrielfroes/photo-organizer)
* [Código Fonte TV](https://www.youtube.com/codigofontetv), Youtube Channel.