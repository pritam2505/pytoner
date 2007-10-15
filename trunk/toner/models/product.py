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
from brand import Brand

class Product(core.Model):
  def __init__(self, product_id=None, brand=None, product_name=None, product_desc=None, product_count=None):
    core.Model.__init__(self)

    if product_id:
      try:
        self._id = int(product_id)
      except:
        raise TypeError("product_id must be an integer")
    else:
      self._id = -1

    if brand:
      self._brand = brand
    else:
      self._brand = Brand() 

    if product_name:
       self._name = product_name
    else:
       self._name = ""

    if product_desc:
      self._desc = product_desc
    else:
      self._desc = "" 

    if product_count:
      try:
        self._count = int(product_count)
      except:
        raise TypeError("product_count must be an integer")
    else:
      self._count = 0

  def __str__(self):
    return '<product id="%d" brand_id="%d" brand_name="%s" name="%s" desc="%s" count="%d"' % ( self._id, self._brand._id, self._brand._name,
                                                                                               self._name, self._desc, self._count )

