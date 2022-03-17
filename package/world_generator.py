# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 15:14:22 2021

@author: adame
"""

import numpy as np
import numpy.random as rnd

larg = 10
haut = 10
path = "C:\\Users\\adame\\OneDrive\\Bureau\\Minesweeper"

def kro(i,j):
    return(1 if i==j else 0)

def on_corner(i,j, xmax, ymax):
    return((i==0 and j == 0) or (i==0 and j == ymax-1) or (i == xmax-1 and j == 0) or (i == xmax-1 and j == ymax-1))

def wgen_random(n_mines, xmax, ymax):
    print(xmax,ymax)
    w = np.zeros((xmax,ymax))
    x,y = rnd.randint(0,xmax),rnd.randint(0,ymax)
    
    for p in range(n_mines):
        while w[x][y] == 1:
            x,y = rnd.randint(0,xmax),rnd.randint(0,ymax)
        w[x][y] = 1
            
    return(w)


def wgen_random_clean(n_mines,xmax=haut,ymax=larg):
    
    w = np.zeros((xmax,ymax))
    x,y = rnd.randint(0,xmax),rnd.randint(0,ymax)
    
    for p in range(n_mines):
        while w[x][y] == 1:
            x,y = rnd.randint(0,xmax), rnd.randint(0,ymax)
        w[x][y] = 1
            
    w_clean= np.zeros((xmax,ymax))
    
    if w[0][0] != 1:
        w_clean[0][0] = w[0][1] + w[1][0] + w[1][1]
    if w[xmax-1][0] != 1:
        w_clean[xmax-1][0] = w[xmax-1][1] + w[xmax-2][0] + w[xmax-2][1]
    if w[0][ymax-1] != 1:
        w_clean[0][ymax-1] = w[1][ymax-1] + w[xmax-2][0] + w[xmax-2][1]
    if w[xmax-1][ymax-1] != 1:
        w_clean[xmax-1][ymax-1] = w[xmax-2][ymax-1] + w[xmax-1][ymax-2] + w[xmax-2][ymax-2]
    
    for x in range(xmax):
        for y in range(ymax):
            if w[x][y] == 1:
                w_clean[x][y] = -1
            else:
                if not(on_corner(x,y, xmax, ymax)) and w[x][y] != 1 and (x==0 or y==0 or x==xmax-1 or y==ymax-1):
                    if x==0:
                        w_clean[x][y] = w[x][y-1] + w[x][y+1] + w[x+1][y-1] + w[x+1][y] + w[x+1][y+1]
                    if x==xmax-1:
                        w_clean[x][y] = w[x][y-1] + w[x][y+1] + w[x-1][y-1] + w[x-1][y] + w[x-1][y+1]
                    if y==0:
                        w_clean[x][y] = w[x-1][y] + w[x+1][y] + w[x-1][y+1] + w[x][y+1] + w[x+1][y+1]
                    if y==ymax-1:
                        w_clean[x][y] = w[x-1][y] + w[x+1][y] + w[x-1][y-1] + w[x][y-1] + w[x+1][y-1]
                elif not(on_corner(x,y, xmax, ymax)) and w[x][y] != 1:
                    w_clean[x][y] = w[x][y-1] + w[x][y+1] + w[x+1][y-1] + w[x+1][y] + w[x+1][y+1] + w[x-1][y-1] + w[x-1][y] + w[x-1][y+1]
                else:
                    continue
    return(w_clean)                        







