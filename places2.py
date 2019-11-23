from tkinter import *
import tkinter as tk
import random

root = tk.Tk()
label = Label(root, text = "Treasure Hunt")
label.pack()

topFrame = Frame(root)
topFrame.pack()

botFrame = Frame(root)
botFrame.pack(side = BOTTOM)

t = Toplevel(root)

class Game():
    
    def Grid():
        grid = []
        for r in range(8):
            grid.append([])
            for c in range(8):
                grid[r].append(0)

        #player generated
        grid[7][0] = "player"
            
        #treasure chest generated
                
        #bandit generated
        for b in range(5):
            rowno = random.randint(0,7)
            colno = random.randint(0,7)
            
            bno = grid[rowno][colno]

            if bno == "player" and bno != 0:
                while bno == "player":
                    rowno = random.randint(0,7)
                    colno = random.randint(0,7)
                    bno = grid[rowno][colno]
                    if bno != "player" and bno == 0:
                        bno = "b"
                        grid[rowno][colno] = bno
                        
            else:
                grid[rowno][colno] = "b"
                
        for t in range(10):
            rno = random.randint(0,7)
            cno = random.randint(0,7)
            
            tno = grid[rno][cno]

            if tno == "b" and tno == "player" and tno != 0:
                while tno == "player" and tno == "b":
                    rno = random.randint(0,7)
                    cno = random.randint(0,7)
                    tno = grid[rno][cno]
                    if tno != "player" and tno != "b" and tno == 0:
                        tno = "tc"
                        grid[rno][cno] = tno
                        
            else:
                grid[rno][cno] = "tc"


        #print randomly generated grid
        print (grid)

        def places():

            rownum = 0
            colnum = 0


            for row_i in range(8):
##                print (row_i)
                row_in = grid[row_i]
                for col_i in range(8):
##                    print (col_i)
                    print (grid[row_i][col_i])
                    Label(root, text= str(grid[row_i][col_i])).grid(row = rownum, column = colnum)
                    colnum = colnum + 1
                rownum = rownum + 1

        places()

##        for row_i in grid:
##            for cell_i in row_i:
##                print(cell_i, end = '\t')
##            print()
            
##        for row_index, row in enumerate(grid):
##            for cell_index, cell in enumerate(row):
##                grd = tk.Button(root, text = cell, width = 5)
##                grd.grid(row = row_index, column = cell_index)
##                         
    startbutton = Button(None, text = "Start",fg = "Black", command = Grid)
    startbutton.pack(side = LEFT, fill = X )

    def Quit_Game():
        root.destroy()

    quitbutton = Button(None, text = "Quit Game", fg = "Red", command = Quit_Game)
    quitbutton.pack(side = RIGHT, fill = Y)

    root.mainloop

Game()
