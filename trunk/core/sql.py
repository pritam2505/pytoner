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

import MySQLdb
import core

class Sql(object):
  __instance__ = None
  
  def __new__(cls):
    if cls.__instance__ is None:
      cls.__instance__ = object.__new__(cls)
    return cls.__instance__
    
  def __init__(self):
    object.__init__(self)

    self.__config = core.Config()
    self.__logs = core.Logs()
      
    # init connection param
    self._config_load()
      
    # connect
    try:
      self.__logs.debug('Try to connect to Mysql')
      self._connect = MySQLdb.connect(host=self.__host,
                                       user=self.__user,
                                       passwd=self.__pass,
                                       port=self.__port,
                                       db=self.__db)
    except Exception, e:
      self.__logs.fatal('Mysql connection failure: %s' % (e))
    
    self.__logs.debug('Connection okay.')
  
  def _config_load(self):
    self.__host = 'localhost'
    self.__port = 3306
    self.__user = 'root'
    self.__pass = ''
    self.__db = 'pytonner'
    
    if self.__config.has_option('mysql', 'host'):
      self.__host = self.__config.get('mysql', 'host')
    
    if self.__config.has_option('mysql', 'port'):
      self.__port = self.__config.getint('mysql', 'port')
    
    if self.__config.has_option('mysql', 'user'):
      self.__user = self.__config.get('mysql', 'user')
    
    if self.__config.has_option('mysql', 'pass'):
      self.__pass = self.__config.get('mysql', 'pass')
    
    if self.__config.has_option('mysql', 'db'):
      self.__db   = self.__config.get('mysql', 'db')
