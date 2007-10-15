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

class Brand(core.Dao):
  def __init__(self):
    core.Dao.__init__(self)
    
  def add(self, brand):
    if self.exists_by_name(brand._name) is True:
      self._logs.info('brand %s exists !' % (brand._name))
      return False
      
    query = "INSERT INTO brand ( brand_name ) VALUES ( '%s');" %  (brand._name)
    
    cur = self._sql._connect.cursor()
    cur.execute(query)
    cur.close()
    
    return True

  def del_by_id(self, brand_id):
    query = "DELETE FROM brand WHERE brand_id = %d;" % (brand_id)
    cur = self._sql._connect.cursor()
    cur.execute(query)
    cur.close()

  def del_by_name(self, brand_name):
    query = "DELETE FROM brand WHERE brand_name = '%s';" % (brand_name)
    cur = self._sql._connect.cursor()
    cur.execute(query)
    cur.close()
  
  def exists_by_name(self, brand_name):
    query = "SELECT brand_id FROM brand WHERE brand_name = '%s';" % (
            brand_name )
  
    cur = self._sql._connect.cursor()
    cur.execute(query)
    
    if cur.rowcount == 1:
      result = True
    else:
      result = False
    
    cur.close()
    return result

  def exists_by_id(self, brand_id):
    query = "SELECT brand_id FROM brand WHERE brand_id = '%d';" % ( brand_id )

    cur = self._sql._connect.cursor()
    cur.execute(query)

    if cur.rowcount == 1:
      result = True
    else:
      result = False

    cur.close()
    return result
  
  def _make_list(self, cursor):
    brands = []
    for row in cursor.fetchall():
      brand = models.Brand(brand_id=row[0], brand_name=row[1])
      brands.append(brand)
    return brands

  def get_by_id(self, brand_id):
    query = "SELECT brand_name FROM brand WHERE brand_id = %d;" % (brand_id)

    cur = self._sql._connect.cursor()
    cur.execute(query)
    
    result = None
    if cur.rowcount == 1:
      row = cur.fetchone()
      result = models.Brand(brand_id=brand_id, brand_name=row[0])

    cur.close()
    return result

  def get_by_name(self, brand_name):
    query = "SELECT brand_id FROM brand WHERE brand_name = '%s';" % (brand_name)

    cur = self._sql._connect.cursor()
    cur.execute(query)

    result = None
    if cur.rowcount == 1:
      row = cur.fetchone()
      result = models.Brand(row[0], brand_name)

    cur.close()
    return result

  def getList(self):
    query = "SELECT brand_id, brand_name FROM brand;"
    
    cur = self._sql._connect.cursor()
    cur.execute(query)
    brands = self._make_list(cur)
    cur.close()
    
    return brands

  def update(self, brand):
    query = """
      UPDATE
        brand
      SET
        brand_name = '%s'
      WHERE
        brand_id = %d;""" % ( brand._name, brand._id )

    cur = self._sql._connect.cursor()
    cur.execute(query)
    cur.close()

  def search(self, brand_name):
    query = """
      SELECT brand_id, brand_name FROM brand WHERE brand_name LIKE '%s';
    """ % ( brand_name )
    
    cur = self._sql._connect.cursor()
    cur.execute(query)
    brands = self._make_list(cur)
    cur.close()

    return brands
 
