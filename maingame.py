import random
import sys

def print_grid(g):
    for row_i in g:
            for cell_i in row_i:
                print(cell_i, end = '\t')
            print()
            print('')

def check_place(grid, rowcoord, colcoord):
    if grid[rowcoord][colcoord] == 0 and rowcoord != 7 and colcoord != 0:
        return True
    
    return False

def Game():
    
    def Grid():

        #Adds land to the grid which is a list
        grid = [[0]*8 for num in range(8)]

        #Places bandits in grid
        bcount = 1
        while bcount < 6:
            rowno = random.randint(0,7)
            colno = random.randint(0,7)
            if check_place(grid, rowno, colno):
                grid[rowno][colno] = "b"
                bcount += 1

        #Places chests in grid
        tccount = 1
        while tccount < 11:
            rno = random.randint(0,7)
            cno = random.randint(0,7)
            
            if check_place(grid, rno, cno):
                grid[rno][cno] = "tc"
                tccount += 1

        #the grid shown to the player which will be compared to the original grid
        grid2 = []
        #adds the values that are going into the grid that is shown to the player
        grid2 = [["*"]*8 for num in range(8)]

        #Places the player into the board
        grid2[7][0] = 'player'

        #prints the list in a grid form
        print_grid(grid)
        print_grid(grid2)

        def Move():
            print("Press the letter keys on the keyboard to choose directions and then type in the number of spaces you want to move")
            #the coins variable to count the number of coins
            coins = 0
            moves = 0

            #Letters for direction
            hv = ["W","w","S","s"]
            lr = ["A","a","d","D"]

            tcnum = 0
            bnum = 0
#Count the treasure chests and bandits
            for r in grid:
                for c in r:
                    if c == "tc":
                        tcnum += 1
                    elif c == "b":
                        bnum += 1

            print (tcnum, "treasure chests")
            print(bnum, "bandits")
            
            #While coins aren't equal to 15 bandits and 0 treasure chests, the code will keep running
            while bnum != 15 and tcnum != 0:
                
                rownum = 0
                colnum = 0

                
                for row in grid2:
                    for col in row:
                        if col == 'player':
                            plposr = rownum
                            plposc = colnum
                            break
                        colnum += 1
                    colnum = 0
                    rownum += 1

                print(plposr,plposc)

                plposr2 = plposr
                plposc2 = plposc

                hventry = str(input("Use the W or S key to move up or down: "))
                while hventry not in hv:
                    hventry = str(input("Enter the blocks you want to move up or down. Use the W or S key: "))

                hvblockentry = int(input("Enter the number of blocks you want to move up or down. Should be less than 7: "))
                while hvblockentry > 7:
                    hvblockentry = int(input("Enter the number of blocks you want to move up or down. Should be less than 7: "))

                #checks if the direction entered is in the list 'hv'
                if hventry in hv:
                    #runs the code if the direction is up
                    if hventry == "w" or hventry == "W":
                        #if the player is on the up edge of the grid
                        if plposr == 0:
                            #until the player presses the letter to go down
                            hvblockentry = 0
                        #if the player is not on the edge of the grid
                        elif plposr != 0:
                            #plposr2 is used to check if the final value will go behind the grid
                            plposr2 = plposr2 - hvblockentry
                            #while the final place of the player is not beyond the grid
                            while plposr2 > 7 or plposr2 < 0:
                                hvblockentry = int(input("Enter the number of blocks you want to move up. Decrease the number: "))
                                plposr2 = plposr
                                plposr2 = plposr2 - hvblockentry
                            #if the player is not going to the edge of the grid
                            else:
                                grid2[plposr][plposc] = "*"
                                plposr = plposr2
                                grid2[plposr][plposc] = 'player'
                                print(plposr,plposc)                                   
                        
                   #runs the code if the direction is down
                    elif hventry =="s" or hventry == "S":
                        #if the player is on the edge of the grid
                        if plposr == 7:
                            hvblockentry = 0
                        #if the player is not on the bottom edge of the grid
                        elif plposr != 7:
                            #plposr2 is used to check if the final value will go behind the grid
                            plposr2 = plposr2 + hvblockentry
                            #while the final place of the player is not beyond the grid
                            while plposr2 > 7 or plposr2 < 0:
                                hvblockentry = int(input("Enter the number of blocks you want to move down. Decrease the number: "))
                                plposr2 = plposr
                                plposr2 = plposr2 + hvblockentry
                            #if the player is not going to the edge of the grid
                            else:
                                grid2[plposr][plposc] = "*"
                                plposr = plposr2
                                print(plposr,plposc)
                                grid2[plposr][plposc] = 'player'
                print(plposr,plposc)
                  

                lrentry = str(input("Enter the blocks you want to move left or right. Use the A or D key: "))
                while lrentry not in lr:
                    lrentry = str(input("Enter the blocks you want to move left or right. Use the A or D key: "))
                    #if statement to check whether player is at end of the grid. col
                
                lrblockentry = int(input("Enter the number of blocks you want to left up or right. Should be less than 7: "))
                while lrblockentry > 7:
                    lrblockentry = int(input("Enter the number of blocks you want to move left or right. Should be less than 7: "))
                    #if statement to check whether player is at end of the grid. col

                if lrentry in lr:
                    if lrentry == "A" or lrentry == "a":
                        #if the player is on the up edge of the grid
                        if plposc == 0:
                            #until the player presses the letter to go right
                            lrblockentry = 0
                        #if the player is not on the edge of the grid
                        elif plposc != 0:
                            #plposr2 is used to check if the final value will go behind the grid
                            plposc2 = plposc2 - lrblockentry
                            #while the final place of the player is not beyond the grid
                            while plposc2 > 7 or plposc2 < 0:
                                lrblockentry = int(input("Enter the number of blocks you want to move up. Decrease the number: "))
                                plposc2 = plposc
                                plposc2 = plposc2 - lrblockentry
                            #if the player is not going to the edge of the grid
                            else:
                                grid2[plposr][plposc] = "*"
                                plposc = plposc2
                                grid2[plposr][plposc] = 'player'
                                print(plposr,plposc)
                                
                    elif lrentry == "D" or lrentry == "d":
                        #if the player is on the up edge of the grid
                        if plposc == 7:
                            #until the player presses the letter to go left
                            lrblockentry = 0
                        #if the player is not on the edge of the grid
                        elif plposc != 7:
                            #plposr2 is used to check if the final value will go behind the grid
                            plposc2 = plposc2 + lrblockentry
                            #while the final place of the player is not beyond the grid
                            while plposc2 > 7 or plposc2 < 0:
                                lrblockentry = int(input("Enter the number of blocks you want to move up. Decrease the number: "))
                                plposc2 = plposc
                                plposc2 = plposc2 + lrblockentry
                            #if the player is not going to the edge of the grid
                            else:
                                grid2[plposr][plposc] = "*"
                                plposc = plposc2
                                grid2[plposr][plposc] = 'player'
                                print(plposr,plposc)
                            
                moves += 1

                #if the position of the player is on a treasure chest
                if grid[plposr][plposc] == "tc":
                    coins += 10
                    print("You have",coins,"coins.")
                #if the position of the player is on a bandit
                elif grid[plposr][plposc] == "b":
                    coins = 0
                    print("A bandit has stolen all you coins. You have 0 coins.")
                else:
                    print("You have",coins,"coins.")                    

                #shows the grid to the player                                  
                for row_i in grid2:
                    for cell_i in row_i:
                        print(cell_i, end = '\t')
                    print()
                    print('')

        Move()
    Grid()

menuinput = input(str("Do you want to Start or Quit the game? Press S or Q:"))

if menuinput == "S" or menuinput == "s":
    Game()
elif menuinput == "Q" or menuinput == "q":
    print ("You have decided to exit the game.")
    sys.exit()
else:
    while menuinput != "s" and menuinput != "S" and menuinput != "Q" and menuinput != "q":
        menuinput = input(str("Do you want to Start or Quit the game? Press S or Q:"))
        if menuinput == "S" or menuinput == "s":
            Game()
        elif menuinput == "Q" or menuinput == "q":
            sys.exit()