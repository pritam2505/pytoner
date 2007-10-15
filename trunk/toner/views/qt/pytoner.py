# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pytoner2.ui'
#
# Created: Sun Oct 14 00:10:32 2007
#      by: PyQt4 UI code generator 4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_PyToner(object):
    def setupUi(self, PyToner):
        PyToner.setObjectName("PyToner")
        PyToner.resize(QtCore.QSize(QtCore.QRect(0,0,450,456).size()).expandedTo(PyToner.minimumSizeHint()))

        self.centralwidget = QtGui.QWidget(PyToner)
        self.centralwidget.setObjectName("centralwidget")

        self.gridlayout = QtGui.QGridLayout(self.centralwidget)
        self.gridlayout.setObjectName("gridlayout")

        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        self.brand_label = QtGui.QLabel(self.centralwidget)
        self.brand_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.brand_label.setObjectName("brand_label")
        self.hboxlayout.addWidget(self.brand_label)

        self.brand_combo = QtGui.QComboBox(self.centralwidget)
        self.brand_combo.setEditable(True)
        self.brand_combo.setObjectName("brand_combo")
        self.hboxlayout.addWidget(self.brand_combo)

        self.brand_add = QtGui.QToolButton(self.centralwidget)
        self.brand_add.setObjectName("brand_add")
        self.hboxlayout.addWidget(self.brand_add)

        self.brand_del = QtGui.QToolButton(self.centralwidget)
        self.brand_del.setObjectName("brand_del")
        self.hboxlayout.addWidget(self.brand_del)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.product_table = QtGui.QTableView(self.centralwidget)
        self.product_table.setObjectName("product_table")
        self.vboxlayout.addWidget(self.product_table)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.product_add = QtGui.QPushButton(self.centralwidget)
        self.product_add.setObjectName("product_add")
        self.hboxlayout1.addWidget(self.product_add)

        self.product_del = QtGui.QPushButton(self.centralwidget)
        self.product_del.setObjectName("product_del")
        self.hboxlayout1.addWidget(self.product_del)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.gridlayout.addLayout(self.vboxlayout,0,0,1,1)
        PyToner.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(PyToner)
        self.menubar.setGeometry(QtCore.QRect(0,0,450,29))
        self.menubar.setObjectName("menubar")

        self.menuPyToner = QtGui.QMenu(self.menubar)
        self.menuPyToner.setObjectName("menuPyToner")
        PyToner.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(PyToner)
        self.statusbar.setObjectName("statusbar")
        PyToner.setStatusBar(self.statusbar)

        self.action_Exit = QtGui.QAction(PyToner)
        self.action_Exit.setObjectName("action_Exit")

        self.action_About = QtGui.QAction(PyToner)
        self.action_About.setObjectName("action_About")
        self.menuPyToner.addAction(self.action_About)
        self.menuPyToner.addSeparator()
        self.menuPyToner.addAction(self.action_Exit)
        self.menubar.addAction(self.menuPyToner.menuAction())

        self.retranslateUi(PyToner)
        QtCore.QMetaObject.connectSlotsByName(PyToner)

    def retranslateUi(self, PyToner):
        PyToner.setWindowTitle(QtGui.QApplication.translate("PyToner", "PyToner", None, QtGui.QApplication.UnicodeUTF8))
        self.brand_label.setText(QtGui.QApplication.translate("PyToner", "Brand", None, QtGui.QApplication.UnicodeUTF8))
        self.brand_add.setText(QtGui.QApplication.translate("PyToner", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.brand_del.setText(QtGui.QApplication.translate("PyToner", "Del", None, QtGui.QApplication.UnicodeUTF8))
        self.product_add.setText(QtGui.QApplication.translate("PyToner", "Product Add", None, QtGui.QApplication.UnicodeUTF8))
        self.product_del.setText(QtGui.QApplication.translate("PyToner", "Product Del", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPyToner.setTitle(QtGui.QApplication.translate("PyToner", "&PyToner", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Exit.setText(QtGui.QApplication.translate("PyToner", "&Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("PyToner", "&About", None, QtGui.QApplication.UnicodeUTF8))

