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

from controler import Controler
from toner import models, views, dao

class Brand(Controler):
  def __init__(self):
    Controler.__init__(self)

  def menu(self):
    while True:
      print " [0] Previous"
      print " [1] Add Brand"
      print " [2] Del Brand"
      print " [3] List Brand"
      print " [4] Search Brand"
      print " [5] Edit Brand"
      print

      choice = self._input_int(" Your choise: ")
      print

      if choice == 0:
        return
      if choice == 1:
        self.add()
      if choice == 2:
        self.delete()
      elif choice == 3:
        self.list()
      elif choice == 4:
        self.search()
      elif choice == 5:
        self.edit()
      else:
        print "choice not understood, try again."


  def add(self):
    brand_sql = dao.Brand()
    brand_name = self._input("brand_name: ")
    
    if brand_sql.add(brand_name) is True:
      print "Okay"
    else:
      print "Error"
    print
  
  def delete(self):
    brand_dao = dao.Brand()
    brand_id = self._input_num_or_list(self.list, "brand_id: (l=list)")
    print

    brand_dao.del_by_id(brand_id)

  def edit(self):
    brand_dao = dao.Brand()
    brand_id = self._input_num_or_list(self.list, "brand_id: (l=list)")

    brand = brand_dao.get_by_id(brand_id)

    brand._name = self._input_with_default(brand._name, "brand_name: ")
    brand_dao.update(brand)
    print


  def list(self):
    brand_sql = dao.Brand()
    brand_view = views.console.Brand()

    list = brand_sql.getList()
    brand_view.show_list(list)

  def search(self):
    brand_name = self._input("brand search: ")
    print

    brand_dao = dao.Brand()
    brand_view = views.console.Brand()

    list = brand_dao.search(brand_name)
    brand_view.show_list(list)
  
