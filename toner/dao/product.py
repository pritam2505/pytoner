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

from toner import core, models
from brand import Brand

class Product(core.Dao):
  def __init__(self):
    core.Dao.__init__(self)
    self._brand_dao = Brand()

  def _make_list(self, cursor):

    list = []
    for row in cursor.fetchall():
      product = models.Product(product_id=row[0], brand=self._brand_dao.get_by_id(row[1]),product_name=row[2],
                               product_desc=row[3], product_count=row[4])
      list.append(product)

    return list

  def add(self, product):
    query = """INSERT INTO product (
                 brand_id, product_name, product_desc,
                 product_count
               ) VALUES (
                 %(product_brand_id)s, %(product_name)s, %(product_desc)s, %(product_count)s
               );
             """ 
             
             
    params = { 'product_brand_id': product._brand._id, 'product_name': product._name, 
               'product_desc': product._desc, 'product_count': product._count } 

    cur = self._sql._connect.cursor()
    cur.execute(query, params)

    cur.close()

  def del_by_id(self, product_id):
    query = "DELETE FROM product WHERE product_id = %(product_id)s;"

    cur = self._sql._connect.cursor()
    cur.execute(query, {'product_id': product_id})
    cur.close()

  def del_by_name(self, product_name):
    query = "DELETE FROM product WHERE product_name = %(product_name)s;"

    cur = self._sql._connect.cursor()
    cur.execute(query, {'product_name': product_name})
    cur.close()

  def get_by_id(self, product_id):
    query = """SELECT
                 brand_id, product_name, product_desc, product_count
               FROM
                 product
               WHERE
                 product_id = %(product_id)s;"""

    cur = self._sql._connect.cursor()
    cur.execute(query, {'product_id': product_id})

    product = None
    if cur.rowcount == 1:
      row = cur.fetchone()
      product = models.Product(product_id=product_id, brand=self._brand_dao.get_by_id(row[0]), product_name=row[1],
                               product_desc=row[2], product_count=row[3])

    cur.close()
    return product

  def get_by_name(self, product_name):
    query = """SELECT
                 product_id, brand_id, product_desc, product_count
               FROM
                 product
               WHERE
                 product_name = %(product_name)s;"""

    cur = self._sql._connect.cursor()
    cur.execute(query, {'product_name': product_name})

    product = None
    if cur.rowcount == 1:
      row = cur.fetchone()
      product = models.Product(product_id=row[0], brand=self._brand_dao.get_by_id(row[1]), product_name=product_name,
                               product_desc=row[2], product_count=row[3])

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

  def get_list_by_brand_name(self, brand_name):
    query = """SELECT 
                 product_id, brand_id, product_name, product_desc,
                 product_count
               FROM 
                product NATURAL JOIN brand
               WHERE
                brand_name = %(brand_name)s;""" 

    cur = self._sql._connect.cursor()
    cur.execute(query, {'brand_name': brand_name})
    list = self._make_list(cur) 
    cur.close()

    return list

  def update(self, product):
    query = """UPDATE 
                product
               SET
                brand_id = %(brand_id)s,
                product_name = %(product_name)s,
                product_desc = %(product_desc)s,
                product_count = %(product_count)s
               WHERE
                 product_id = %(product_id)s;"""
    
    params = {'brand_id': product._brand._id, 'product_name': product._name, 'product_desc': product._desc, 'product_count': product._count,
              'product_id': product._id}

    cur = self._sql._connect.cursor()
    cur.execute(query, params)
    cur.close()

  def count_incr(self, product_id):
    query = """UPDATE
                 product 
               SET
                 product_count = product_count + 1
               WHERE
                 product_id = %(product_id)s;"""

    cur = self._sql._connect.cursor()
    cur.execute(query, {'product_id': product_id})
    cur.close()

  def count_decr(self, product_id):
    query = """UPDATE
                 product 
               SET
                 product_count = product_count - 1
               WHERE
                 product_id = %(product_id)s;"""

    cur = self._sql._connect.cursor()
    cur.execute(query, {'product_id':product_id})
    cur.close()

  def search(self, search):
    query = """SELECT
                 product_id, brand_id, product_name, product_desc,
                 product_count
               FROM
                 product
               WHERE
                 product_name LIKE %(search)s;
            """

    cur = self._sql._connect.cursor()
    cur.execute(query, {'search': search})
    list = self._make_list(cur)
    cur.close()

    return list

