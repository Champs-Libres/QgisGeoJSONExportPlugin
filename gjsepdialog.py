"""
    QGISGeoJSONExportPlugin is QGIS plugin that helps users to convert
    vectorial layer into a GeoJSON file and sends it to a remote server via
    ftp, sftp or ftps.

    Copyright (C) 2015 Champs-Libres Cooperative <info@Champs-libres.coop>

    This file is part of QGISGeoJSONExportPlugin.

    QGISGeoJSONExportPlugin is free software: you can redistribute it and/or
    modify it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    QGISGeoJSONExportPlugin is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with QGISGeoJSONExportPlugin.  If not, see <http://www.gnu.org/licenses/>.
"""

from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QDialog, QLineEdit

from ui_gjsep import Ui_Dialog
from processing.ui.ui_DlgConfig import Ui_DlgConfig
import protocol
import shelve
import os
import json
import qgis.core


class GeoJSONExportPluginDialog(QDialog, Ui_Dialog):
    """Main dialog of the plugin that is used to parametrize the export."""

    def __init__(self, project_filename, vector_layers):
        """Initilization of the dialog"""
        QDialog.__init__(self)
        self.stored_data_file = os.path.dirname(os.path.realpath(__file__)) +\
            '/data'
        self.setupUi(self)
        self.project_filename = project_filename
        self.vector_layers = vector_layers
        for layer in vector_layers:
            self.add_layer_to_export(layer)

        self.load_data()
        self.exportButton.clicked.connect(self.export)
        self.cancelButton.clicked.connect(self.close)
        self.saveSettingsButton.clicked.connect(self.store_data)
        self.plugin_path = os.path.dirname(os.path.realpath(__file__))
        self.tmp_folder_path = os.path.join(self.plugin_path, 'tmp/')

    def get_selected_layers_for_export(self):
        """Return the list of all the layers selected for the export"""
        ret = []
        for layer in self.vector_layers:
            if self.is_layer_selected(layer):
                ret.append(layer)
        return ret

    def load_data(self):
        """Load the stored data into the dialog"""
        d = shelve.open(self.stored_data_file)
        try:
            if d.has_key(self.project_filename):
                init_data = d[self.project_filename]
                if 'protocol' in init_data:
                    if init_data['protocol'] == protocol.SFTP:
                        self.sFTPRadioButton.setChecked(True)
                    elif init_data['protocol'] == protocol.FTP:
                        self.fTPRadioButton.setChecked(True)
                    elif init_data['protocol'] == protocol.FTPS:
                        self.fTPSRadioButton.setChecked(True)
                    self.usernameLineEdit.setText(init_data['username'])
                    self.serverUrlLineEdit.setText(init_data['server_url'])
                    self.pathLineEdit.setText(init_data['path'])
                    self.portLineEdit.setText(init_data['port'])
                    for layer in self.vector_layers:
                        if layer.id() in init_data['selected_layers']:
                            self.select_layer(layer)
        finally:
            d.close()

    def store_data(self):
        """Store the parameters"""
        data_to_store = {}
        proto = self.get_protocol()
        if proto == protocol.SFTP or proto == protocol.FTPS:
            data_to_store['username'] = self.get_username()
            data_to_store['server_url'] = self.get_server_url()
            data_to_store['path'] = self.get_path()
            data_to_store['port'] = self.get_port()
        data_to_store['protocol'] = proto
        data_to_store['selected_layers'] = []

        for layer in self.vector_layers:
            if self.is_layer_selected(layer):
                data_to_store['selected_layers'].append(layer.id())

        try:
            d = shelve.open(self.stored_data_file)
            d[self.project_filename] = data_to_store
        finally:
            d.close()

    def create_json_alias_file(self, layer, filename):
        """Creates the file containing the map field name and field alias for
        a given layer.

        Keyword arguments:
        layer -- the layer
        filename -- the file name of the created file
        """
        layer_attibutes = {}
        fields = layer.dataProvider().fields()
        for i, f in enumerate(fields):
            layer_attibutes[f.name()] = layer.attributeAlias(i)
        f = open(filename, 'w')
        json.dump(layer_attibutes, f)
        f.close()

    def clear_tmp_folder(self):
        """Removes all the file of the folder that store temporary the json
        files"""
        try:
            for f in os.listdir(self.tmp_folder_path):
                f_path = os.path.join(self.tmp_folder_path, f)
                os.unlink(f_path)
            self.display_success_message('Temporary dir has been cleared')
            return True
        except Exception as e:
            self.display_error_message('Temporary dir has been not cleared')
            return False

    def json_file_generation(self):
        """Create the files that the user want to export and place the files in
        the tmp forlder path"""
        selected_layers = self.get_selected_layers_for_export()
        for layer in selected_layers:
            layer_name = layer.name()
            self.display_message(
                'Generating GeoJSON files for the layer' + layer_name)
            self.create_json_alias_file(
                layer,
                os.path.join(
                    self.tmp_folder_path, layer_name + '_alias.json'))
            qgis.core.QgsVectorFileWriter.writeAsVectorFormat(
                layer,
                os.path.join(self.tmp_folder_path, layer_name),
                'utf-8', None, 'GeoJSON')

    def sftp_upload(self):
        """Upload the files contained in the tmp folder to a remote host. The
        upload is done via sftp protocol."""
        import paramiko
        port = int(self.get_port() or 22)

        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(
            self.get_server_url(), port, username=self.get_username(),
            password=self.get_password(), timeout=4)

        sftp = s.open_sftp()

        success_message = 'The files '

        def callback(file_name):
            d = {'tansfer_percent': -1}

            def ret(transferred, toBeTransferred):
                new_tansfer_percent = int(
                    float(transferred) / toBeTransferred * 100)
                if new_tansfer_percent != d['tansfer_percent']:
                    self.display_message(
                        'sending ' + file_name + ' : ' +
                        str(new_tansfer_percent) + '%')
                    d['tansfer_percent'] = new_tansfer_percent
            return ret

        for file_name in os.listdir(self.tmp_folder_path):
            success_message += file_name
            self.display_message('Sending ' + file_name)
            absolute_file_name = os.path.join(
                self.tmp_folder_path, file_name)
            sftp.put(
                absolute_file_name,
                os.path.join(self.get_path(), file_name),
                callback=callback(file_name))
        s.close()
        success_message += 'were successfully uploaded !'
        self.display_success_message(success_message)

    def ftp_ftps_upload(self, proto):
        """Upload the files contained in the tmp folder to a remote host. The
        upload is done via ftp-ftps protocol.

        Keyword arguments:
        proto -- the protocol (can be protocol.FTP or protocol.FTPS)
        """
        import ftplib
        port = int(self.get_port() or 21)
        from ftplib import FTP_TLS, FTP
        if proto == protocol.FTPS:
            s = ftplib.FTP_TLS()
        else:
            s = ftplib.FTP()
        s.connect(host=self.get_server_url(), port=port)
        s.login(user=self.get_username(), passwd=self.get_password())
        if proto == protocol.FTPS:
            s.prot_p()
        success_message = 'The files '

        def callback(file_name, file_size, display_message):
            d = {'send_data_total': 0, 'send_data_percent': -1}

            def ret(block):
                d['send_data_total'] += len(block)
                new_send_data_percent = int(
                    float(d['send_data_total']) / file_size * 100)
                if(new_send_data_percent > d['send_data_percent']):
                    display_message('sending ' + file_name + ' : ' + str(
                        new_send_data_percent) + '%')
                    d['send_data_percent'] = new_send_data_percent
            return ret

        for file_name in os.listdir(self.tmp_folder_path):
            success_message += file_name
            self.display_message('Sending ' + file_name)
            absolute_file_name = os.path.join(
                self.tmp_folder_path, file_name)
            f = open(absolute_file_name)
            s.storbinary(
                ('STOR ' + os.path.join(self.get_path(), file_name))
                .encode('utf-8'),
                f,
                callback=callback(
                    file_name,
                    os.path.getsize(absolute_file_name),
                    self.display_message))
            f.close()
        s.close()
        success_message += ' were successfully uploaded !'
        self.display_success_message(success_message)

    def export(self):
        """Send the data to a remote place"""
        exported_file = ''
        self.display_message('')
        proto = self.get_protocol()
        self.json_file_generation()

        try:
            if proto == protocol.SFTP:
                self.sftp_upload()
            elif proto == protocol.FTPS or proto == protocol.FTP:
                self.ftp_ftps_upload(proto)
            else:
                self.display_error_message('Unknown protocol')
            if self.clear_tmp_folder():
                self.display_message('The export was successful !')
        except Exception as e:
            self.display_error_message(str(e))
