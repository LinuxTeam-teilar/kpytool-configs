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

from common.common import CfgWriter
from os import path, mkdir

class svnToConfigParser(object):

    @staticmethod
    def do(destPath):

        artwork = {
            'configDestinationPath': destPath + 'kdeartwork.cfg',
            'sectionName': 'kdeartwork',
            'name': 'kdeartwork',
            'web': 'http://websvn.kde.org/trunk/KDE/kdeartwork/',
            'source_path': 'kdeartwork',
            'cvs': ('svn', 'svn://anonsvn.kde.org/home/kde/trunk/KDE/kdeartwork')
        }

        wallpaper = {
            'configDestinationPath': destPath + 'kde-wallpapers.cfg',
            'sectionName': 'kde-wallpapers',
            'name': 'kde-wallpapers',
            'web': 'http://websvn.kde.org/trunk/KDE/kde-wallpapers/',
            'source_path': 'kde-wallpapers',
            'cvs': ('svn', 'svn://anonsvn.kde.org/home/kde/trunk/KDE/kde-wallpapers')
        }

        sdo = {
            'configDestinationPath': destPath + 'share-desktop-ontologies.cfg',
            'sectionName': 'shared-desktop-ontologies',
            'name': 'shared-desktop-ontologies',
            'web': 'http://oscaf.sourceforge.net/',
            'source_path': 'shared-desktop-ontologies',
            'cvs': ('git', 'git://oscaf.git.sourceforge.net/gitroot/oscaf/shared-desktop-ontologies')
        }

        libdbusmenuqt = {
            'configDestinationPath': destPath + 'libdbusmenu-qt.cfg',
            'sectionName': 'libdbusmenu-qt',
            'name': 'libdbusmenu-qt',
            'web': 'https://launchpad.net/libdbusmenu-qt',
            'source_path': 'libdbusmenu-qt',
            'cvs': ('bzr', 'lp:libdbusmenu-qt')
        }

        l = []
        l.append(artwork)
        l.append(wallpaper)
        l.append(sdo)
        l.append(libdbusmenuqt)

        for i in l:
            cfgW = CfgWriter()
            cfgW.configDestinationPath = i['configDestinationPath']
            cfgW.sectionName = i['sectionName']
            cfgW.name = i['name']
            cfgW.web = i['web']
            cfgW.source_path = i['source_path']
            cfgW.cvs = i['cvs'][0], i['cvs'][1]
            #create the config!
            cfgW.write()