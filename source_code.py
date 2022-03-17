# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 13:48:59 2021

@author: adame
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget


def main():

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

#%%

import os,sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

path = "C:/Users/adame/OneDrive/Bureau/"

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Minesweeper')
        self.setWindowIcon(QIcon(path + 'smb.png'))

        self.show()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
    
#%%

import os

print(os.listdir(path))
