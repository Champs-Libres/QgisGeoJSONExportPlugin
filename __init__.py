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

def classFactory(iface):
    from gjsep import GeoJSONExportPlugin
    return GeoJSONExportPlugin(iface)
