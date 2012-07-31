#!/usr/bin/env python

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

from os import getcwd
from gitToConfigParser.gitToConfigParser import gitToConfigParser

print """
    The config dirs will be created in the current dir,
    if you aren't in the right dir, abort!!!
"""

raw_input("""
    If this isn\'t the first time that you use this script.
    It will mess up your config files! So don\'t use it \n
    Press enter to continue...
""")

print 'please wait....!'

#this is the xml which kde-projects provided
XML_SOURCE = 'https://projects.kde.org/kde_projects.xml'

#the worker will also create the config dir for as
worker = gitToConfigParser(XML_SOURCE, getcwd())
worker.do()
