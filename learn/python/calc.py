import sys
from PyQt5 import QtCore, QtGui, QtWidgets
# local design
from design import Ui_MainWindow

class Calculator(QtWidgets.QMainWindow):
	def __init__(self):
		super().__init__()

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.number_string = '0'
		# falta-me criar o grupo dos botões no designer
		for button in self.ui.digits.buttons():
			button.clicked.connect(self.add_digit)

		self.show()

	def add_digit(self):
		number = self.sender()
		self.ui.LCD.display(self.number_string)


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = Calculator()
	app.exec_()
