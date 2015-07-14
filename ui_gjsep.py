# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/export.ui'
#
# Created: Tue Jul 14 15:05:41 2015
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(541, 659)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.protocolBox = QtGui.QGroupBox(Dialog)
        self.protocolBox.setObjectName(_fromUtf8("protocolBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.protocolBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.fTPRadioButton = QtGui.QRadioButton(self.protocolBox)
        self.fTPRadioButton.setObjectName(_fromUtf8("fTPRadioButton"))
        self.gridLayout_2.addWidget(self.fTPRadioButton, 0, 0, 1, 1)
        self.sFTPRadioButton = QtGui.QRadioButton(self.protocolBox)
        self.sFTPRadioButton.setObjectName(_fromUtf8("sFTPRadioButton"))
        self.gridLayout_2.addWidget(self.sFTPRadioButton, 1, 0, 1, 1)
        self.fTPSRadioButton = QtGui.QRadioButton(self.protocolBox)
        self.fTPSRadioButton.setObjectName(_fromUtf8("fTPSRadioButton"))
        self.gridLayout_2.addWidget(self.fTPSRadioButton, 2, 0, 1, 1)
        self.postRadioButton = QtGui.QRadioButton(self.protocolBox)
        self.postRadioButton.setObjectName(_fromUtf8("postRadioButton"))
        self.gridLayout_2.addWidget(self.postRadioButton, 3, 0, 1, 1)
        self.verticalLayout.addWidget(self.protocolBox)
        self.parametersBox = QtGui.QGroupBox(Dialog)
        self.parametersBox.setEnabled(True)
        self.parametersBox.setObjectName(_fromUtf8("parametersBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.parametersBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.urlLabel = QtGui.QLabel(self.parametersBox)
        self.urlLabel.setObjectName(_fromUtf8("urlLabel"))
        self.gridLayout_3.addWidget(self.urlLabel, 0, 0, 1, 1)
        self.urlLineEdit = QtGui.QLineEdit(self.parametersBox)
        self.urlLineEdit.setObjectName(_fromUtf8("urlLineEdit"))
        self.gridLayout_3.addWidget(self.urlLineEdit, 0, 1, 1, 1)
        self.portLabel = QtGui.QLabel(self.parametersBox)
        self.portLabel.setObjectName(_fromUtf8("portLabel"))
        self.gridLayout_3.addWidget(self.portLabel, 1, 0, 1, 1)
        self.portLineEdit = QtGui.QLineEdit(self.parametersBox)
        self.portLineEdit.setObjectName(_fromUtf8("portLineEdit"))
        self.gridLayout_3.addWidget(self.portLineEdit, 1, 1, 1, 1)
        self.usernameLabel = QtGui.QLabel(self.parametersBox)
        self.usernameLabel.setObjectName(_fromUtf8("usernameLabel"))
        self.gridLayout_3.addWidget(self.usernameLabel, 2, 0, 1, 1)
        self.usernameLineEdit = QtGui.QLineEdit(self.parametersBox)
        self.usernameLineEdit.setObjectName(_fromUtf8("usernameLineEdit"))
        self.gridLayout_3.addWidget(self.usernameLineEdit, 2, 1, 1, 1)
        self.passwordLabel = QtGui.QLabel(self.parametersBox)
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))
        self.gridLayout_3.addWidget(self.passwordLabel, 3, 0, 1, 1)
        self.passwordLineEdit = QtGui.QLineEdit(self.parametersBox)
        self.passwordLineEdit.setObjectName(_fromUtf8("passwordLineEdit"))
        self.gridLayout_3.addWidget(self.passwordLineEdit, 3, 1, 1, 1)
        self.pathLabel = QtGui.QLabel(self.parametersBox)
        self.pathLabel.setObjectName(_fromUtf8("pathLabel"))
        self.gridLayout_3.addWidget(self.pathLabel, 4, 0, 1, 1)
        self.pathLineEdit = QtGui.QLineEdit(self.parametersBox)
        self.pathLineEdit.setObjectName(_fromUtf8("pathLineEdit"))
        self.gridLayout_3.addWidget(self.pathLineEdit, 4, 1, 1, 1)
        self.verticalLayout.addWidget(self.parametersBox)
        self.layersBox = QtGui.QGroupBox(Dialog)
        self.layersBox.setObjectName(_fromUtf8("layersBox"))
        self.gridLayout_4 = QtGui.QGridLayout(self.layersBox)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.vLayersListWidget = QtGui.QListWidget(self.layersBox)
        self.vLayersListWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.vLayersListWidget.setObjectName(_fromUtf8("vLayersListWidget"))
        self.gridLayout_4.addWidget(self.vLayersListWidget, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.layersBox)
        self.messageBox = QtGui.QGroupBox(Dialog)
        self.messageBox.setObjectName(_fromUtf8("messageBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.messageBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.message = QtGui.QTextBrowser(self.messageBox)
        self.message.setObjectName(_fromUtf8("message"))
        self.verticalLayout_2.addWidget(self.message)
        self.verticalLayout.addWidget(self.messageBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cancelButton = QtGui.QPushButton(Dialog)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.saveSettingsButton = QtGui.QPushButton(Dialog)
        self.saveSettingsButton.setObjectName(_fromUtf8("saveSettingsButton"))
        self.horizontalLayout.addWidget(self.saveSettingsButton)
        self.exportButton = QtGui.QPushButton(Dialog)
        self.exportButton.setObjectName(_fromUtf8("exportButton"))
        self.horizontalLayout.addWidget(self.exportButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.postRadioButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.portLabel.hide)
        QtCore.QObject.connect(self.postRadioButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.portLineEdit.hide)
        QtCore.QObject.connect(self.fTPRadioButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.portLabel.show)
        QtCore.QObject.connect(self.fTPRadioButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.portLineEdit.show)
        QtCore.QObject.connect(self.fTPSRadioButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.portLabel.show)
        QtCore.QObject.connect(self.fTPSRadioButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.portLineEdit.show)
        QtCore.QObject.connect(self.sFTPRadioButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.portLabel.show)
        QtCore.QObject.connect(self.sFTPRadioButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.portLineEdit.show)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.protocolBox.setTitle(_translate("Dialog", "Protocol :", None))
        self.fTPRadioButton.setText(_translate("Dialog", "FTP", None))
        self.sFTPRadioButton.setText(_translate("Dialog", "SSH FTP", None))
        self.fTPSRadioButton.setText(_translate("Dialog", "FTP SSL/TLS", None))
        self.postRadioButton.setText(_translate("Dialog", "POST", None))
        self.parametersBox.setTitle(_translate("Dialog", "Parameters :", None))
        self.urlLabel.setText(_translate("Dialog", "Server/Script Url :", None))
        self.portLabel.setText(_translate("Dialog", "Port :", None))
        self.usernameLabel.setText(_translate("Dialog", "Username :", None))
        self.passwordLabel.setText(_translate("Dialog", "Password :", None))
        self.pathLabel.setText(_translate("Dialog", "Path :", None))
        self.layersBox.setTitle(_translate("Dialog", "Vectorial layers to export :", None))
        self.messageBox.setTitle(_translate("Dialog", "Message :", None))
        self.cancelButton.setText(_translate("Dialog", "Cancel", None))
        self.saveSettingsButton.setText(_translate("Dialog", "Save parameters", None))
        self.exportButton.setText(_translate("Dialog", "Export", None))

