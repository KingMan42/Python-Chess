
#Write a function for each piece type that takes two cooridinates and checks to see if it is a legal move

#     Inputs
#sx = starting x coordinate
#fx = final x coordinate
#sy = starting y coordinate
#fy = final y coordinate

def knight(sx,sy,fx,fy):
    if((fx - sx) == 1 and (fy - sy) == 2):
        return True
    elif((fx - sx) == -1 and (fy - sy) == 2):
        return True
    elif((fx - sx) == -1 and (fy - sy) == -2):
        return True
    elif((fx - sx) == 1 and (fy - sy) == -2):
        return True
    elif((fx - sx) == 2 and (fy - sy) == 1):
        return True
    elif((fx - sx) == -2 and (fy - sy) == 1):
        return True
    elif((fx - sx) == -2 and (fy - sy) == -1):
        return True
    elif((fx - sx) == 2 and (fy - sy) == -1):
        return True
    else:
        return False

def pawn(sx, sy, fx, fy):
    if((fx - sx) == 0 and (fy - sy) == 1):
        return True
    elif((fx - sx) == 0 and (fy - sy) == -1):
        return True
    elif((sy) == 1 and (fy - sy) == 2) and ((fx - sx) == 0):
        return True
    elif((sy) == 6 and (fy - sy) == -2)and ((fx - sx) == 0):
        return True
    elif(((fx- sx) == 1 and ((fy - sy) == 1 or (fy - sy) == -1))):
        if cBoardData[fx][fy][0] == "W" or cBoardData[fx][fy][0] == "B":
          return True
        else:
          return False
    elif(((fx- sx) == -1 and ((fy - sy) == 1 or (fy - sy) == -1))):
        if cBoardData[fx][fy][0] == "W" or cBoardData[fx][fy][0] == "B":
          return True
        else:
          return False

def rook(sx, sy, fx, fy):
    if((fx - sx) > -7 and (fy- sy) == 0):
        return True
    elif((fx - sx) == 0 and (fy-sy) > -7):
        return True
    else:
        return False

def bishop(sx, sy, fx, fy):
    if((fx - sx) ==  (fy - sy)):
        return True
    elif((fx - sx) == -(fy - sy)):
        return True
    elif(-(fx - sx) == (fy - sy)):
        return True
    elif(-(fx - sx) == -(fy - sy)):
        return True
    else:
        return False

def queen(sx , sy, fx, fy):
    # Boss Bitch
    #if(((fy - sy) < 0) and ((fx - sx) == 0 or (fx - sx) ==
    pass
        
          

#Draws Board
def draw(cBoardData):
    
    print("      0    1    2    3    4    5    6    7  ")
    for y in range(8):
        print("     ---  ---  ---  ---  ---  ---  ---  --- ")
        print( str(y) + "   |"+cBoardData[0][y]+"|"+"|"+cBoardData[1][y]+"|"+"|"+cBoardData[2][y]+"|"+"|"+cBoardData[3][y]+"|"+"|"+cBoardData[4][y]+"|"+"|"+cBoardData[5][y]+"|"+"|"+cBoardData[6][y]+"|"+"|"+cBoardData[7][y]+"|")
    print("     ---  ---  ---  ---  ---  ---  ---  --- ")    


#Sets board data to starting positions
def start():
    x, y = 8, 8;
    cBoardData = [[0 for i in range(x)]for j in range(y)]
    for n in range(8):
        for m in range(8):
            cBoardData[m][n] = "   "
    cBoardData[0][0] = "WR "
    cBoardData[7][0] = "WR "
    cBoardData[1][0] = "WKn"
    cBoardData[6][0] = "WKn"
    cBoardData[2][0] = "WB "
    cBoardData[5][0] = "WB "
    cBoardData[3][0] = "WKi"
    cBoardData[4][0] = "WQ "
    for p in range(8):
        cBoardData[p][1] = "WP "
    cBoardData[0][7] = "BR "
    cBoardData[7][7] = "BR "
    cBoardData[1][7] = "BKn"
    cBoardData[6][7] = "BKn"
    cBoardData[2][7] = "BB "
    cBoardData[5][7] = "BB "
    cBoardData[3][7] = "BKi"
    cBoardData[4][7] = "BQ "
    for p in range(8):
        cBoardData[p][6] = "BP " 
    return cBoardData
    

def main():
    print("\t\t Welcome to Ryan and Daniel's Python Chess Game!\n")
    cBoardData = start()
    while(1):
        draw(cBoardData);
        
    
    #Take an input of which posistion piece you want to move

        valid_input = False;
        #Check to see if position is valid i.e is on the board and had a piece there and piece is white piece
        while(valid_input == False):
            p1pieceX, plpieceY = [int(x) for x in input("Enter the coordinate of which piece you would like to move (in the form x,y):").split(',')]
            print(p1pieceX, plpieceY)
            p1piece = [p1pieceX, plpieceY]
            if (p1piece[0] < 0 or p1piece[0] > 7):
                print( "Invalid Move")
            elif (p1piece[1] < 0 or p1piece[1] > 7):
                print( "Invalid Move")
            elif (cBoardData[p1piece[0]][p1piece[1]] == "   "):
                print( "Invalid Move")
##            elif(cBoardData[p1piece[0]][p1piece[1]][0] == "B"):
##                print( "Invalid Move")
            else:
                valid_input = True
        
        valid_input = False
    #Get input for where the player wants to move
        
        
        while(valid_input == False):
            p1moveX, plmoveY = [int(x) for x in input("Enter the coordinate of which place you would like to move to(in the form x,y):").split(',')]
            plmove = [p1moveX, plmoveY]
            if (plmove[0] < 0 or plmove[0] > 7):
                print( "Invalid Move")
            elif (plmove[1] < 0 or plmove[1] > 7):
                print( "Invalid Move")
            elif(cBoardData[plmove[0]][plmove[1]][0] == "W" or [plmove[1]][0] == "B"):
                print( "Invalid Move")
            else:
                valid_input = True


    #Move Piece in cBoardData
        piece_to_move = cBoardData[p1pieceX][plpieceY]
        cBoardData[p1pieceX][plpieceY] = "   "
        cBoardData[p1moveX][plmoveY] = piece_to_move
    #Draw board
    

main()
    

