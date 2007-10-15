
from toner import dao, models
from PyQt4 import QtCore,QtGui

class ProductBrandDelegate(QtGui.QItemDelegate):
  def __init__(self):
    QtGui.QAbstractItemDelegate.__init__(self)
    self._brand_dao = dao.Brand()
    self._product_dao = dao.Product()

  def createEditor(self, parent, option, index):
    combo = QtGui.QComboBox(parent)
    combo.setInsertPolicy(QtGui.QComboBox.NoInsert)

    brand_list = self._brand_dao.getList()
    for brand in brand_list:
      combo.insertItem(0, brand._name)

    return combo
    
  def setEditorData(self, widget, index):
    index = widget.findText(index.data().toString())
    widget.setCurrentIndex(index)

  def setModelData(self, widget, model, index):
    brand_name = widget.currentText()
    model.setData(index, QtCore.QVariant(brand_name), QtCore.Qt.EditRole)

  def editorChange(self, brand_name):
    brand = self._brand_dao.get_by_name(brand_name)
    self._item._brand = brand
    
    self._product_dao.update(self._item)
    self.emit(QtCore.SIGNAL("commitData(QtWidget *)"))
    

class ProductModel(QtCore.QAbstractTableModel):
  def __init__(self):
    QtCore.QAbstractTableModel.__init__(self)

    self._view_name = " -- ALL -- " 
    self._product_dao = dao.Product()
    self._brand_dao = dao.Brand()
    self.update()
  
  def set_view(self, view_name):
    self._view_name = view_name
    self.update()
    self.emit(QtCore.SIGNAL("layoutChanged()"))

  def update(self):
    if self._view_name == " -- ALL -- ":
      self._product_list = self._product_dao.get_list()
    else:
      self._product_list = self._product_dao.get_list_by_brand_name(self._view_name)

  def rowCount(self, parent=QtCore.QModelIndex()):
    return len(self._product_list)

  def columnCount(self, parent=QtCore.QModelIndex()):
    return 4

  def sort(self, column, order):
    if order == 1:
      reverse=True
    else:
      reverse=False

    if column == 0:
      my_cmp=lambda x, y: cmp(x._brand._name, y._brand._name)
    elif column == 1:
      my_cmp=lambda x, y: cmp(x._name, y._name)
    elif column == 2:
      my_cmp=lambda x, y: cmp(x._desc, y._desc)
    elif column == 4:
      my_cmp=lambda x, y: cmp(x._count, y._count)
    else:
      my_cmp=cmp

    self._product_list.sort(cmp=cmp, reverse=reverse)
    self.emit(QtCore.SIGNAL("layoutChanged()"))

  def headerData(self, section, orientation, role):
    if role == QtCore.Qt.DisplayRole and orientation == QtCore.Qt.Horizontal:
      if section == 0:
        result = "brand_name"
      elif section == 1:
        result = "product_name"
      elif section == 2:
        result = "product_desc"
      elif section == 3:
        result = "product_count"

      return QtCore.QVariant(result)

    if role == QtCore.Qt.DisplayRole and orientation == QtCore.Qt.Vertical:
      return QtCore.QVariant(self._product_list[section]._id)

    return QtCore.QVariant()


  def data(self, index, role):
    if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
      item = self._product_list[index.row()]
      if index.column() == 0:
        value = item._brand._name
      elif index.column() == 1:
        value = item._name
      elif index.column() == 2:
        value = item._desc
      elif index.column() == 3:
        value = item._count
      else:
        value = "error"

      return QtCore.QVariant(value)
    
    return QtCore.QVariant()

  def setData(self, index, value, role):
    if role == QtCore.Qt.EditRole:
      item = self._product_list[index.row()]
      changed = False
      if index.column() == 0:
        if value.type() == QtCore.QVariant.String:
          brand_name = value.toString()
          item._brand = self._brand_dao.get_by_name(brand_name)
          changed = True
      elif index.column() == 1:
        if value.type() == QtCore.QVariant.String:
          item._name = value.toString()
          changed = True
      elif index.column() == 2:
        if value.type() == QtCore.QVariant.String:
          item._desc = value.toString()
          changed = True
      elif index.column() == 3:
        if value.type() == QtCore.QVariant.Int:
          item._count, ok = value.toInt()
          if ok:
            changed = True
        
      if changed:
        self._product_dao.update(item)  
        self.emit(QtCore.SIGNAL("layoutChanged()"))
        return True
      else:
        return False

    return False

  def flags(self, index):
    #if index.column() == 0:
    #  return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
    #else:
    return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable

  def insertRows(self, row, count, parent=QtCore.QModelIndex()):
    self.beginInsertRows(parent, row, row + count - 1)
    for i in range(row, row + count):
      brand = models.Brand(-1, "Invalid")
      product = models.Product(brand=brand, product_name="change me", product_desc="change me", product_count=0)
      self._product_dao.add(product)
      product = self._product_dao.get_by_name(product._name)
      if (product == None):
        return False
      self._product_list.append(product)

    self.endInsertRows()
    return True

  def removeRows(self, row, count, parent=QtCore.QModelIndex()):
    self.beginRemoveRows(parent, row, row + count - 1)
    for i in range(row, row + count):
      id = self._product_list[i]._id
      self._product_dao.del_by_id(id)

    self.endRemoveRows()
    return True

