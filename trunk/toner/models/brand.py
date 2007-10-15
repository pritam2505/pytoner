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

from toner import core

class Brand(core.Model):
  def __init__(self, brand_id=None, brand_name=None):
    core.Model.__init__(self)
    
    if brand_id:
      try:
        self._id = int(brand_id)
      except:
        raise TypeError("brand_id must be an int")
    else:
      self._id = -1

    if brand_name:
      self._name = brand_name
    else:
      self._name = ""

  def __str__(self):
    return '<brand id="%d" name="%s" />' % (self._id, self._name)
    
