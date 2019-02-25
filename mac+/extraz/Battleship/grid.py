from random import randint
 
# this a battleship grid oject
class GameGrid(object):
    # this creates the battleship oject 
    def __init__(self):
        # this code creates the ten by ten grid 
        self.grid = [[0]*10 for i in range(10)]
        # this inserts the grid cordinates
        for x in range(0,10):
            for y in range(0,10):
                self.grid[x][y] = str(x) + str(chr(y+65))
                
    # this function prints the grid 
    def print_grid(self):
        print()
        print("---------------------------------------------------")
        for row in self.grid:
            print("| ", end='')
            for col in row:
                print( str(col)+" | ", end='')
            print()
            print("---------------------------------------------------")
        print()
        
        
        
    def place_point(self, x = 0, y = 0):
        
        self.grid [x][y] = " O"
        
        


# AI = GameGrid()
# AE = GameGrid()

# ss = randint(0, 1)
# print(ss)
# test = True

# if ( test == True ):
     
#     if ss == 0: 
#         num_x = randint(0,9)
#         num_y = randint(0, 4)
     
#         for i in range(0,5):
#             num_y+=1
        
#             AI.place_point(num_x, num_y)
#     else:
#         num_y = randint(0,9)
#         num_x = randint(0, 4)
     
#         for i in range(0,5):
#             num_x+=1
        
#             AI.place_point(num_x, num_y)
        
        
# AI.print_grid()  


# ssi = randint(0, 1)
# print(ss)
# tist = True

# if ( tist == True ):
     
#     if ss == 0: 
#         numt_x = randint(0,9)
#         numt_y = randint(0, 4)
     
#         for i in range(0,5):
#             numt_y+=1
        
#             AE.place_point(numt_x, numt_y)
#     else:
#         numt_y = randint(0,9)
#         numt_x = randint(0, 4)
     
#         for i in range(0,5):
#             numt_x+=1
        
#             AE .place_point(numt_x, numt_y)        

# AE.print_grid()  







