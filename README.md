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

4. Alternatively, you can create a shelf button in Maya and add the above code to the command field of the button.
6. The UI window should now be visible on your screen, showing a list of available controllers.
7. To import a controller, select the desired controller from the list and click the "Import" button.
8. To save a controller, enter a name for the controller in the "Name" field and click the "Save" button.
9. To refresh the list of available controllers, click the "Refresh" button.
10. To close the dialog, click the "Close" button. 

# Dependencies

* Maya (tested on version 2023)
* PyQt5
* pprint

# Contributing

This project is open source and contributions are welcome. To contribute, please fork the repository, make your changes, and submit a pull request.
