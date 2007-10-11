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

class Dao:
  def __init__(self):
    self._config = core.Config()
    self._logs = core.Logs()
    self._sql = core.Sql()
    
