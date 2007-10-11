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

class Logs(object):
  __instance__ = None
  
  def __new__(cls):
    if cls.__instance__ is None:
      cls.__instance__ = object.__new__(cls)
    return cls.__instance__
  
  def __init__(self):
    object.__init__(self)
    self._file = open('pytoner.log', 'a+')

  def finalize(self):
    self._file.close()

  def _message(self, message):
    self._file.write("%s\n" % message)
    self._file.flush()

  def debug(self, message):
    self._message("DEBUG: %s" % message)

  def info(self, message):
    self._message("INFO: %s" % message)

  def warning(self, message):
    self._message("WARNING: %s" % message)

  def error(self, message):
    self._message("ERROR: %s" % message)

  def fatal(self, message):
    self._message("FATAL: %s" % message)
    print("FATAL: %s" % message)
    sys.exit(1)

