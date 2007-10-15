
from toner import core, dao, views, models

import sys

from PyQt4 import QtCore,QtGui
from product_model import ProductModel
from product_model import ProductBrandDelegate


class Main(QtGui.QMainWindow):
  def __init__(self):
    self._app = QtGui.QApplication(sys.argv)
    QtGui.QMainWindow.__init__(self)
    
    self._pytoner = views.qt.Ui_PyToner()
    self._pytoner.setupUi(self) 

    # Combo #
    self._brand_dao = dao.Brand()
    self.brand_update()

    # Menu #
    QtCore.QObject.connect(self._pytoner.action_Exit, QtCore.SIGNAL("activated()"),
                           self.actionExit)

    # Add Brand #
    QtCore.QObject.connect(self._pytoner.brand_add, QtCore.SIGNAL("clicked()"),
                           self.brand_add)

    # Del Brand #
    QtCore.QObject.connect(self._pytoner.brand_del, QtCore.SIGNAL("clicked()"),
                           self.brand_del)

    # Product TAble #
    self._product_model = ProductModel()
    self._pytoner.product_table.setSortingEnabled(True)
    self._pytoner.product_table.setModel(self._product_model)

    self._product_brand_delegate = ProductBrandDelegate()
    self._pytoner.product_table.setItemDelegateForColumn(0, self._product_brand_delegate)

    QtCore.QObject.connect(self._pytoner.brand_combo, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self._product_model.set_view)

    QtCore.QObject.connect(self._pytoner.product_add,
                           QtCore.SIGNAL("clicked()"),
                           self.product_add)

    QtCore.QObject.connect(self._pytoner.product_del,
                           QtCore.SIGNAL("clicked()"),
                           self.product_del)

  def main(self):
    #show
    self.show()
    sys.exit(self._app.exec_())

  def brand_add(self):
    # add data
    brand = models.Brand(-1, self._pytoner.brand_combo.currentText())
    self._brand_dao.add(brand)
    # update display
    self.brand_update()

  def brand_del(self):
    self._brand_dao.del_by_name(self._pytoner.brand_combo.currentText())
    self.brand_update()

  def brand_update(self):
    self._pytoner.brand_combo.clear()
    brand_list = self._brand_dao.getList()
    self._pytoner.brand_combo.insertItem(0, " -- ALL -- ")
    for brand in brand_list:
      self._pytoner.brand_combo.insertItem(0, brand._name)

    self._pytoner.brand_combo.setInsertPolicy(QtGui.QComboBox.NoInsert)
   
  def product_add(self):
    print "product_add()"
    indexes = self._pytoner.product_table.selectedIndexes()
    if len(indexes) == 0:
      self._product_model.insertRow(self._product_model.rowCount())
    else:
      index = indexes[0]
      self._product_model.insertRow(index.row())

  def product_del(self):
    print "product_del()"
    indexes = self._pytoner.product_table.selectedIndexes()
    if len(indexes) > 0:
      self._product_model.removeRow(indexes[0].row())
    else:
      print "selection not found"

  def actionExit(self):
    sys.exit(0)
