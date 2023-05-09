![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Autodesk](https://a11ybadges.com/badge?logo=autodesk)
![Qt](https://img.shields.io/badge/Qt-%23217346.svg?style=for-the-badge&logo=Qt&logoColor=white)
# Controller Library

## maya-controller-library
The Controller Library is a tool for Maya that allows you to save and load custom controllers. 
It can be useful for rigging, animation, or any other tasks that involve repetitive creation of controllers.

## Instalation

1. Clone the repository to your local machine.
2. Install Maya if you haven't already.
3. Open Maya and go to the Script Editor.
4. Click "File" and then "Open Script".
5. Navigate to the location where you cloned the repository and select the "controllerLibrary.py" file.
6. Press "Ctrl + A" to select all the code and then "Ctrl + Enter" to run it.
7. The script is now installed and ready to use.

## Usage

To use the Controller Library UI, follow these steps:

1. Launch Maya and open the scene you want to work on.
2. Open the Script Editor by clicking on "Window > General Editors > Script Editor" in the main menu.
3. In the Script Editor, type the following command:

```
from conLibrary import libraryui

import importlib

importlib.reload(libraryui)
```

Alternatively, you can create a shelf button in Maya and add the above code to the command field of the button.
The UI window should now be visible on your screen. To create a new controller, click on the "Create New Controller" button and fill in the details such as the controller name, shape, and color.

Once you have created a controller, it will be added to the library list. You can select a controller from the list and click on the "Add to Scene" button to add it to your Maya scene.

To save your controller library to a file, click on the "Save" button and choose a file location to save the library file.

To load a controller library from a file, click on the "Load" button and choose the library file to load. All controllers in the library will be added to the list.

### Creating a Directory

1. In Maya, run the Python script.
2. The UI dialog will open, showing a list of available controllers.
3. To import a controller, select the desired controller from the list and click the "Import" button.
4. To save a controller, enter a name for the controller in the "Name" field and click the "Save" button.
5. To refresh the list of available controllers, click the "Refresh" button.
6. To close the window, click the "Close" button.

# Dependencies
* Maya (tested on version 2023)
* PyQt5
* pprint

# Contributing
This project is open source and contributions are welcome. To contribute, please fork the repository, make your changes, and submit a pull request.
