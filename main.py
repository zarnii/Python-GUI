import sys
import os
import mainwindow
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *



class MainWindow(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
	"""docstring for MainWindow"""
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setupUi(self)
		self.pushButton.clicked.connect(self.pressButton)
		self.populate()


	def pressButton(self):
		pass

	def populate(self):
		path = "C:\\Windows"
		model =	QtWidgets.QFileSystemModel()
		model.setRootPath((QtCore.QDir.rootPath()))
		self.treeView.setModel(model)
		self.treeView.setSortingEnabled(True)




	

if __name__ == '__main__':
	#Создание приложения
	app = QtWidgets.QApplication([sys.argv])

	#Запуск формы главного окна
	window = MainWindow()
	window.show()
	

	#Запуск
	sys.exit(app.exec())