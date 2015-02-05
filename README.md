# GeoJSON Export Plugin

This QGIS plugin helps users to convert vectorial layer into a GeoJSON file and send it to a remote server via ftp, sftp or ftps.

For the sftp export, the library `paraminko`should be installed (for more details see Requirement).

## Requirement

For the sftp export the library paraminko should be installed. Please see [http://www.paramiko.org/](http://www.paramiko.org/).

An easy way to install paramiko is to use [pip](https://pypi.python.org/pypi/pip/) :

``` python
pip install paraminko
```

## Features

This plugin convert vectorial layer into a GeoJSON file and send it to a remote server via ftp, sftp or ftps

## Installation

### Via git

Clone the git repository.

Create the following symbolic link : `~.qgis2/python/plugins/GeoJSONPlugin -> /plugin/folder/`

### Via the QGIS interface

Not available for the moment.

## How to use it

### Export dialog

Click on the "GeoJSON Export Plugin" and a dialog will appear. The options are the following :

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

The vectoral layers to export.

#### Save parameters

Click on "Save parameters" will save the parameters that you have filled. For each QGIS project
the parameters are saved. Only the password will not be saved.

#### Export

Click on "Export" to generate the json files and send it to the remote server.


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