from PyQt4 import QtGui
from PyQt4 import QtCore
from helper import *
from defs import *
from arch import *

class StackFrame:

	def __init__(self, title, architecture, frame_ptr, stack_ptr, bottom, line, assembly):
		self.title = title
		self.architecture = architecture
		self.frame_ptr = frame_ptr
		self.stack_ptr = stack_ptr
		self.bottom = bottom
		self.line = line
		self.assembly = assembly
		self.items = []

	def addItem(self, frame_item):
		self.items.insert(0, frame_item)

	def removeItem(self):
		self.items.pop()

class FrameItem:

	def __init__(self):
		self.title = None
		self.addr = None
		self.length = None
		self.value = None
		self.initialized = None
		self.struct = None
		self.zoom_val = None

class FrameDisplay(QtGui.QTableWidget):

	def __init__(self, frame, addr_box):
		super(FrameDisplay, self).__init__()
		self.frame = frame
		self.addr_box = addr_box
		self.inspectOn = False
		self.initUI()

	def initUI(self):
		self.setColumnCount(1)
		self.horizontalHeader().hide()
		self.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
		self.updateDisplay()
		self.setMaximumHeight(self.rowCount()*self.rowHeight(0) + 2)
		self.highlightStackPointer()

		self.cellClicked.connect(self.cellInspected)

	def toggleInspect(self, inspectOn):
		self.inspectOn = inspectOn

	def cellInspected(self, row, col):
		if self.inspectOn:
			item = self.cellWidget(row, col)
			if item:
				self.addr_box.setText(item.statusTip())
			else:
				self.addr_box.clear()

	def highlightStackPointer(self):
		for i in range(0, self.rowCount()):
			header_text = self.verticalHeaderItem(i).text()
			if header_text and self.frame.architecture.stack_pointer in header_text:
				self.selectRow(i)

	def addTempStorageSpace(self, last_addr):
		temp_space = (last_addr - int(self.frame.stack_ptr, 16)) / 4

		for i in range(0, temp_space):
			self.insertRow(self.rowCount())
			header = QtGui.QTableWidgetItem("")
			curr_addr = hex(int(self.frame.stack_ptr, 16) + 4*i)
			header.setToolTip("^ " + str(curr_addr))
			self.setVerticalHeaderItem(self.rowCount() - 1, header)

			if self.frame.stack_ptr == curr_addr:
				header.setText(self.frame.architecture.stack_pointer)

	def updateDisplay(self):
		sorted_list = sorted(self.frame.items, key=lambda x: x.addr)
		# Check if in main
		if self.frame.stack_ptr != None:
			self.addTempStorageSpace(int(sorted_list[0].addr, 16))

		for item in sorted_list:
			self.displayItem(item)

	def displayItem(self, frame_item):
		item_title = QtGui.QLabel()
		if not frame_item.initialized:
			item_title.setText(" " + frame_item.title + " =\n     " + UNINITIALIZED)
			item_title.setStatusTip(UNINITIALIZED)
		else:
			item_title.setText(" " + frame_item.title + " =\n     " + frame_item.struct + frame_item.value)
			item_title.setStatusTip(frame_item.zoom_val)

		row_span = int(frame_item.length)/4

		for i in range(0, row_span):
			self.insertRow(self.rowCount())
			header = QtGui.QTableWidgetItem("")
			header.setToolTip("^ " + str(hex(int(frame_item.addr, 16) + 4*i)))
			self.setVerticalHeaderItem(self.rowCount() - 1, header)

			if i == 0:
				if self.frame.frame_ptr == frame_item.addr and self.frame.stack_ptr == frame_item.addr:
					header.setText(self.frame.architecture.base_pointer + "/" + self.frame.architecture.stack_pointer)
				elif self.frame.frame_ptr == frame_item.addr:
					header.setText(self.frame.architecture.base_pointer)
				elif self.frame.stack_ptr == frame_item.addr:
					header.setText(self.frame.architecture.stack_pointer)

		new_row = self.rowCount() - row_span
		self.setCellWidget(new_row, 0, item_title)

		if row_span > 1:
			self.setSpan(new_row, 0, row_span, 1)

	def selectionChanged(self, selected, deselected):
		if not self.inspectOn and len(selected.indexes()) > 0:
			row = selected.indexes()[0].row()
			self.addr_box.setText(self.verticalHeaderItem(row).toolTip())
