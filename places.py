import random
import sys

def Game():
    """
    Starts the Game module
    """

    
    def Grid():
    """
    Creates the grid implementation filled with 0's, b's, and tc's
    """

        #Grid list 
        grid = []
        
        """
        #Creating a 8x8 grid initially filled with 0's
        for r in range(8):
            grid.append([])
            for c in range(8):
                grid[r].append(0)
        """

        """
        Alternate Code
        :Creates a 8 x 8 grid filled with 0's
        """ 
        grid = [[0] * 8 ] * 8

        """
        Creates 5 number of "b"'s in the grid
        """
        """
        for b in range(0,5):
           
            rowno = random.randint(0,7)
            colno = random.randint(0,7)          
            bno = "b"
            grid[rowno][colno] = bno
        """

        """
        Alternate Code
        :Creates 5 number of "b"'s in the grid
        """ 
        bcount = 0
        while bcount <= 5:
            #Pair of random coordinates for place in the grid
            rowcoord, colcoord = random.randint(0, 7), random.randint(0, 7)
            #Checks if the random coordinate hold only the 0 value and don't overlap the coordinates of b's in the grid
            if grid[rowcoord][colcoord] == 0:
                grid[rowcoord][colcoord] = "b"
                bcount += 1
      
        
        """
        for t in range(0,10):
            rno = random.randint(0,7)
            cno = random.randint(0,7)
            
            tno = grid[rno][cno]

            if tno == "b" and tno != 0:
                while tno == "b" and tno != 0:
                    rno = random.randint(0,7)
                    cno = random.randint(0,7)
                    tno = grid[rno][cno]
                    if tno != "b" and tno == 0:
                        tno = "tc"
                        grid[rno][cno] = tno
                        
            else:
                grid[rno][cno] = "tc"
        """  

        """
        Alternate Code
        :Creates 10 number of "tc"'s in the grid
        """ 
        tccount = 0
        while tccount <= 10:
            #Pair of random coordinates for place in the grid
            rowcoord, colcoord = random.randint(0, 7), random.randint(0, 7)
            #Checks if the random coordinate hold only the 0 value and don't overlap the coordinates of tc's in the grid
            if grid[rowcoord][colcoord] == 0:
                grid[rowcoord][colcoord] = "tc"
                tccount += 1

#remove at the end of the game section
        for row_i in grid:
            for cell_i in row_i:
                print(cell_i, end = '\t')
            print()
            print('')
#remove at the end of the game section
                
        grid2 = []
        for r in range(8):
            grid2.append([])
            for c in range(8):
                grid2[r].append('*')

        grid2[7][0] = 'player'
                
        for row_i in grid2:
            for cell_i in row_i:
                print(cell_i, end = '\t')
            print()
            print('')

        def Move():
            print("Press the letters to choose directions and then type in the number of spaces you want to move")
            coins = 0
            hv = ["W","w","S","s"]
            lr = ["A","a","d","D"]
            while coins != 100:
                
                hventry = str(input("Enter the blocks you want to move up or down. Use the W or S key: "))
                while hventry not in hv:
                    hventry = str(input("Enter the blocks you want to move up or down. Use the W or S key: "))

                hvblockentry = int(input("Enter the number of blocks you want to move up or down. Should be less than 7: "))
                while hvblockentry > 7:
                    hvblockentry = int(input("Enter the number of blocks you want to move up or down. Should be less than 7: "))

                lrentry = str(input("Enter the blocks you want to move left or right. Use the A or D key: "))
                while lrentry not in lr:
                    lrentry = str(input("Enter the blocks you want to move left or right. Use the A or D key: "))
                
                lrblockentry = int(input("Enter the number of blocks you want to left up or right. Should be less than 7: "))
                while lrblockentry > 7:
                    lrblockentry = int(input("Enter the number of blocks you want to move left or right. Should be less than 7: "))

                for r in grid:
                    for c in r:
                        if c == 'player':
                            plposr = c
                            plpos = grid[r][plposr]
                            print (plpos)
                            
                for row in grid2:
                    for col in row:
                        if col == 'player':
                            plposr2 = col
                            plpos2 = grid[row][plposr2]                            
                            print(plpos2)                    

        Move()
    Grid()

menuinput = input(str("Do you want to Start or Quit the game? Press S or Q:"))

if menuinput == "S" or menuinput == "s":
    Game()
else:
    sys.exit()
