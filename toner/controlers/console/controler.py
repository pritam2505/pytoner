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

class Controler:
  def __init__(self):
    self._logs = core.Logs() 

  def _input(self, prompt=None):
    if prompt is None:
      line = raw_input()
    else:
      line = raw_input(prompt)

    if '\n' in line:
      line = line[:-1]

    return line

  def _input_int(self, prompt=None):
    try:
      num = int(self._input(prompt))
    except:
      print "Only numeric values are allowed !"
      return -1 

    return num

  def _input_num_or_list(self, list, prompt=None):
    while True:
      line = self._input(prompt)
            
      num = -1
      if line == "l":
        list()
        continue
      
      try:
        num = int(line)
      except:
        print "Need numeric value or 'l' for list"
     
      if num > -1:
        break
    
    return num

  def _input_with_default(self, default, prompt=None):
    line = self._input("%s [%s] " % (prompt, default))

    if line == "":
      line = default

    return line

