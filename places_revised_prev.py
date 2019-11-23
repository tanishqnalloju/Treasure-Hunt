import random
import sys


def check_place(grid, rowcoord, colcoord):
    """
    Check if the given coordinates represent an empty cell and the starting position or not
    """
    #print(grid[rowcoord][colcoord], grid)
    if grid[rowcoord][colcoord] == 0 and rowcoord != 7 and colcoord != 0:
        return True
    
    return False

def print_grid(grid):
    for row_i in grid:
        for cell_i in row_i:
            print(cell_i, end = '\t')
        print()
        print('')


def Game():
    """
    Starts the Game module
    """

    
    def Grid():
        """
        Creates the grid implementation filled with 0's, b's, and tc's
        """
        
        #Grid list 
        """
        Alternate Code
        :Creates a 8 x 8 grid filled with 0's
        """ 
        grid = [[0]*8 for num in range(8)]
        """
        for num in range(8):
            grid.append([0] * 8) 
        """
        print(grid)
        
        """
        Alternate Code
        :Creates 5 number of "b"'s in the grid
        """         
        bcount = 0
        while bcount < 5:
            #Pair of random coordinates for place in the grid
            rowcoord, colcoord = random.randint(0, 7), random.randint(0, 7)
            #Checks if the random coordinate hold only the 0 value and don't overlap the coordinates of b's in the grid
            if check_place(grid, rowcoord, colcoord):
                grid[rowcoord][colcoord] = "b"
                bcount += 1       
            

        """
        Alternate Code
        :Creates 10 number of "tc"'s in the grid
        """         
        tccount = 0
        while tccount < 10:
            #Pair of random coordinates for place in the grid
            rowcoord, colcoord = random.randint(0, 7), random.randint(0, 7)
            #Checks if the random coordinate hold only the 0 value and don't overlap the coordinates of tc's in the grid
            #print(rowcord, colcord)
            if check_place(grid, rowcoord, colcoord):
                grid[rowcoord][colcoord] = "tc"
                tccount += 1
            
        
        #remove at the end of the game sections
        print_grid(grid)
        
        #remove at the end of the game section
                
        #grid2 = [["*"] * 8 ] * 8
        grid2 = []
        for num in range(8):
            grid2.append(["*"] * 8) 

        grid2[7][0] = 'p'
                
        print_grid(grid2)

    
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
                        if c == 'p':
                            plposr = c
                            plpos = grid[r][plposr]
                            print (plpos)
                            
                for row in grid2:
                    for col in row:
                        if col == 'p':
                            plposr2 = col
                            plpos2 = grid[row][plposr2]                            
                            print(plpos2)                    

    Grid()
    Move()

menuinput = input("Do you want to Start or Quit the game? Press Enter else Q to quit")

if menuinput != "q" or menuinput != "Q":
    Game()
else:
    exit()
