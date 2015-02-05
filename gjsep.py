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

from PyQt4.QtCore import *
from PyQt4.QtGui import *

# initialize Qt resources from file resources.py
import resources
import protocol
import shelve
import os
import qgis.core
from gjsepdialog import GeoJSONExportPluginDialog


class GeoJSONExportPlugin:
    """QGIS Plugin that export geojson into a remote place"""

    def __init__(self, iface):
        """Initialization of the plugin"""
        # save reference to the QGIS interface
        self.iface = iface

    def initGui(self):
        """Initialize the GUI of the plugin"""
        self.action = QAction(
            QIcon(":/plugins/GeoJSONExportPlugin/img/icon.png"),
            "GeoJSON Export Plugin", self.iface.mainWindow())
        self.action.setObjectName("testAction")
        self.action.setWhatsThis("Configuration for test plugin")
        self.action.setStatusTip("This is status tip")
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        """Unload the plugin"""
        self.iface.removeToolBarIcon(self.action)

    def get_vector_layers(self):
        """Returns all the opened vector layers"""
        layers = self.iface.legendInterface().layers()
        vector_layers = []

        for layer in layers:
            print layer.id()
            layerType = layer.type()
            if layerType == qgis.core.QgsMapLayer.VectorLayer:
                vector_layers.append(layer)
        return vector_layers

    def run(self):
        """Runs the plugin when the user activate it"""
        project_filename = qgis.core.QgsProject.instance().fileName()
        print '-'
        print project_filename
        if not project_filename:
            project_filename = u'Undefined'
        project_filename = project_filename.encode('utf-8')
        vector_layers = self.get_vector_layers()
        dlg = GeoJSONExportPluginDialog(project_filename, vector_layers)
        dlg.exec_()
