import sys
import os
import mainwindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *



class MainWindow(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):
	"""docstring for MainWindow"""
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.pushButton.clicked.connect(self.search_in_DERECTORY)


	def pressButton(self):
		self.textBrowser.setText(str('wd'))


	def search_in_DERECTORY(self):
		self.textBrowser.setText('')
		DERECTORY = self.lineEdit.text()
		DERECTORY_COPY = DERECTORY
		file_number = 0

		try:
			fod = {}
			files_on_DERECTORY = os.listdir(DERECTORY)
			for file in files_on_DERECTORY:
				info_adout_file = os.path.getsize(f'{DERECTORY}/{file}')
				file_number += 1
				'''fod[f'{file}'] = info_adout_file
				sorted_fod = sorted(fod.items(), key=lambda x: x[1])
				sorted_fod = dict(sorted_fod)
				#print(sorted_fod)
				#sorted_tuple = sorted(fod.items(), key=lambda x: x[1])'''
				self.textBrowser.append(f'{file_number}) {file}| размер: {info_adout_file} byte')
		except FileNotFoundError:
			QMessageBox.information(self, 'Поиск', "Системе не удалось найти данный путь!", QMessageBox.Cancel)
		except NotADirectoryError:
			QMessageBox.information(self, 'Открытие файла', "Нельзя открыть файл!", QMessageBox.Cancel)


if __name__ == '__main__':
	#Создание приложения
	app = QtWidgets.QApplication([sys.argv])

	#Запуск формы главного окна
	window = MainWindow()
	window.show()
	

	#Запуск
	sys.exit(app.exec())