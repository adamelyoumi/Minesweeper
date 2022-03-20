# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 15:14:22 2021

@author: adame
"""

import numpy as np
import numpy.random as rnd

larg = 10
haut = 10

def wgen_random(n_mines, xmax=haut, ymax=larg):

    w = np.zeros((xmax,ymax))
    x,y = rnd.randint(0,xmax),rnd.randint(0,ymax)
    
    for p in range(n_mines):
        while w[x][y] == 1:
            x,y = rnd.randint(0,xmax),rnd.randint(0,ymax)
        w[x][y] = 1
            
    return(w) # w is an array that contains a number of 1s equal to n_mines (the rest being all 0s)


def wgen_random_clean(n_mines,xmax=haut,ymax=larg):

    w = wgen_random(n_mines,xmax,ymax)

    w_clean= np.zeros((xmax,ymax))
    
    # Dealing with corners
    if w[0][0] != 1:
        w_clean[0][0] = w[0][1] + w[1][0] + w[1][1]
    else:
        w_clean[0][0] = -1

    if w[xmax-1][0] != 1:
        w_clean[xmax-1][0] = w[xmax-1][1] + w[xmax-2][0] + w[xmax-2][1]
    else:
        w_clean[xmax-1][0] = -1

    if w[0][ymax-1] != 1:
        w_clean[0][ymax-1] = w[1][ymax-1] + w[0][ymax-2] + w[xmax-2][1]
    else:
        w_clean[0][ymax-1] = -1

    if w[xmax-1][ymax-1] != 1:
        w_clean[xmax-1][ymax-1] = w[xmax-2][ymax-1] + w[xmax-1][ymax-2] + w[xmax-2][ymax-2]
    else:
        w_clean[xmax-1][ymax-1] = -1
    

    for x in range(1,xmax-1):

        # Dealing with left and right edges
        if w[x][0] == 1:
            w_clean[x][0] = -1
        else:
            w_clean[x][0] = w[x-1][0] + w[x+1][0] + w[x-1][1] + w[x][1] + w[x+1][1]

        if w[x][ymax-1] == 1:
            w_clean[x][ymax-1] = -1
        else:
            w_clean[x][ymax-1] = w[x-1][ymax-1] + w[x+1][ymax-1] + w[x-1][ymax-2] + w[x][ymax-2] + w[x+1][ymax-2]

    for y in range(1,ymax-1):

        # Dealing with top and bottom edges
        if w[0][y] == 1:
            w_clean[0][y] = -1
        else:
            w_clean[0][y] = w[0][y-1] + w[0][y+1] + w[1][y-1] + w[1][y] + w[1][y+1]

        if w[xmax-1][y] == 1:
            w_clean[xmax-1][y] = -1
        else:
            w_clean[xmax-1][y] = w[xmax-1][y-1] + w[xmax-1][y+1] + w[xmax-2][y-1] + w[xmax-2][y] + w[xmax-2][y+1]

    for x in range(1,xmax-1):
        for y in range(1,ymax-1):
            if w[x][y] == 1:
                w_clean[x][y] = -1
            else:
                w_clean[x][y] = w[x][y-1] + w[x][y+1] + w[x+1][y-1] + w[x+1][y] + w[x+1][y+1] + w[x-1][y-1] + w[x-1][y] + w[x-1][y+1]

    return(w_clean)                        







