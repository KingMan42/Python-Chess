import os

#To Do:
## CLEAN CODE
## Finish Pawn movement/taking other pieces.
## Create a way to keep track of what pieces have been taken.
## Finish the king check function
## A lot


#Finished Functions (that need testing):
##Knight
##Bishop
##Rook


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
    #elif((fx - sx) == 1 and (fy - sy) == 1):
    #Check for opposing piece
    #      return True
    #elif((fx - sx) == -1 and (fy - sy) == 1):
    #      return True
    #Check for opposing piece
    else:
        return False

def rook(sx, sy, fx, fy):
    if((fx - sx) != 0 (fy - sy) == 0):
        return True
    elif((fx - sx) == 0 and (fy - sy) != 0):
        return True
    else:
        return False

def bishop(sx, sy, fx, fy):
    if(abs(fx - sx) ==  abs(fy - sy)):
        return True
    else:
        return False

def queen(sx , sy, fx, fy):
    if (fx- sx) == 0:
        return True
    elif (fy - sy) == 0:
        return True
    elif((fx - sx) ==  (fy - sy)):
        return True
    elif((fx - sx) == -(fy - sy)):
        return True
    elif(-(fx - sx) == (fy - sy)):
        return True
    elif(-(fx - sx) == -(fy - sy)):
        return True
    else:
        return False

def king_in_check(cBoardData,kx,ky):
    #Get color of piece
    colour = cBoardData[kx][ky][0]
    #Loop through all other opposing team pieces and see if they can move to kings spot
        for n in range(8):
            for m in range(8):
                if(cBoardData[n][m][0] != colour):
                    can_the_piece_move = valid_move(cBoardData[n][m], n, m, kx, ky)
                    
                    
                    
    


def king(cBoardData,sx,sy,fx,fy):
    #Check that the move is only one spot
    oneSpot = False
    
    if(abs(fx-sx) <= 1):
        if(abs(fy-sy) <= 1):
            oneSpot = True

    
    #Create Copy of Current Board;
    cBoardCopy = cBoardData
    

    #In copy move the king
    cBoardCopy
    king = cBoardData[sx][sy]
    cBoardCopy[sx][sy] = "   "
    cBoardCopy[fx][fy] = king


    if(king_in_check(cBoardCopy,fx,fy) == False):
        return True
        
          

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
    
def check_block(cBoardData, piece, p1pieceX_start, plpieceY_start, p1moveX_finish, plmoveY_finish, is_whites_turn):
    blocked = False
#If Rook
    if piece[1] == "R":
        if ((p1moveX_finish - p1pieceX_start) != 0):
            for x in range(1,(abs(p1moveX_finish - p1pieceX_start))):
                #Can we change this to just (if cboardData... != " ")?
                if cBoardData[p1pieceX_start + x][plpieceY_start][0] == "W" or cBoardData[p1pieceX_start + x][plpieceY_start][0] =="B":
                    blocked = True
                elif cBoardData[p1pieceX_start - x][plpieceY_start][0] == "W" or cBoardData[p1pieceX_start - x][plpieceY_start][0] =="B":
                    blocked = True
        elif ((plmoveY_finish - plpieceY_start) != 0):
            for x in range( 1,(abs(plmoveY_finish - plpieceY_start))):
                if ((plmoveY_finish - plpieceY_start) > 0):
                    #Same as above. Plus shouldnt this be "+ y" and not "+ x" 
                    if cBoardData[p1pieceX_start][plpieceY_start + x][0] == "W" or cBoardData[p1pieceX_start][plpieceY_start + x][0] =="B":
                        blocked = True
                elif ((plmoveY_finish - plpieceY_start) < 0): 
                    if cBoardData[p1pieceX_start][plpieceY_start - x][0] == "W" or cBoardData[p1pieceX_start][plpieceY_start - x][0] =="B":
                        blocked = True
#If Pawn               
    if piece[1] == "P":
        if cBoardData[p1pieceX_start][plpieceY_start + 1][0] != " " and is_whites_turn == True and plpieceY_start == 1:
            blocked = True
        elif cBoardData[p1pieceX_start][plpieceY_start - 1][0] != " " and is_whites_turn == False and plpieceY_start == 6:
            blocked = True
        elif ((plmoveY_finish - plpieceY_start) > 0) and ((p1moveX_finish - p1pieceX_start) == 0) and cBoardData[p1pieceX_start][plpieceY_start + 1][0] != " ":
            blocked = True
        elif ((plmoveY_finish - plpieceY_start) < 0) and ((p1moveX_finish - p1pieceX_start) == 0) and cBoardData[p1pieceX_start][plpieceY_start - 1][0] != " ":
            blocked = True
        else:
            pass
#If bishop                
    if piece[1] == "B":
        if((p1moveX_finish - p1pieceX_start) > 0) and ((plmoveY_finish - plpieceY_start) > 0):
            for space in range(1, (abs(p1moveX_finish - p1pieceX_start))):
                if cBoardData[p1pieceX_start + space][plpieceY_start + space][0] == "W" or cBoardData[p1pieceX_start + space][plpieceY_start + space][0] == "B":
                    blocked = True
        elif((p1moveX_finish - p1pieceX_start) > 0) and ((plmoveY_finish - plpieceY_start) < 0):
            for space in range(1, (abs(p1moveX_finish - p1pieceX_start))):
                if cBoardData[p1pieceX_start + space][plpieceY_start - space][0] == "W" or cBoardData[p1pieceX_start + space][plpieceY_start - space][0] == "B":
                    blocked = True
        elif((p1moveX_finish - p1pieceX_start) < 0) and ((plmoveY_finish - plpieceY_start) > 0):
            for space in range(1, (abs(p1moveX_finish - p1pieceX_start))):
                if cBoardData[p1pieceX_start - space][plpieceY_start + space][0] == "W" or cBoardData[p1pieceX_start - space][plpieceY_start + space][0] == "B":
                    blocked = True
        elif((p1moveX_finish - p1pieceX_start) < 0) and ((plmoveY_finish - plpieceY_start) < 0):
            for space in range(1, (abs(p1moveX_finish - p1pieceX_start))):
                if cBoardData[p1pieceX_start - space][plpieceY_start - space][0] == "W" or cBoardData[p1pieceX_start - space][plpieceY_start - space][0] == "B":
                    blocked = True
        else:
            pass
                       
#If Queen
    if piece[1] == "Q":
        if ((p1moveX_finish - p1pieceX_start) == 0) or ((plmoveY_finish - plpieceY_start) == 0):
            if ((p1moveX_finish - p1pieceX_start) > 0 or (p1moveX_finish - p1pieceX_start < 0)):
                for x in range(1,(abs(p1moveX_finish - p1pieceX_start))):
                    if cBoardData[p1pieceX_start + x][plpieceY_start][0] == "W" or cBoardData[p1pieceX_start + x][plpieceY_start][0] =="B":
                        blocked = True
                    elif cBoardData[p1pieceX_start - x][plpieceY_start][0] == "W" or cBoardData[p1pieceX_start - x][plpieceY_start][0] =="B":
                        blocked = True
            elif ((plmoveY_finish - plpieceY_start) > 0) or ((plmoveY_finish - plpieceY_start) < 0):
                for x in range( 1,(abs(plmoveY_finish - plpieceY_start))):
                    if ((plmoveY_finish - plpieceY_start) > 0):
                        if cBoardData[p1pieceX_start][plpieceY_start + x][0] == "W" or cBoardData[p1pieceX_start][plpieceY_start + x][0] =="B":
                            print(x)
                            blocked = True
                    elif ((plmoveY_finish - plpieceY_start) < 0): 
                        if cBoardData[p1pieceX_start][plpieceY_start - x][0] == "W" or cBoardData[p1pieceX_start][plpieceY_start - x][0] =="B":
                            print(x)
                            blocked = True
                
        if (abs(p1moveX_finish - p1pieceX_start) > 0):
            if((p1moveX_finish - p1pieceX_start) > 0) and ((plmoveY_finish - plpieceY_start) > 0):
                for space in range(1, (abs(p1moveX_finish - p1pieceX_start))):
                    if cBoardData[p1pieceX_start + space][plpieceY_start + space][0] == "W" or cBoardData[p1pieceX_start + space][plpieceY_start + space][0] == "B":
                        blocked = True
            elif((p1moveX_finish - p1pieceX_start) > 0) and ((plmoveY_finish - plpieceY_start) < 0):
                for space in range(1, (abs(p1moveX_finish - p1pieceX_start))):
                    if cBoardData[p1pieceX_start + space][plpieceY_start - space][0] == "W" or cBoardData[p1pieceX_start + space][plpieceY_start - space][0] == "B":
                        blocked = True
            elif((p1moveX_finish - p1pieceX_start) < 0) and ((plmoveY_finish - plpieceY_start) > 0):
                for space in range(1, (abs(p1moveX_finish - p1pieceX_start))):
                    if cBoardData[p1pieceX_start - space][plpieceY_start + space][0] == "W" or cBoardData[p1pieceX_start - space][plpieceY_start + space][0] == "B":
                        blocked = True
            elif((p1moveX_finish - p1pieceX_start) < 0) and ((plmoveY_finish - plpieceY_start) < 0):
                for space in range(1, (abs(p1moveX_finish - p1pieceX_start))):
                    if cBoardData[p1pieceX_start - space][plpieceY_start - space][0] == "W" or cBoardData[p1pieceX_start - space][plpieceY_start - space][0] == "B":
                        blocked = True
            else:
                pass
    return blocked


def valid_move(piece, p1pieceX_start, p1pieceY_start, p1pieceX_finish, p1pieceY_finish):
    
    if piece[1] == "R":
            can_the_piece_move = rook(p1pieceX_start, plpieceY_start, p1moveX_finish, plmoveY_finish)
        elif piece[1] == "B":
            can_the_piece_move = bishop(p1pieceX_start, plpieceY_start, p1moveX_finish, plmoveY_finish)
        elif piece[1] == "K" and piece[2] == "n":
            can_the_piece_move = knight(p1pieceX_start, plpieceY_start, p1moveX_finish, plmoveY_finish)
        elif piece[1] == "K" and piece[2] == "i":
            can_the_piece_move = king(p1pieceX_start, plpieceY_start, p1moveX_finish, plmoveY_finish)
        elif piece[1] == "P":
            can_the_piece_move = pawn(p1pieceX_start, plpieceY_start, p1moveX_finish, plmoveY_finish)
        elif piece[1] == "Q":
            can_the_piece_move = queen(p1pieceX_start, plpieceY_start, p1moveX_finish, plmoveY_finish)
        else:
            print("Sorry, not sure what piece you're moving. Blame Ryan")


    return can_the_piece_move



def main():
    print("\t\t Welcome to Ryan and Daniel's Python Chess Game!\n")
    cBoardData = start()
    is_whites_turn = True
    while(1):
        draw(cBoardData);
        
    
    #Take an input of which posistion piece you want to move

        valid_input_in = False;
        #Check to see if position is valid i.e is on the board and had a piece there and piece is white piece
        while(valid_input_in == False):
            p1pieceX_start, plpieceY_start = [int(x) for x in input("Enter the coordinate of which piece you would like to move (in the form x,y):").split(',')]
            p1piece = [p1pieceX_start, plpieceY_start]
            piece = cBoardData[p1pieceX_start][plpieceY_start]
            if (piece[0] == "B" and is_whites_turn == True):
                print("Not your piece loser!")
            elif (piece[0] == "W" and is_whites_turn == False):
                print("Dude...not your piece")
            elif (p1piece[0] < 0 or p1piece[0] > 7):
                print( "Invalid Piece")
            elif (p1piece[1] < 0 or p1piece[1] > 7):
                print( "Invalid Piece")
            elif (cBoardData[p1piece[0]][p1piece[1]] == "   "):
                print( "Invalid Piece")
            else:
                valid_input_in = True
        #print(piece)

        
        
        valid_input_out = False
    #Get input for where the player wants to move
        
        
        while(valid_input_out == False):
            p1moveX_finish, plmoveY_finish = [int(x) for x in input("Enter the coordinate of which place you would like to move to(in the form x,y):").split(',')]
            plmove = [p1moveX_finish, plmoveY_finish]
            if (plmove[0] < 0 or plmove[0] > 7):
                print( "Invalid Move")
            elif (plmove[1] < 0 or plmove[1] > 7):
                print( "Invalid Move")
            elif(cBoardData[plmove[0]][plmove[1]][0] == "W"):
                if is_whites_turn == True:
                    print("You can't take your own piece!")
                else:
                    valid_input_out = True
            elif(cBoardData[plmove[0]][plmove[1]][0] == "B"):
                if is_whites_turn == False:
                    print("You can't take your own piece!")
                else:
                    valid_input_out = True
            else:
                valid_input_out = True

        #Checks if pieces are in the way.

        blocked = check_block(cBoardData, piece, p1pieceX_start, plpieceY_start, p1moveX_finish, plmoveY_finish,is_whites_turn)
        
            
                

        #Checks the legality of the attempted move against the pieces mobility
        can_the_piece_move = valid_move(piece, p1pieceX_start, p1pieceY_start, p1pieceX_finish, p1pieceY_finish)
       

        

                   

    #Move Piece in cBoardData if allowed

        ###  Clear the screen to remove the clutter.
        #### This doesn't work in the shell, only cmd prompt.
        #os.system('cls')

        if can_the_piece_move == False:
            print("\n\n\n Sorry! I don't think you can move like that. \n\n\n")
        elif blocked == True:
            print("\n\n\n Sorry, you've got a piece in your way.\n\n\n")
        else:
            piece_to_move = cBoardData[p1pieceX_start][plpieceY_start]
            cBoardData[p1pieceX_start][plpieceY_start] = "   "
            cBoardData[p1moveX_finish][plmoveY_finish] = piece_to_move
            is_whites_turn = not(is_whites_turn)
    #Draws board at start of loop
    

main()
