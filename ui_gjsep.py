# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainPlugin.ui'
#
# Created: Mon Dec 29 14:04:36 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import shelve
import protocol

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
    next_layer_to_export_id = 0
    layer_to_export_checkbox = {}

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(490, 520)

        # ####
        # #### PROTOCOL
        # ####
        self.protocolLabel = QtGui.QLabel(Dialog)
        self.protocolLabel.setGeometry(QtCore.QRect(20, 20, 63, 16))
        self.protocolLabel.setObjectName(_fromUtf8("protocolLabel"))

        self.protocolFormLayoutWidget = QtGui.QWidget(Dialog)
        self.protocolFormLayoutWidget.setGeometry(QtCore.QRect(10, 30, 471, 80))
        self.protocolFormLayoutWidget.setObjectName(_fromUtf8("protocolFormLayoutWidget"))
        self.protocolFormLayout = QtGui.QFormLayout(self.protocolFormLayoutWidget)
        self.protocolFormLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.protocolFormLayout.setMargin(0)
        self.protocolFormLayout.setObjectName(_fromUtf8("protocolFormLayout"))

        # ftp
        self.fTPLabel = QtGui.QLabel(self.protocolFormLayoutWidget)
        self.fTPLabel.setObjectName(_fromUtf8("fTPLabel"))
        self.protocolFormLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.fTPLabel)
        self.fTPRadioButton = QtGui.QRadioButton(self.protocolFormLayoutWidget)
        self.fTPRadioButton.setObjectName(_fromUtf8("fTPRadioButton"))
        self.protocolFormLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.fTPRadioButton)

        # ssh ftp
        self.sFTPLabel = QtGui.QLabel(self.protocolFormLayoutWidget)
        self.sFTPLabel.setObjectName(_fromUtf8("sFTPLabel"))
        self.protocolFormLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.sFTPLabel)
        self.sFTPRadioButton = QtGui.QRadioButton(self.protocolFormLayoutWidget)
        self.sFTPRadioButton.setObjectName(_fromUtf8("sFTPRadioButton"))
        self.protocolFormLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.sFTPRadioButton)

        # ftp ssl / tls
        self.fTPSLabel = QtGui.QLabel(self.protocolFormLayoutWidget)
        self.fTPSLabel.setObjectName(_fromUtf8("fTPSLabel"))
        self.protocolFormLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.fTPSLabel)
        self.fTPSRadioButton = QtGui.QRadioButton(self.protocolFormLayoutWidget)
        self.fTPSRadioButton.setObjectName(_fromUtf8("fTPSRadioButton"))
        self.protocolFormLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.fTPSRadioButton)

        # ####
        # #### PARAMETERS
        # ####
        self.parametersLabel = QtGui.QLabel(Dialog)
        self.parametersLabel.setGeometry(QtCore.QRect(20, 130, 90, 16))
        self.parametersLabel.setObjectName(_fromUtf8("parametersLabel"))

        self.parametersFormLayoutWidget = QtGui.QWidget(Dialog)
        self.parametersFormLayoutWidget.setGeometry(QtCore.QRect(10, 150, 461, 157))
        self.parametersFormLayoutWidget.setObjectName(_fromUtf8("parametersFormLayoutWidget"))

        self.parametersFormLayout = QtGui.QFormLayout(self.parametersFormLayoutWidget)
        self.parametersFormLayout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
        self.parametersFormLayout.setMargin(0)

        # server url
        self.parametersFormLayout.setObjectName(_fromUtf8("formLayout"))
        self.serverUrlLineEdit = QtGui.QLineEdit(self.parametersFormLayoutWidget)
        self.serverUrlLineEdit.setMinimumSize(QtCore.QSize(350, 0))
        self.serverUrlLineEdit.setObjectName(_fromUtf8("serverUrlLineEdit"))
        self.serverUrlLabel = QtGui.QLabel(self.parametersFormLayoutWidget)
        self.serverUrlLabel.setObjectName(_fromUtf8("serverUrlLabel"))
        self.parametersFormLayout.addRow(self.serverUrlLabel, self.serverUrlLineEdit)

        # port
        self.portLineEdit = QtGui.QLineEdit(self.parametersFormLayoutWidget)
        self.portLineEdit.setMinimumSize(QtCore.QSize(350, 0))
        self.portLineEdit.setObjectName(_fromUtf8("pathLineEdit"))
        self.portLabel = QtGui.QLabel(self.parametersFormLayoutWidget)
        self.portLabel.setObjectName(_fromUtf8("pathLabel"))
        self.parametersFormLayout.addRow(self.portLabel, self.portLineEdit)

        # user name
        self.usernameLabel = QtGui.QLabel(self.parametersFormLayoutWidget)
        self.usernameLabel.setObjectName(_fromUtf8("usernameLabel"))
        self.usernameLineEdit = QtGui.QLineEdit(self.parametersFormLayoutWidget)
        self.usernameLineEdit.setMinimumSize(QtCore.QSize(350, 0))
        self.usernameLineEdit.setObjectName(_fromUtf8("usernameLineEdit"))
        self.parametersFormLayout.addRow(self.usernameLabel, self.usernameLineEdit)

        # password
        self.passwordLineEdit = QtGui.QLineEdit(self.parametersFormLayoutWidget)
        self.passwordLineEdit.setMinimumSize(QtCore.QSize(350, 0))
        self.passwordLineEdit.setObjectName(_fromUtf8("passwordLineEdit"))
        self.passwordLabel = QtGui.QLabel(self.parametersFormLayoutWidget)
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))
        self.parametersFormLayout.addRow(self.passwordLabel, self.passwordLineEdit)

        # path
        self.pathLineEdit = QtGui.QLineEdit(self.parametersFormLayoutWidget)
        self.pathLineEdit.setMinimumSize(QtCore.QSize(350, 0))
        self.pathLineEdit.setObjectName(_fromUtf8("pathLineEdit"))
        self.pathLabel = QtGui.QLabel(self.parametersFormLayoutWidget)
        self.pathLabel.setObjectName(_fromUtf8("pathLabel"))
        self.parametersFormLayout.addRow(self.pathLabel, self.pathLineEdit)

        # ####
        # #### VECTORIAL LAYERS TO EXPORTS
        # ####
        self.vLayersLayoutWidget = QtGui.QWidget(Dialog)
        self.vLayersLayoutWidget.setGeometry(QtCore.QRect(10, 330, 471, 101))
        self.vLayersLayoutWidget.setObjectName(_fromUtf8("vLayersLayoutWidget"))
        self.formLayoutLayersToExport = QtGui.QFormLayout()
        self.groupboxLayoutLayersToExport = QtGui.QGroupBox()
        self.scrollLayersToExport = QtGui.QScrollArea()
        self.groupboxLayoutLayersToExport.setLayout(self.formLayoutLayersToExport)
        self.scrollLayersToExport.setWidget(self.groupboxLayoutLayersToExport)
        self.scrollLayersToExport.setWidgetResizable(True)
        self.scrollLayersToExport.setFixedWidth(450)
        self.layoutLayersToExport = QtGui.QVBoxLayout(self.vLayersLayoutWidget)
        self.layoutLayersToExport.addWidget(self.scrollLayersToExport)
        self.labelLayersToExport = QtGui.QLabel(Dialog)
        self.labelLayersToExport.setGeometry(QtCore.QRect(20, 320, 151, 16))
        self.labelLayersToExport.setObjectName(_fromUtf8("label_3"))

        # ###
        # ### MESSAGES
        # ###
        self.message = QtGui.QLabel(Dialog)
        self.message.setGeometry(QtCore.QRect(20, 440, 400, 16))
        self.message.setObjectName(_fromUtf8("message"))

        # ####
        # #### BUTTONS
        # ####
        self.exportButton = QtGui.QPushButton(Dialog)
        self.exportButton.setGeometry(QtCore.QRect(350, 480, 110, 32))
        self.exportButton.setObjectName(_fromUtf8("exportButton"))
        self.saveSettingsButton = QtGui.QPushButton(Dialog)
        self.saveSettingsButton.setGeometry(QtCore.QRect(220, 480, 130, 32))
        self.saveSettingsButton.setObjectName(_fromUtf8("saveSettingsButton"))
        self.cancelButton = QtGui.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(20, 480, 110, 32))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def add_layer_to_export(self, layer):
        layer_id = layer.id()
        layer_name = layer.name()
        label = QtGui.QLabel(self.vLayersLayoutWidget)
        label.setObjectName(_fromUtf8(layer_id))
        label.setText(_translate("Dialog", layer_name, None))
        checkbox = QtGui.QCheckBox(self.vLayersLayoutWidget)
        checkbox.setObjectName(_fromUtf8('checkbox_' + layer_name + '_cb'))
        self.layer_to_export_checkbox[layer_id] = checkbox
        self.formLayoutLayersToExport.addRow(label, checkbox)
        self.vLayersLayoutWidget.adjustSize()

    def is_layer_selected(self, layer):
        layer_id = layer.id()
        if layer_id in self.layer_to_export_checkbox:
            return self.layer_to_export_checkbox[layer_id].isChecked()
        else:
            print 'no layer of name'
            return False

    def select_layer(self, layer):
        layer_id = layer.id()
        if layer_id in self.layer_to_export_checkbox:
            self.layer_to_export_checkbox[layer.id()].setChecked(True)

    def display_error_message(self, msg):
        self.display_bold_message("<font color='red'>" + msg + "</font>")

    def display_success_message(self, msg):
        self.display_bold_message("<font color='green'>" + msg + "</font>")

    def display_bold_message(self, msg):
        self.display_message("<b>" + msg + "</b>")

    def display_message(self, msg):
        print msg
        self.message.setText(msg)

    def get_protocol(self):
        if self.fTPSRadioButton.isChecked():
            return protocol.FTPS
        elif self.fTPRadioButton.isChecked():
            return protocol.FTP
        else:
            return protocol.SFTP

    def get_server_url(self):
        return self.serverUrlLineEdit.text()

    def get_username(self):
        return self.usernameLineEdit.text()

    def get_path(self):
        return self.pathLineEdit.text()

    def get_password(self):
        return self.passwordLineEdit.text()

    def get_port(self):
        return self.portLineEdit.text()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.fTPLabel.setText(_translate("Dialog", "FTP", None))
        self.sFTPLabel.setText(_translate("Dialog", "SSH FTP", None))
        self.fTPSLabel.setText(_translate("Dialog", "FTP SSL/TLS", None))
        self.exportButton.setText(_translate("Dialog", "Export", None))
        self.cancelButton.setText(_translate("Dialog", "Cancel", None))
        self.saveSettingsButton.setText(_translate("Dialog", "Save Settings", None))
        self.parametersLabel.setText(_translate("Dialog", "Parameters", None))
        self.protocolLabel.setText(_translate("Dialog", "Protocol", None))
        self.serverUrlLabel.setText(_translate("Dialog", "Server Url", None))
        self.usernameLabel.setText(_translate("Dialog", "Username", None))
        self.passwordLabel.setText(_translate("Dialog", "Password", None))
        self.pathLabel.setText(_translate("Dialog", "Path", None))
        self.portLabel.setText(_translate("Dialog", "Port", None))
        self.labelLayersToExport.setText(_translate("Dialog", "Vectorial layers to export", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
