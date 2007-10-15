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

import sys
import datetime

from config import Config

class Logs(object):
  __instance__ = None
  
  def __new__(cls):
    if cls.__instance__ is None:
      cls.__instance__ = object.__new__(cls)
      cls.__constuct__(cls.__instance__)
    return cls.__instance__
  
  def __constuct__(self):
    object.__init__(self)
    self._config = Config()

    self._files = {}
    self._sections = {'debug':[], 'info':[], 'warning':[], 'error':[], 'fatal':[]}
    self._enabled = self._config.getboolean('pytoner', 'logs')

    if self._enabled:
      # prepare files and section
      for file_name in self._config.options('logs'):
        self._files[file_name] = open(file_name, 'a+')

        sections = self._config.get('logs', file_name)
        if sections == "*":
          for section in self._sections:
            self._sections[section].append(file_name)
        else:
          for section in sections.split(','):
            if self._sections.has_key(section):
              self._sections[section].append(file_name)

    # create section functions
    for section in self._sections:
      self.__dict__[section] = lambda message, section=section: self._message(section, message)

  def _message(self, level, message):
    dt=datetime.datetime(1999, 2, 1)
    now=dt.now()

    if self._enabled:
     if self._sections.has_key(level):
       for file_name in self._sections[level]:
         file = self._files[file_name]
         file.write("%s - %s: %s\n" % (now, level, message))
         file.flush()

  def __finalize__(self):
    for key, value in self._files:
      value.close()

