
#****************************************************************
#    Piece functions that return if move is valid for piece
#****************************************************************


def knight(sx,sy,fx,fy):
    if (abs(fx - sx) == 1 and abs(fy - sy) == 2):
        return True
    elif (abs(fx - sx) == 2 and abs(fy - sy) == 1):
        return True
    else:
        return False


def pawn(sx, sy, fx, fy):
    if((fx - sx) == 0 and abs(fy - sy) == 1):
        return True
    elif((sy) == 1 and (fy - sy) == 2) and ((fx - sx) == 0):
        return True
    elif((sy) == 6 and (fy - sy) == -2)and ((fx - sx) == 0):
        return True
    #Add check for diagnal move if opposing piece there. 
    else:
        return False

def rook(sx, sy, fx, fy):
    if((fx - sx) != 0 and (fy - sy) == 0):
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
    if (fx - sx) == 0:
        return True
    elif (fy - sy) == 0:
        return True
    elif(abs(fx - sx) ==  abs(fy - sy)):
        return True
    else:
        return False


def king(cBoardData, sx, sy, fx, fy, is_whites_turn):
    #Check that the move is only one spot
    oneSpot = False
    
    if(abs(fx-sx) <= 1):
        if(abs(fy-sy) <= 1):
            oneSpot = True

    
    #Create Copy of Current Board;
    cBoardCopy = cBoardData
    

    #In copy move the king
    king = cBoardData[sx][sy]
    cBoardCopy[sx][sy] = "   "
    cBoardCopy[fx][fy] = king


    if(king_in_check(cBoardCopy,fx,fy) == False):
        return True







#*****************************************************
#*  Functions related to piece movements             *
#*****************************************************


#Will check all pieces and see if they can attack king in one move
def king_in_check(cBoardData,kx,ky, is_whites_turn):
    #Get color of piece
    colour = cBoardData[kx][ky][0]
    #Loop through all other opposing team pieces and see if they can move to kings spot
    for n in range(8):
        for m in range(8):
            if(cBoardData[n][m][0] != colour and cBoardData[n][m][0] != " "):
                if(valid_move(cBoardData[n][m], n, m, kx, ky) == True and check_block(cBoardData, cBoardData[n,m],kx,ky,is_whites_turn)):
                    return True
                    
                #cBoardData, piece, plpieceX_start, plpieceY_start, plmoveX_finish, plmoveY_finish,is_whites_turn
             
#Encapsating function to check if a piece can move based on a pieces rules.
def valid_move(piece, plpieceX_start, plpieceY_start, plmoveX_finish, plmoveY_finish, is_whites_turn):
    
    if piece[1] == "R":
            can_the_piece_move = rook(plpieceX_start, plpieceY_start, plmoveX_finish, plmoveY_finish)
    elif piece[1] == "B":
            can_the_piece_move = bishop(plpieceX_start, plpieceY_start, plmoveX_finish, plmoveY_finish)
    elif piece[1] == "K" and piece[2] == "n":
            can_the_piece_move = knight(plpieceX_start, plpieceY_start, plmoveX_finish, plmoveY_finish)
    elif piece[1] == "K" and piece[2] == "i":
            can_the_piece_move = king(plpieceX_start, plpieceY_start, plmoveX_finish, plmoveY_finish, is_whites_turn)
    elif piece[1] == "P":
            can_the_piece_move = pawn(plpieceX_start, plpieceY_start, plmoveX_finish, plmoveY_finish)
    elif piece[1] == "Q":
            can_the_piece_move = queen(plpieceX_start, plpieceY_start, plmoveX_finish, plmoveY_finish)
    else:
            print("Sorry, not sure what piece you're moving. Blame Ryan")


    return can_the_piece_move




#***************************************************
#*  Functions for checking if piece is blocked     *
#***************************************************


#Check to see if path is blocked in a horizonal direction
def check_horizonal(cBoardData, plpieceX_start, plpieceY_start,plmoveX_finish, plmoveY_finish):
    blocked = False
    #Check which direction the piece is moving
    if ((plmoveX_finish - plpieceX_start) != 0):
        #Check all squares from starting spot to ending
        for x in range(abs(plmoveX_finish - plpieceX_start) - 1):
            if cBoardData[plpieceX_start + (x+1)][plpieceY_start][0] != " ":
                blocked = True
            elif cBoardData[plpieceX_start - (x+1)][plpieceY_start][0] != " ":
                blocked = True
    elif ((plmoveY_finish - plpieceY_start) != 0):
        for x in range(abs(plmoveY_finish - plpieceY_start) - 1):
            if((plmoveY_finish - plpieceY_start) > 0):
                if cBoardData[plpieceX_start][plpieceY_start + (x+1)][0] != " ":
                    blocked = True
            elif ((plmoveY_finish - plpieceY_start) < 0): 
                if cBoardData[plpieceX_start][plpieceY_start - (x+1)][0] != " ":
                    blocked = True
    return blocked


#Check to see if path is blocked in a diagonal direction
def check_diagonal(cBoardData, plpieceX_start, plpieceY_start,plmoveX_finish, plmoveY_finish):
    blocked = False
    diffX = plmoveX_finish
    diffY = plmoveY_finish
    if((plmoveX_finish - plpieceX_start) > 0):
        deltX = -1
    else:
        deltX = 1
    if((plmoveY_finish - plpieceY_start) > 0):
        deltY = -1
    else:
        deltY = 1

    for x in range(abs(plmoveX_finish - plpieceX_start) - 1):
        diffX = diffX + deltX
        diffY = diffY + deltY
        if cBoardData[diffX][diffY][0] != " ":
                blocked = True
        
       

    return blocked




def check_block(cBoardData, piece, plpieceX_start, plpieceY_start, plmoveX_finish, plmoveY_finish, is_whites_turn):
    blocked = False
#Rook
    if piece[1] == "R":
        blocked = check_horizonal(cBoardData, plpieceX_start, plpieceY_start,plmoveX_finish, plmoveY_finish)



#Pawn               
    if piece[1] == "P":
       #If whites turn check y positive else check y negative
        if(is_whites_turn == True):
            for x in range(abs(plmoveY_finish - plpieceY_start)):
                if(cBoardData[plpieceX_start][plpieceY_start + (x+1)][0] != " "):
                    blocked = True
        else:
            for x in range(abs(plmoveY_finish - plpieceY_start)):
                if(cBoardData[plpieceX_start][plpieceY_start - (x+1)][0] != " "):
                    blocked = True
 

#Bishop                
    if piece[1] == "B":
        blocked = check_diagonal(cBoardData, plpieceX_start, plpieceY_start,plmoveX_finish, plmoveY_finish) 
            

#Queen
    if piece[1] == "Q":

        #Find whether moving diagnolly or straight.
        if ((plmoveX_finish - plpieceX_start) == 0) or ((plmoveY_finish - plpieceY_start) == 0):
            blocked = check_horizonal(cBoardData, plpieceX_start, plpieceY_start,plmoveX_finish, plmoveY_finish)
        else:
            blocked = check_diagonal(cBoardData, plpieceX_start, plpieceY_start,plmoveX_finish, plmoveY_finish)
                
    return blocked

