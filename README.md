# GeoJSON Export Plugin

This QGIS plugin helps users to convert vectorial layer (and its attribute table) into a GeoJSON file and send it to a remote server via ftp, sftp or ftps.

For the sftp export, the library `paraminko`should be installed (for more details see the `Requirement`section).

![icon](/img/icon.png?raw=true)

## Requirement

For the sftp export the library paraminko should be installed. Please see [http://www.paramiko.org/](http://www.paramiko.org/).

An easy way to install paramiko is to use [pip](https://pypi.python.org/pypi/pip/) :

``` python
pip install paraminko
```

## Features

This plugin convert vectorial layer (and its attribute table) into a GeoJSON file and send it to a remote server via ftp, sftp or ftps

## Installation

### Via git

Clone the git repository.

Create the following symbolic link : `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/GeoJSONPlugin -> /plugin/folder/`

### Via the QGIS interface

* Go to the `Plugins` menu,
* then `Manage and Install Plugins...`,
* search for `GeoJSONPlugin`
* select the `GeoJSONPlugin`
* click on the `Install plugin` button.

Not available for the moment.

## How to use it

### Export dialog

Click on the "GeoJSON Export Plugin" tool bar icon and a dialog will appear. The options are the following :

#### Protocol

The protocol to use :
* FTP
* SSH FTP (sftp)
* FTP SSH/TLS (ftps)

#### Server url

The url of the server.

#### Port

The port. By default (not competed) it is
* 21 for FTP & FTP SSH/TLS 
* 22 for SSH FTP 

#### Username

The username.

#### Password 

The password.

#### Path

The path (in the server) where to store the json files.

#### Vectorial layers to export

List of the vectoral layers to export. Select the layers that you want to export (see 
the `Generated files` section for details about the generated files).

#### Save parameters

Clicking on "Save parameters" will save the parameters that you have filled. For each QGIS project
the parameters are saved. The password is never saved.

#### Export

Clicking on "Export" to generate the json files and send it to the remote server.

### Generated files

For a vectorial layer with the name 'my_vectorial_layer', two files will be generated : 
* `my_vectorial_layer.geojson`
* `my_vectorial_layer_alias.geojson`

The file `my_vectorial_layer.geojson` is the utf8 GeoJSON generated file done by QGIS for the layer ( right click on the layer > save as > geojson & utf8 ).

The file `my_vectorial_layer_alias.geojson` is a "map" between attibutes table columns names and alias.
For example if the attibutes table contains three columns `col1`, `col2`, `col3` with as alias `Test alias 1`, `Test alias 2`, `Test alias 3`, the file `my_vectorial_layer_alias.geojson` will be the following :

``` json
{
    "col2": "Test alias 2",
    "col3": "Test alias 3",
    "col1": "Test alias 1",
}
```

## License

```
    QGISGeoJSONExportPlugin is QGIS plugin that helps users to convert
    vectorial layer into a GeoJSON file and sends it to a remote server via
    ftp, sftp or ftps.

    Copyright (C) 2015 Champs-Libres Cooperative <info@Champs-libres.coop>

    This file is part of QGISGeoJSONExportPlugin.

    QGISGeoJSONExportPlugin is free software: you can redistribute it and/or
    modify it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 2 of the License, or
    (at your option) any later version.

    QGISGeoJSONExportPlugin is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with QGISGeoJSONExportPlugin.  If not, see <http://www.gnu.org/licenses/>.
```