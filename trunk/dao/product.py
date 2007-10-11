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
import models
from brand import Brand

class Product(core.Dao):
  def __init__(self):
    core.Dao.__init__(self)

  def _make_list(self, cursor):
    brand_dao = Brand()

    list = []
    for row in cursor.fetchall():
      product = models.Product()
      product.set(row[0], brand_dao.get_by_id(row[1]),row[2], row[3], row[4])
      list.append(product)

    return list

  def add(self, product):
    query = """INSERT INTO product (
                 brand_id, product_name, product_desc,
                 product_count
               ) VALUES (
                 %d, '%s', '%s', %d
               );
             """ % (
               product._brand._id, product._name, product._desc,
               product._count
             )

    cur = self._sql._connect.cursor()
    cur.execute(query)
    cur.close()

  def delete_by_id(self, product_id):
    query = "DELETE FROM product WHERE product_id = %d;" % (product_id)

    cur = self._sql._connect.cursor()
    cur.execute(query)
    cur.close()

  def get_by_id(self, product_id):
    query = """SELECT
                 brand_id, product_name, product_desc, product_count
               FROM
                 product
               WHERE
                 product_id = %d;""" % (product_id)

    cur = self._sql._connect.cursor()
    cur.execute(query)

    product = None
    if cur.rowcount == 1:
      row = cur.fetchone()
      product = models.Product()
      product.set(product_id, row[0], row[1], row[2], row[3])

    cur.close()
    return product

  def get_list(self):
    query = """SELECT 
                 product_id, brand_id, product_name, product_desc,
                 product_count
               FROM product;"""

    cur = self._sql._connect.cursor()
    cur.execute(query)
    list = self._make_list(cur) 
    cur.close()

    return list

  def update(self, product):
    query = """UPDATE 
                 product
               SET
                product_name = '%s',
                product_desc = '%s',
                product_count = %d
               WHERE
                 product_id = %d;""" % (
              product._name, product._desc, product._count,
              product._id
            )
    
    cur = self._sql._connect.cursor()
    cur.execute(query)
    cur.close()

  def count_incr(self, product_id):
    query = """UPDATE
                 product 
               SET
                 product_count = product_count + 1
               WHERE
                 product_id = %d;""" % ( product_id )

    cur = self._sql._connect.cursor()
    cur.execute(query)
    cur.close()

  def count_decr(self, product_id):
    query = """UPDATE
                 product 
               SET
                 product_count = product_count - 1
               WHERE
                 product_id = %d;""" % ( product_id )

    cur = self._sql._connect.cursor()
    cur.execute(query)
    cur.close()

  def search(self, product_name):
    query = """SELECT
                 product_id, brand_id, product_name, product_desc,
                 product_count
               FROM
                 product
               WHERE
                 product_name LIKE '%s';
            """ % (product_name)

    cur = self._sql._connect.cursor()
    cur.execute(query)
    list = self._make_list(cur)
    cur.close()

    return list

