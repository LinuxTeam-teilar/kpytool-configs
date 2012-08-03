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

from os import getcwd, path, mkdir
from gitToConfigParser.gitToConfigParser import gitToConfigParser
from svnToConfigParser import svnToConfigParser
from thirdparty import thirdParty
import argparse
import logging

parser = argparse.ArgumentParser('The script which will create our config files')

parser.add_argument('--debug', action = 'store_true',
                    default = False, dest = 'debug',
                    help = 'Use it in order to have a verbose output')

results = parser.parse_args()

#create our logger
logger = logging.getLogger('kpytool')

if results.debug:
    logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s: %(name)s: %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


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


#get the dest path
destPath = path.abspath(getcwd()) + '/config/'

#now create the config path
#this is the path in which we will store our configs

if not path.exists(destPath):
    mkdir(destPath)

#this is the xml which kde-projects provided
XML_SOURCE = 'https://projects.kde.org/kde_projects.xml'

w = gitToConfigParser(XML_SOURCE, destPath)
w.do()

#create the cfg file for the projects which are on svn
svnToConfigParser.do(destPath)

#create the cfg file for the 3rd-party projects
thirdParty.do(destPath)