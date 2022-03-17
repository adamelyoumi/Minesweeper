# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 14:47:20 2021

@author: adame
"""

import sys,os

path = "C:/Users/adame/OneDrive/Bureau/Minesweeper/"
os.chdir(path)

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from package.world_generator import wgen_random, wgen_random_clean


def initUI():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(960-250, 540-100, 400, 150)
    win.setWindowIcon(self,"smb.png")
    win.setWindowTitle("Difficulté")
    
    lab = QLabel("Choisissez le nombre de mines monde (40x40)")
    
    win.show()
    sys.exit(app.exec_())


initUI()