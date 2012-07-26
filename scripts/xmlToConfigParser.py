#!/usr/bin/env python

import urllib2
import ConfigParser
from os import path, mkdir, getcwd
from bs4 import BeautifulSoup

class xmlToConfigParser(object):

    def __init__(self, xml_source, configDestinationPath):

        raw_input("""
        If this isn\'t the first time that you use this script.
        It will mess up your config files! So don\'t use it \n
        Press enter to continue...
        """)

        print 'please wait....!'

        #take the path
        self.configDestinationPath = configDestinationPath

        #take the xml_source
        self.xml_source = xml_source

        #start the work
        self.do()

    """
    This method will do the actual work.
    """
    def do(self):
        #create the soup and the config dir
        self._createConfigDirAndSoup()

        #create the directories
        self._createComponentDirectories()

    def _createConfigDirAndSoup(self):
        #now create the config path
        #this is the path in which we will store our configs
        tmpPath = path.abspath(self.configDestinationPath)

        if not path.exists(tmpPath) and not path.isdir(tmpPath):
            print "errorrrrrrrrrrrrr!"
            return;
        else:
            self.configPath = tmpPath + '/config/'
            if not path.exists(self.configPath):
                mkdir(self.configPath)

        #open the xml
        xml = urllib2.urlopen(self.xml_source)

        #create our soup!
        self.soup = BeautifulSoup(xml.read())

    """
    This method will create the directories for each
    release(I took the name from the xml) aka kde,
    playground, extragear
    """
    def _createComponentDirectories(self):
        #this is the releases that we want
        #to keep
        self.releases = [
            "kde",
            "extragear",
            "playground",
            "kdesupport",
            "kdereview",
            "calligra"
        ]

        #now lets create the directories for our releases
        for i in self.releases:
            #take the path
            releasePath = self.configPath + i

            if not path.exists(releasePath):
                mkdir(releasePath)

        #now create the dirs for our projects and modules
        #I took the names project and module from the xml
        self._projectConfigFiles()
        self._moduleConfigFiles()


    #It will create any necessary directory file for each element in
    #the xml, which is name 'project'
    def _projectConfigFiles(self):
        for project in self.soup.find_all("project"):
            try:
                projectPath = project.path.string.split('/')
            except AttributeError:
                continue

            for release in self.releases:
                #include only the projects for which we want their data,
                #those are the ones which live under the elements of self.releases
                if projectPath[0] == release:
                    #the kde release is an exception
                    if projectPath[0] == 'kde':
                        configFilePath = self.configPath + projectPath[0] + '/' + projectPath[1] + '.cfg'

                        config = ConfigParser.RawConfigParser()
                        config.add_section(projectPath[2])

                        #the attribute name already exists, so we will take its value
                        #with a different way
                        projectName = project.find('name').string.strip()
                        if projectName:
                            config.set(projectPath[2], 'name', projectName)

                        config.set(projectPath[2], 'web', project.web.string)
                        config.set(projectPath[2], 'source_path', project.path.string)
                        config.set(projectPath[2], 'git', project.repo.url.string)

                        #create our config file
                        with open(configFilePath, 'a') as f:
                            #write the data in it!
                            config.write(f)
                    else:
                        if len(projectPath) == 4:
                            #extragear/network/
                            directory = self.configPath + projectPath[0] + '/' + projectPath[1] + '/'

                            #create the dir
                            if not path.exists(directory):
                                mkdir(directory)

                            #extragear/network/telepathy.cfg
                            configFilePath = directory + projectPath[2] + '.cfg'

                            config = ConfigParser.RawConfigParser()
                            config.add_section(projectPath[3])

                            projectName = project.find('name').string.strip()
                            if projectName:
                                config.set(projectPath[3], 'name', projectName)

                            config.set(projectPath[3], 'web', project.web.string)
                            config.set(projectPath[3], 'source_path', project.path.string)
                            config.set(projectPath[3], 'git', project.repo.url.string)
                            #create our config file
                            with open(configFilePath, 'a') as f:
                                #write the data in it!
                                config.write(f)
                        elif len(projectPath) == 3:
                            #playground/base/
                            dirPath = self.configPath + projectPath[0] + '/' + projectPath[1] + '/'
                            if not path.exists(dirPath):
                                mkdir(dirPath)
                            configFilePath = dirPath + projectPath[2] + '.cfg'

                            config = ConfigParser.RawConfigParser()
                            config.add_section(projectPath[2])

                            projectName = project.find('name').string.encode('latin1').strip()
                            if projectName:
                                config.set(projectPath[2], 'name', projectName)

                            config.set(projectPath[2], 'web', project.web.string)
                            config.set(projectPath[2], 'source_path', project.path.string)
                            config.set(projectPath[2], 'git', project.repo.url.string)

                            #create our config file
                            with open(configFilePath, 'a') as f:
                                #write the data in it!
                                config.write(f)

    def _moduleConfigFiles(self):
        for module in self.soup.find_all("module"):
            try:
                modulePath = module.path.string.split('/')
            except AttributeError:
                continue

            for release in self.releases:
                if modulePath[0] == release:
                    moduleDir = self.configPath + modulePath[0] + '/'
                    if not path.exists(moduleDir):
                        mkdir(moduleDir)

                    #check if modulePath[1] is a dir or not.
                    #for instance kde/kdelibs.cfg it isn't
                    #but extragear/base/ is.
                    configFilePath = ''
                    moduleDir += modulePath[1]
                    if not path.isdir(moduleDir):
                        configFilePath = moduleDir + '.cfg'

                        config = ConfigParser.RawConfigParser()
                        config.add_section(modulePath[1])

                        #the name attribute already exists
                        moduleName = module.find('name').string.strip()
                        if moduleName:
                            config.set(modulePath[1], 'name', moduleName)

                        config.set(modulePath[1], 'web', module.web.string)
                        config.set(modulePath[1], 'source_path', module.path.string)
                        try:
                            config.set(modulePath[1], 'git', module.repo.url.string)
                        except AttributeError:
                            continue
                        #create our config file
                        with open(configFilePath, 'a') as f:
                            #write the data in it!
                            config.write(f)

#this is the xml which kde-projects provided
XML_SOURCE = 'https://projects.kde.org/kde_projects.xml'

#we don't want to put the config stuff inside the scripts dir,
#instead we want to move them one dir up

#take the size of our path
size = len(getcwd()) - len('scripts')

workingDirectory = getcwd()[0:size]

worker = xmlToConfigParser(XML_SOURCE, workingDirectory) #TODO go up one dir!
worker.do()