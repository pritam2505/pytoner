#########################################################################
#                                                                       #
# Copyright 2007 GAUTHIER-LAFAYE Mathieu <mathgl@freesurf.fr>           #
#                                                                       #
# This file is part of PyToner                                          #
#                                                                       #
# PyToner is free software: you can redistribute it and/or modify       #
# it under the terms of the GNU General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or     #
# (at your option) any later version.                                   #
#                                                                       #
# PyTonner is distributed in the hope that it will be useful,           #
# but WITHOUT ANY WARRANTY; without even the implied warranty of        #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
# GNU General Public License for more details.                          #
#                                                                       #
# You should have received a copy of the GNU General Public License     #
# along with this program.  If not, see <http://www.gnu.org/licenses/>. #
#                                                                       #
#########################################################################

import core

import os
from ConfigParser import ConfigParser

class Config(object, ConfigParser):
  __instance__ = None
  
  def __new__(cls):
    if cls.__instance__ is None:
      cls.__instance__ = object.__new__(cls)
    return cls.__instance__
  
  def __init__(self):
    object.__init__(self)
    ConfigParser.__init__(self)
    
    self.__logs = core.Logs()
    
    self.__logs.debug('search for a valid config file')
    #search for a configfile ...
    found = None
    search = ('/etc/pytoner.cfg', './pytoner.cfg')
    for filepath in search:
      if os.path.exists(filepath):
        if os.path.isfile(filepath):
          found = filepath
          break

    if found is None:
      self.__logs.fatal('Config file not found.')
    
    self.__logs.debug('Load config from %s !' % (found))
    self.read(found)
