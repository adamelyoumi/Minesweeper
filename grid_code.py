from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from package import world_generator
from time import time, sleep
import os

h = world_generator.haut
l = world_generator.larg

but_sz = 20   # Button size
path = ""
n_mines = 10

class Ui_GridWindow(QtWidgets.QMainWindow):
   def setupUi(self,MainWindow,h,l,n_mines,world):
      print(world)
      self.MainWindow = MainWindow
      self.world = world
      self.h = h
      self.l = l

      MainWindow.setObjectName("MainWindow")
      MainWindow.setWindowTitle("Minesweeper")
      self.icon = QtGui.QIcon(os.path.join("images","demineur.png"))
      MainWindow.setWindowIcon(self.icon)
      MainWindow.resize(120 + but_sz*l, 120 + but_sz*h)

      self.centralwidget = QtWidgets.QWidget(self.MainWindow)
      self.centralwidget.setObjectName("centralwidget")
      self.nFlags = 0

      self.photo = QtWidgets.QLabel(self.centralwidget)
      self.photo.setGeometry(but_sz*l, 5, 50,50)
      self.photo.setText("")
      #self.photo.setPixmap(QtGui.QPixmap(os.path.join("images","pause2.jpg")))
      self.photo.setObjectName("image")

      self.resultat = QtWidgets.QLabel(self.centralwidget)
      self.resultat.setGeometry(QtCore.QRect(20, 20, 221, 16))
      #self.resultat.setFont(font)
      self.resultat.setObjectName("nMinesLabel")

      self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
      self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 70, but_sz*l, but_sz*h))
      self.gridLayoutWidget.setObjectName("gridLayoutWidget")

      self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
      self.gridLayout.setContentsMargins(0,0,0,0)
      self.gridLayout.setSpacing(0)
      self.gridLayout.setObjectName("gridLayout")

      self.buttons = [[0 for _ in range(h)] for _ in range(l)]

      for i in range(h):
         for j in range(l):
            self.buttons[i][j] = QtWidgets.QPushButton(self.gridLayoutWidget)
            self.buttons[i][j].setObjectName("case_"+str(i)+"_"+str(j))
            self.buttons[i][j].setText("")

            self.gridLayout.addWidget(self.buttons[i][j], i, j, 1,1)
            self.buttons[i][j].installEventFilter(self)

      MainWindow.setCentralWidget(self.centralwidget)

   def eventFilter(self, obj, event):
      if event.type() == QtCore.QEvent.MouseButtonPress:
         if event.button() == QtCore.Qt.LeftButton:
            self.leftClickedButton(obj)
         elif event.button() == QtCore.Qt.RightButton:
            self.rightClickedButton(obj)
      return QtCore.QObject.event(obj, event)


   def leftClickedButton(self, obj):
      L = str.split(obj.objectName(),"_")
      L.pop(0)
      [i,j] = L
      i,j=int(i),int(j)
      print("Left clicked " + obj.objectName())
      if self.world[i][j] == -1:
         self.resultat.setText("Exploded !")
         for i in range(self.h):
            for j in range(self.l):
               self.buttons[i][j].setText(str(int(self.world[i][j])))
           
         #sleep(10)
         #self.MainWindow.close()

      else:
         self.buttons[i][j].setText(str(int(self.world[i][j])))
         if self.world[i][j] == 0:
            self.propagate(i,j)

   def rightClickedButton(self, obj):
      L = str.split(obj.objectName(),"_")
      L.pop(0)
      [i,j] = L
      i,j=int(i),int(j)
      if self.buttons[i][j].text() == "":
         self.buttons[i][j].setText("F")
         self.nFlags += 1
      elif self.buttons[i][j].text() == "F":
         self.buttons[i][j].setText("")
         self.nFlags -= 1
      print(str(self.nFlags) + " / " + str(n_mines))
      self.check_win()

   def check_win(self):
      compt = 0
      for i in range(h):
         for j in range(l):
            if self.buttons[i][j].text() == "F" and self.world[i][j] == -1:
               compt+=1
      if compt == n_mines:
         self.resultat.setText("Success !")
         #self.photo.setPixmap(QtGui.QPixmap(os.path.join("images","pogu2.jpg")))

   def propagate(self,i,j): # Recursive function to display relevant values if a "0" is clicked
      if self.world[i][j] == 0:

            self.buttons[i][j].setText("0")
            if i==0 and j==0:
               if self.buttons[0][1].text() == "":
                  self.propagate(0,1)
               if self.buttons[1][0].text() == "":
                  self.propagate(1,0)
               if self.buttons[1][1].text() == "":
                  self.propagate(1,1)

            elif i==0 and j==self.l-1:
               if self.buttons[0][self.l-2].text() == "":
                  self.propagate(0,self.l-2)
               if self.buttons[0][self.l-1].text() == "":
                  self.propagate(1,self.l-1)
               if self.buttons[1][self.l-2].text() == "":
                  self.propagate(1,self.l-2)

            elif i==self.h-1 and j==0:
               if self.buttons[self.h-1][1].text() == "":
                  self.propagate(self.h-1,1)
               if self.buttons[self.h-2][0].text() == "":
                  self.propagate(self.h-2,0)
               if self.buttons[self.h-2][1].text() == "":
                  self.propagate(self.h-2,1)

            elif i==self.h-1 and j==self.l-1:
               if self.buttons[self.h-1][self.l-2].text() == "":
                  self.propagate(self.h-1, self.l-2)
               if self.buttons[self.h-2][self.l-1].text() == "":
                  self.propagate(self.h-2, self.l-1)
               if self.buttons[self.h-2][self.l-2].text() == "":
                  self.propagate(self.h-2, self.l-2)

            elif i==0:
               if self.buttons[0][j-1].text() == "":
                  self.propagate(0,j-1)
               if self.buttons[0][j+1].text() == "":
                  self.propagate(0,j+1)
               if self.buttons[1][j-1].text() == "":
                  self.propagate(1,j-1)
               if self.buttons[1][j].text() == "":
                  self.propagate(1,j)
               if self.buttons[1][j+1].text() == "":
                  self.propagate(1,j+1)

            elif i==self.h-1:
               if self.buttons[self.h-1][j-1].text() == "":
                  self.propagate(self.h-1,j-1)
               if self.buttons[self.h-1][j+1].text() == "":
                  self.propagate(self.h-1,j+1)
               if self.buttons[self.h-2][j-1].text() == "":
                  self.propagate(self.h-2,j-1)
               if self.buttons[self.h-2][j].text() == "":
                  self.propagate(self.h-2,j)
               if self.buttons[self.h-2][j+1].text() == "":
                  self.propagate(self.h-2,j+1)

            elif j==0:
               if self.buttons[i-1][0].text() == "":
                  self.propagate(i-1,0)
               if self.buttons[i+1][0].text() == "":
                  self.propagate(i+1,0)
               if self.buttons[i-1][1].text() == "":
                  self.propagate(i-1,1)
               if self.buttons[i][1].text() == "":
                  self.propagate(i,1)
               if self.buttons[i+1][1].text() == "":
                  self.propagate(i+1,1)

            elif j==self.l-1:
               if self.buttons[i-1][self.l-1].text() == "":
                  self.propagate(i-1,self.l-1)
               if self.buttons[i+1][self.l-1].text() == "":
                  self.propagate(i+1,self.l-1)
               if self.buttons[i-1][self.l-2].text() == "":
                  self.propagate(i-1,self.l-2)
               if self.buttons[i][self.l-2].text() == "":
                  self.propagate(i,self.l-2)
               if self.buttons[i+1][self.l-2].text() == "":
                  self.propagate(i+1,self.l-2)

            elif i>0 and i<self.h-1 and j>0 and j<self.l-1:
               if self.buttons[i-1][j-1].text() == "":
                  self.propagate(i-1,j-1)
               if self.buttons[i+1][j-1].text() == "":
                  self.propagate(i+1,j-1)
               if self.buttons[i][j-1].text() == "":
                  self.propagate(i,j-1)
               if self.buttons[i-1][j].text() == "":
                  self.propagate(i-1,j)
               if self.buttons[i+1][j].text() == "":
                  self.propagate(i+1,j)
               if self.buttons[i-1][j+1].text() == "":
                  self.propagate(i-1,j+1)
               if self.buttons[i][j+1].text() == "":
                  self.propagate(i,j+1)
               if self.buttons[i+1][j+1].text() == "":
                  self.propagate(i+1,j+1)
      else:
         self.buttons[i][j].setText(str(int(self.world[i][j])))

if __name__ == "__main__":
   import sys
   app = QtWidgets.QApplication(sys.argv)
   MainWindow = QtWidgets.QMainWindow() # On définit une Mainwindow
   ui = Ui_GridWindow()
   ui.setupUi(h,l,n_mines)
   MainWindow.show()
   sys.exit(app.exec_())
