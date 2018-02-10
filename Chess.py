import os
import ChessPieces as CP
#To Do:
## Add ability for pawn to take pieces
## Create a way to keep track of what pieces have been taken.
## Finish the king check function


'''
Bugs:
    
'''


#     Inputs
#sx = starting x coordinate
#fx = final x coordinate
#sy = starting y coordinate
#fy = final y coordinate


        
#*************************************
#*      Sets up board                *
#*************************************          

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
    is_whites_turn = True
    #Game Loop
    while(1):
        draw(cBoardData);
        
    
    #Take an input of which posistion piece you want to move

        valid_input_in = False
        valid_input_out = False

        #Check to see if input and output are legal
        while(valid_input_in == False and valid_input_out == False):
            plpieceX_start, plpieceY_start = [int(x) for x in input("Enter the coordinate of which piece you would like to move (in the form x,y):").split(',')]
            plpiece = [plpieceX_start, plpieceY_start]
            piece = cBoardData[plpieceX_start][plpieceY_start]
            if (piece[0] == "B" and is_whites_turn == True):
                print("Not your piece loser!")
            elif (piece[0] == "W" and is_whites_turn == False):
                print("Dude...not your piece")
            elif (plpiece[0] < 0 or plpiece[0] > 7):
                print( "Invalid Piece")
            elif (plpiece[1] < 0 or plpiece[1] > 7):
                print( "Invalid Piece")
            elif (cBoardData[plpiece[0]][plpiece[1]] == "   "):
                print( "Invalid Piece")
            else:
                valid_input_in = True

            #If input is good check output
            if(valid_input_in == True):
                plmoveX_finish, plmoveY_finish = [int(x) for x in input("Enter the coordinate of which place you would like to move to(in the form x,y):").split(',')]
                plmove = [plmoveX_finish, plmoveY_finish]
                if (plmove[0] < 0 or plmove[0] > 7):
                    print( "Invalid Move")
                    valid_input_in = False
                elif (plmove[1] < 0 or plmove[1] > 7):
                    print( "Invalid Move")
                    valid_input_in = False
                elif(cBoardData[plmove[0]][plmove[1]][0] == "W"):
                    if is_whites_turn == True:
                        print("You can't take your own piece!")
                        valid_input_in = False
                    else:
                        valid_input_out = True
                elif(cBoardData[plmove[0]][plmove[1]][0] == "B"):
                    if is_whites_turn == False:
                        print("You can't take your own piece!")
                        valid_input_in = False
                    else:
                        valid_input_out = True
                else:
                    valid_input_out = True


        #Checks if pieces are in the way.
        blocked = CP.check_block(cBoardData, piece, plpieceX_start, plpieceY_start, plmoveX_finish, plmoveY_finish, is_whites_turn)
        

        #Checks the legality of the attempted move against the pieces mobility
        can_the_piece_move = CP.valid_move(piece, plpieceX_start, plpieceY_start, plmoveX_finish, plmoveY_finish, is_whites_turn)
       

    
        

        ###  Clear the screen to remove the clutter.
        #### This doesn't work in the shell, only cmd prompt.
        #os.system('cls')



        #Move Piece in cBoardData if allowed
        if can_the_piece_move == False:
            print("\n\n\n Sorry! I don't think you can move like that. \n\n\n")
        elif blocked == True:
            print("\n\n\n Sorry, you've got a piece in your way.\n\n\n")
        else:
            piece_to_move = cBoardData[plpieceX_start][plpieceY_start]
            cBoardData[plpieceX_start][plpieceY_start] = "   "
            cBoardData[plmoveX_finish][plmoveY_finish] = piece_to_move
            is_whites_turn = not(is_whites_turn)
    

main()



