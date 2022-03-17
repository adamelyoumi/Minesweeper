# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
#from QtCore import QCloseEvent
from package import world_generator

h = world_generator.haut
l = world_generator.larg
path = world_generator.path

class Ui_MainWindow(object):

	def __init__(self):
		super().__init__()

	def setupUi(self, MainWindow):
		font = QtGui.QFont()
		font.setFamily("Arial")

		self.a = MainWindow
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(291, 254)
		MainWindow.setFont(font)

		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		MainWindow.setCentralWidget(self.centralwidget)

		self.nMinesChooser = QtWidgets.QSpinBox(self.centralwidget)
		self.nMinesChooser.setGeometry(QtCore.QRect(90, 90, 101, 22))
		self.nMinesChooser.setObjectName("nMinesChooser")

		self.nMinesLabel = QtWidgets.QLabel(self.centralwidget)
		self.nMinesLabel.setGeometry(QtCore.QRect(40, 40, 221, 16))
		self.nMinesLabel.setFont(font)
		self.nMinesLabel.setObjectName("nMinesLabel")

		self.button_OK = QtWidgets.QPushButton(self.centralwidget)
		self.button_OK.setGeometry(QtCore.QRect(90, 140, 93, 28))
		self.button_OK.setObjectName("button_OK")

		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 291, 23))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)

		self.menuJeux = QtWidgets.QMenu(self.menubar)
		self.menuJeux.setObjectName("menuJeux")

		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.actionD_mineur = QtWidgets.QAction(MainWindow)
		self.actionD_mineur.setObjectName("actionD_mineur")
		self.actionabc = QtWidgets.QAction(MainWindow)
		self.actionabc.setObjectName("actionabc")

		self.menuJeux.addAction(self.actionD_mineur)
		self.menuJeux.addAction(self.actionabc)

		self.menubar.addAction(self.menuJeux.menuAction())

		self.retranslateUi(MainWindow)

		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def game_window(self):

		self.world_clean = world_generator.wgen_random_clean(self.n_mines)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.nMinesChooser.setToolTip(_translate("MainWindow", "<html><head/><body><p>Choose the number of mines</p></body></html>"))
		self.nMinesLabel.setText(_translate("MainWindow", "Combien de mines ? (Monde: 40x40)"))
		self.button_OK.setText(_translate("MainWindow", "OK"))
		self.menuJeux.setTitle(_translate("MainWindow", "Jeux"))
		self.actionD_mineur.setText(_translate("MainWindow", "Démineur"))

		self.actionabc.setText(_translate("MainWindow", "abc"))

		self.n_mines = self.get_n_mines()

		self.button_OK.clicked.connect(MainWindow.close)
		self.button_OK.clicked.connect(lambda: self.game_window())


	def get_n_mines(self):
		return(self.nMinesChooser.value())

	def closeEvent(self, event):
		reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?',
				QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

		if reply == QMessageBox.Yes:
			event.accept()
			print('Window closed')
		else:
			event.ignore()

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	w = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(w)
	w.show()
	sys.exit(app.exec_())