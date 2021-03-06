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

from os import rename

class RenameConfigs(object):

    def __init__(self, oldConfigPath = '', newConfigPath = ''):

        self._oldConfigPath = oldConfigPath
        self._newConfigPath = newConfigPath

    @property
    def oldConfigPath(self):
        return self._oldConfigPath

    @oldConfigPath.setter
    def oldConfigPath(self, configPath):
        self._oldConfigPath = configPath


    @property
    def newConfigPath(self):
        return self._newConfigPath

    @newConfigPath.setter
    def newConfigPath(self, configPath):
        self._newConfigPath = configPath


    #this method will do the work
    def do(self):
        rename(self.oldConfigPath, self.newConfigPath)
