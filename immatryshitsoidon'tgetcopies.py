import random
import sys

def Game():
    
    def Grid():
        #grid is a list
        grid = []

        #Adds land to the grid
        for r in range(8):
            grid.append([])
            for c in range(8):
                grid[r].append(0)

        #Places bandits in grid
        for b in range(0,5):
            rowno = random.randint(0,7)
            colno = random.randint(0,7)
            bno = "b"

            grid[rowno][colno] = bno

        #Places chests in grid
        for t in range(0,10):
            rno = random.randint(0,7)
            cno = random.randint(0,7)
            
            tno = grid[rno][cno]

            if tno == "b" and tno != 0 and tno != "tc":
                while tno == "b" and tno != 0 and tno != "tc":
                    rno = random.randint(0,7)
                    cno = random.randint(0,7)
                    tno = grid[rno][cno]
                    if tno != "b" and tno != "tc" and tno == 0:
                        tno = "tc"
                        grid[rno][cno] = tno
                        
            else:
                grid[rno][cno] = "tc"

        #the grid shown to the player which will be compared to the original grid
        grid2 = []
        #adds the values that are going into the grid that is shown to the player
        for r in range(8):
            grid2.append([])
            for c in range(8):
                grid2[r].append('*')

        #Places the player into the board
        grid2[7][0] = 'player'

        #prints the list in a grid form
        for row_i in grid2:
            for cell_i in row_i:
                print(cell_i, end = '\t')
            print()
            print('')

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

            print (tcnum)
            print(bnum)
            
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
                            while plposr2 > 8 or plposr2 < -1:
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
                            #until the player presses the letter to go up
                            hvblockentry = 0
                        #if the player is not on the bottom edge of the grid
                        elif plposr != 7:
                            #plposr2 is used to check if the final value will go behind the grid
                            plposr2 = plposr2 + hvblockentry
                            #while the final place of the player is not beyond the grid
                            while plposr2 > 8 or plposr2 < -1:
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
                            while lrentry != "d" or lrentry != "D":
                                lrblockentry = 0
                        #if the player is not on the edge of the grid
                        elif plposc != 0:
                            #plposr2 is used to check if the final value will go behind the grid
                            plposc2 = plposc2 - lrblockentry
                            #while the final place of the player is not beyond the grid
                            while plposc2 > 7 or plposc2 < -1:
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
                            while plposc2 > 7 or plposc2 < -1:
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