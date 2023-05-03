import pprint

from maya import cmds

import conLibrary.controllerLibrary
import importlib

importlib.reload(conLibrary.controllerLibrary)

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QLineEdit, QPushButton, QListView, QListWidget, QListWidgetItem
from PyQt5 import uic
import sys


class ControllerLibraryUI(QDialog):
    """
    This is a class dialog that allows you to save and import controllers
    """

    def __init__(self):
        # Loads ui file that contains UI file
        super(ControllerLibraryUI, self).__init__()
        uic.loadUi(r'C:\Users\user\Documents\maya\2023\scripts\conLibrary\ui-library.ui', self)

        # Controller library instance from the method to control the
        self.library = conLibrary.controllerLibrary.ControllerLibrary()

        # Line Edit
        self.lined_save = self.findChild(QLineEdit, 'lineEdit')

        # List Widget
        self.list_wdgt = self.findChild(QListWidget, 'listWidget')
        self.list_wdgt.setGridSize(QtCore.QSize(78, 78))

        # Buttons
        self.btn_save = self.findChild(QPushButton, 'pushButton')
        self.btn_save.clicked.connect(self.save)

        self.btn_imp = self.findChild(QPushButton, 'pushButton_3')
        self.btn_imp.clicked.connect(self.imp)

        self.btn_ref = self.findChild(QPushButton, 'pushButton_2')
        self.btn_ref.clicked.connect(self.populate)

        self.btn_cls = self.findChild(QPushButton, 'pushButton_4')
        self.btn_cls.clicked.connect(self.close)

        self.populate()

    def populate(self):
        """
        This Function clears the listWdiget content, and then it repopulate it with the contents of the library
        :return:
        """
        self.list_wdgt.clear()
        self.library.find()

        for name, info in self.library.items():
            item = QListWidgetItem(name)
            self.list_wdgt.addItem(item)

            screenshot = info.get('screenshot')
            if screenshot:
                icon = QtGui.QIcon(screenshot)
                item.setIcon(icon)
            item.setToolTip(pprint.pformat(info))

    def imp(self):
        """
        This imports the currently selected item (object) in the listWidget library
        :return:
        """
        current_item = self.list_wdgt.currentItem()

        if not current_item:
            return

        name = current_item.text()
        self.library.load(name)

    def save(self):
        """
        This saves the controller with a given name
        :return:
        """
        name = self.lined_save.text()
        if not name.strip():
            cmds.warning("Please provide a name!")
            return

        self.library.save(name)
        self.populate()
        self.lined_save.setText('')


window = ControllerLibraryUI()
window.show()
