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
from brand import Brand

import models
import views
import dao

class Product(Controler):
  def __init__(self):
    Controler.__init__(self)
    self._brand = Brand()

  def menu(self):
    while True:
      print " [0] Exit"
      print " [1] Add Product"
      print " [2] Del Product"
      print " [3] List Product"
      print " [4] Search Product"
      print " [5] Edit Product" 
      print " [6] Increment Product Count"
      print " [7] Decrement Product Count"
      print " [8] Manage Brand"
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
      elif choice == 6:
        self.count_incr()
      elif choice == 7:
        self.count_decr()
      elif choice == 8:
        self._brand.menu()
      else:
        print "choice not understood, try again."


  def add(self):
    brand_dao = dao.Brand()
    brand_id = -1
    while brand_dao.exists_by_id(brand_id) is False:
      brand_id = self._input_num_or_list(self._brand.list, "brand_id (or l=list): ")
    
    product = models.Product()
    product._brand = brand_dao.get_by_id(brand_id)
    product._name = self._input("product_name: ")
    product._desc = self._input("product_desc: ")
    product._count = self._input_int("product_count: ")

    product_dao = dao.Product()
    product_dao.add(product)

    print

  def delete(self):
    product_id = self._input_num_or_list(self.list, "product_id (or l=list): ")
    product_dao = dao.Product()
    product_dao.delete_by_id(product_id)

  def edit(self):
    product_id = self._input_num_or_list(self.list, "product_id (or l=list): ")
    product_dao = dao.Product()
    product = product_dao.get_by_id(product_id)

    product._name = self._input_with_default(product._name, "product_name: ")
    product._desc = self._input_with_default(product._desc, "product_desc: ")
    product._count = int(self._input_with_default(product._count, "product_count: "))

    product_dao.update(product)

  def count_incr(self):
    product_id = self._input_num_or_list(self.list, "product_id (or l=list): ")
    product_dao = dao.Product()
    product_dao.count_incr(product_id)


  def count_decr(self):
    product_id = self._input_num_or_list(self.list, "product_id (or l=list): ")
    product_dao = dao.Product()
    product_dao.count_decr(product_id)

  def list(self):
    product_dao = dao.Product()
    product_view = views.console.Product()

    list = product_dao.get_list()
    product_view.show_list(list)

  def search(self):
    product_name = self._input("product_name: ")
    product_dao = dao.Product()
    product_view = views.console.Product()

    list = product_dao.search(product_name)
    product_view.show_list(list)

