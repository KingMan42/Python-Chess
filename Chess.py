
#Write a function for each piece type that takes two cooridinates and checks to see if it is a legal move

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



#Draws Board
def draw(cBoardData):
    
    print"      0    1    2    3    4    5    6    7  "
    for y in range(8):
        print"     ---  ---  ---  ---  ---  ---  ---  --- "
        print str(y) + "   |"+cBoardData[0][y]+"|"+"|"+cBoardData[1][y]+"|"+"|"+cBoardData[2][y]+"|"+"|"+cBoardData[3][y]+"|"+"|"+cBoardData[4][y]+"|"+"|"+cBoardData[5][y]+"|"+"|"+cBoardData[6][y]+"|"+"|"+cBoardData[7][y]+"|"
    print"     ---  ---  ---  ---  ---  ---  ---  --- "    


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
            p1piece = input("Enter the coordinate of which piece you would like to move (in the form x,y):")
            if (p1piece[0] < 0 or p1piece[0] > 7):
                print "Invalid Move"
            elif (p1piece[1] < 0 or p1piece[1] > 7):
                print "Invalid Move"
            elif (cBoardData[p1piece[0]][p1piece[1]] == "   "):
                print "Invalid Move"
            elif(cBoardData[p1piece[0]][p1piece[1]][0] == "B"):
                print "Invalid Move"
            else:
                valid_input = True
        
        valid_input = False
    #Get input for where the player wants to move
        
        
        while(valid_input == False):
            p1move = input("Enter the coordinate of which place you would like to move to(in the form x,y):")
            if (p1move[0] < 0 or p1move[0] > 7):
                print "Invalid Move"
            elif (p1move[1] < 0 or p1move[1] > 7):
                print "Invalid Move"
            elif(cBoardData[p1move[0]][p1move[1]][0] == "W"):
                print "Invalid Move"
            else:
                valid_input = True


    #Move Piece in cBoardData

    #Draw board

main()
    

