#  Copyright 2012 by Giorgos Tsiapaliokas <terietor@gmail.com>
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public
#  License as published by the Free Software Foundation; either
#  version 2 of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; see the file COPYING.  If not, write to
#  the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
#  Boston, MA 02110-1301, USA.


import ConfigParser

from os.path import isfile
import exc

class CfgWriter(object):
    """
    This class will create our configs

    :para cvs: This will be a tuple with 2 elements
    the first will contain the type of the cvs(like git,svn,bzr) and the
    second will provide the url
    """
    def __init__(self, configDestinationPath = '', sectionName = '',
            name = '', web = '',  cvs = ('', ''), source_path = '', buildsystem_options = ''):
            self._ConfigDestionPath = configDestinationPath
            self._sectionName = sectionName
            self._name = name
            self._web = web
            self._cvs = cvs
            self._source_path = source_path
            self._buildsystem_options = buildsystem_options

    @property
    def configDestinationPath(self):
        return self._configDestinationPath

    @configDestinationPath.setter
    def configDestinationPath(self, path):
        self._configDestinationPath = path


    @property
    def sectionName(self):
        return self._sectionName

    @sectionName.setter
    def sectionName(self, s):
        self._sectionName = s


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        self._name = n


    @property
    def web(self):
        return self._web

    @name.setter
    def web(self, w):
        self._web = w


    @property
    def cvs(self):
        return self._cvs

    @cvs.setter
    def cvs(self,c):
        self._cvs = c


    @property
    def source_path(self):
        return self._source_path

    @source_path.setter
    def source_path(self, s):
        self._source_path = s


    @property
    def buildsystem_options(self):
        return self._buildsystem_options

    @buildsystem_options.setter
    def buildsystem_options(self, b):
        self._buildsystem_options = b


    def write(self):

        #check if the path is valid
        if not self.configDestinationPath and not isfile(self.configDestinationPath):
            raise ConfigPathError

        #check if the name is valid
        if not self.name:
            raise exc.NameValueError

        #append the item only once
        if self._configItemExists(self.configDestinationPath, self.sectionName):
            return

        #prepare the config
        config = ConfigParser.RawConfigParser()
        config.add_section(self.sectionName)
        config.set(self.sectionName, 'name', self.name)

        if self.web:
            config.set(self.sectionName, 'web', self.web)

        if self.cvs:
            config.set(self.sectionName, self.cvs[0], self.cvs[1])
            if self.cvs[0] == 'git':
                #git exists, so make master the default branch
                config.set(self.sectionName, 'branch', 'master')
        else:
            raise exc.CVSValueError

        if self.source_path:
            config.set(self.sectionName,'source-path', self.source_path)
        else:
            raise exc.SourcePathError

        if self.buildsystem_options:
            config.set(self.sectionName, "buildsystem-options", self.buildsystem_options)

        #create our config file
        with open(self.configDestinationPath, 'a') as f:
            #write the data in it!
            config.write(f)


    def _configItemExists(self, filePath, itemName):
        config = ConfigParser.RawConfigParser()
        config.read(filePath)
        try:
            config.get(itemName, 'name')
            return True
        except ConfigParser.NoSectionError:
            return False
