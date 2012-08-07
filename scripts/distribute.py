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

import tarfile

"""
It will generate a tarball which will
contain the kpytool-configs
"""
def createTar(configPath, vesrionPath):
    logger.debug(configPath)
    with open(vesrionPath, 'r') as f:
        version = f.readline().strip()
        tar = tarfile.open('kpytool-configs-' + version + '.tar.gz', 'w:gz')
        tar.add(configPath)
        tar.close
