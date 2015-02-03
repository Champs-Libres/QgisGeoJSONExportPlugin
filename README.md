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

TODO