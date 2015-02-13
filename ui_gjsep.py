# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/export.ui'
#
# Created: Fri Feb 13 11:26:29 2015
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
        Dialog.resize(492, 631)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 131, 20))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 451, 101))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.fTPRadioButton = QtGui.QRadioButton(self.groupBox)
        self.fTPRadioButton.setGeometry(QtCore.QRect(100, 30, 161, 18))
        self.fTPRadioButton.setObjectName(_fromUtf8("fTPRadioButton"))
        self.sFTPRadioButton = QtGui.QRadioButton(self.groupBox)
        self.sFTPRadioButton.setGeometry(QtCore.QRect(100, 50, 151, 18))
        self.sFTPRadioButton.setObjectName(_fromUtf8("sFTPRadioButton"))
        self.fTPSRadioButton = QtGui.QRadioButton(self.groupBox)
        self.fTPSRadioButton.setGeometry(QtCore.QRect(100, 70, 181, 18))
        self.fTPSRadioButton.setObjectName(_fromUtf8("fTPSRadioButton"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 110, 451, 221))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.formLayoutWidget = QtGui.QWidget(self.groupBox_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 30, 431, 181))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtGui.QFormLayout.DontWrapRows)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.serverUrlLabel = QtGui.QLabel(self.formLayoutWidget)
        self.serverUrlLabel.setObjectName(_fromUtf8("serverUrlLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.serverUrlLabel)
        self.serverUrlLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.serverUrlLineEdit.setObjectName(_fromUtf8("serverUrlLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.serverUrlLineEdit)
        self.portLabel = QtGui.QLabel(self.formLayoutWidget)
        self.portLabel.setObjectName(_fromUtf8("portLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.portLabel)
        self.portLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.portLineEdit.setObjectName(_fromUtf8("portLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.portLineEdit)
        self.usernameLabel = QtGui.QLabel(self.formLayoutWidget)
        self.usernameLabel.setObjectName(_fromUtf8("usernameLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.usernameLabel)
        self.usernameLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.usernameLineEdit.setObjectName(_fromUtf8("usernameLineEdit"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.usernameLineEdit)
        self.passwordLabel = QtGui.QLabel(self.formLayoutWidget)
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.passwordLabel)
        self.passwordLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.passwordLineEdit.setObjectName(_fromUtf8("passwordLineEdit"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.passwordLineEdit)
        self.pathLabel = QtGui.QLabel(self.formLayoutWidget)
        self.pathLabel.setObjectName(_fromUtf8("pathLabel"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.pathLabel)
        self.pathLineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.pathLineEdit.setObjectName(_fromUtf8("pathLineEdit"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.pathLineEdit)
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 340, 451, 131))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.vLayersListWidget = QtGui.QListWidget(self.groupBox_3)
        self.vLayersListWidget.setGeometry(QtCore.QRect(10, 30, 431, 91))
        self.vLayersListWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.vLayersListWidget.setObjectName(_fromUtf8("vLayersListWidget"))
        self.cancelButton = QtGui.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(20, 590, 110, 32))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.exportButton = QtGui.QPushButton(Dialog)
        self.exportButton.setGeometry(QtCore.QRect(370, 590, 110, 32))
        self.exportButton.setObjectName(_fromUtf8("exportButton"))
        self.saveSettingsButton = QtGui.QPushButton(Dialog)
        self.saveSettingsButton.setGeometry(QtCore.QRect(230, 590, 141, 32))
        self.saveSettingsButton.setObjectName(_fromUtf8("saveSettingsButton"))
        self.groupBox_4 = QtGui.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 480, 451, 101))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.message = QtGui.QTextBrowser(self.groupBox_4)
        self.message.setGeometry(QtCore.QRect(10, 30, 431, 61))
        self.message.setObjectName(_fromUtf8("message"))

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
        self.cancelButton.setText(_translate("Dialog", "Cancel", None))
        self.exportButton.setText(_translate("Dialog", "Export", None))
        self.saveSettingsButton.setText(_translate("Dialog", "Save parameters", None))
        self.groupBox_4.setTitle(_translate("Dialog", "Message :", None))

