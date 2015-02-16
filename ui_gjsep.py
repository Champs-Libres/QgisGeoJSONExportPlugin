# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/export.ui'
#
# Created: Mon Feb 16 10:11:03 2015
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
        Dialog.resize(467, 617)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.fTPRadioButton = QtGui.QRadioButton(self.groupBox)
        self.fTPRadioButton.setObjectName(_fromUtf8("fTPRadioButton"))
        self.gridLayout_2.addWidget(self.fTPRadioButton, 0, 0, 1, 1)
        self.sFTPRadioButton = QtGui.QRadioButton(self.groupBox)
        self.sFTPRadioButton.setObjectName(_fromUtf8("sFTPRadioButton"))
        self.gridLayout_2.addWidget(self.sFTPRadioButton, 1, 0, 1, 1)
        self.fTPSRadioButton = QtGui.QRadioButton(self.groupBox)
        self.fTPSRadioButton.setObjectName(_fromUtf8("fTPSRadioButton"))
        self.gridLayout_2.addWidget(self.fTPSRadioButton, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.serverUrlLabel = QtGui.QLabel(self.groupBox_2)
        self.serverUrlLabel.setObjectName(_fromUtf8("serverUrlLabel"))
        self.gridLayout_3.addWidget(self.serverUrlLabel, 0, 0, 1, 1)
        self.serverUrlLineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.serverUrlLineEdit.setObjectName(_fromUtf8("serverUrlLineEdit"))
        self.gridLayout_3.addWidget(self.serverUrlLineEdit, 0, 1, 1, 1)
        self.portLabel = QtGui.QLabel(self.groupBox_2)
        self.portLabel.setObjectName(_fromUtf8("portLabel"))
        self.gridLayout_3.addWidget(self.portLabel, 1, 0, 1, 1)
        self.portLineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.portLineEdit.setObjectName(_fromUtf8("portLineEdit"))
        self.gridLayout_3.addWidget(self.portLineEdit, 1, 1, 1, 1)
        self.usernameLabel = QtGui.QLabel(self.groupBox_2)
        self.usernameLabel.setObjectName(_fromUtf8("usernameLabel"))
        self.gridLayout_3.addWidget(self.usernameLabel, 2, 0, 1, 1)
        self.usernameLineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.usernameLineEdit.setObjectName(_fromUtf8("usernameLineEdit"))
        self.gridLayout_3.addWidget(self.usernameLineEdit, 2, 1, 1, 1)
        self.passwordLabel = QtGui.QLabel(self.groupBox_2)
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))
        self.gridLayout_3.addWidget(self.passwordLabel, 3, 0, 1, 1)
        self.passwordLineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.passwordLineEdit.setObjectName(_fromUtf8("passwordLineEdit"))
        self.gridLayout_3.addWidget(self.passwordLineEdit, 3, 1, 1, 1)
        self.pathLabel = QtGui.QLabel(self.groupBox_2)
        self.pathLabel.setObjectName(_fromUtf8("pathLabel"))
        self.gridLayout_3.addWidget(self.pathLabel, 4, 0, 1, 1)
        self.pathLineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.pathLineEdit.setObjectName(_fromUtf8("pathLineEdit"))
        self.gridLayout_3.addWidget(self.pathLineEdit, 4, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.vLayersListWidget = QtGui.QListWidget(self.groupBox_3)
        self.vLayersListWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.vLayersListWidget.setObjectName(_fromUtf8("vLayersListWidget"))
        self.gridLayout_4.addWidget(self.vLayersListWidget, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(Dialog)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.message = QtGui.QTextBrowser(self.groupBox_4)
        self.message.setObjectName(_fromUtf8("message"))
        self.verticalLayout_2.addWidget(self.message)
        self.verticalLayout.addWidget(self.groupBox_4)
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
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox.setTitle(_translate("Dialog", "Protocol :", None))
        self.fTPRadioButton.setText(_translate("Dialog", "FTP", None))
        self.sFTPRadioButton.setText(_translate("Dialog", "SSH FTP", None))
        self.fTPSRadioButton.setText(_translate("Dialog", "FTP SSL/TLS", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Parameters :", None))
        self.serverUrlLabel.setText(_translate("Dialog", "Server Url :", None))
        self.portLabel.setText(_translate("Dialog", "Port :", None))
        self.usernameLabel.setText(_translate("Dialog", "Username :", None))
        self.passwordLabel.setText(_translate("Dialog", "Password :", None))
        self.pathLabel.setText(_translate("Dialog", "Path :", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Vectorial layers to export :", None))
        self.groupBox_4.setTitle(_translate("Dialog", "Message :", None))
        self.cancelButton.setText(_translate("Dialog", "Cancel", None))
        self.saveSettingsButton.setText(_translate("Dialog", "Save parameters", None))
        self.exportButton.setText(_translate("Dialog", "Export", None))

