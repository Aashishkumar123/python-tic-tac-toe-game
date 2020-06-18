# importing suitable liabarires
import numpy as np
import time


# creating tic tac toe board
board = np.array([[1,2,3],[4,5,6],[7,8,9]], dtype=str)
print(board)

#player 1 Turn to play
player1 = int(input("Player1 Turn :"))

if player1 == 1 or player1 == 2 or player1 == 3:
    board[0][player1-1] = '0'
    print(board)
elif player1 == 4 or player1 == 5 or player1 == 6:
    board[1][player1-4] = '0'
    print(board)
elif player1 == 7 or player1 == 8 or player1 == 9:
    board[2][player1-7] = '0'
    print(board)
    
else:
    print("Wrong Choice !!")
    
    
#player 2 Turn to play
player2 = int(input("Player2 Turn :"))

if player2 == 1 or player2 == 2 or player2 == 3:
    board[0][player2-1] = "x"
    print(board)
elif player2 == 4 or player2 == 5 or player2 == 6:
    board[1][player2-4] = "x"
    print(board)
elif player2 == 7 or player2 == 8 or player2 == 9:
    board[2][player2-7] = "x"
    print(board)
else:
    print("Wrong Choice !!")


    
#player 1 Turn to play
player1 = int(input("Player1 Turn :"))

if player1 == 1 or player1 == 2 or player1 == 3:
    board[0][player1-1] = '0'
    print(board)
elif player1 == 4 or player1 == 5 or player1 == 6:
    board[1][player1-4] = '0'
    print(board)
elif player1 == 7 or player1 == 8 or player1 == 9:
    board[2][player1-7] = '0'
    print(board)
    
else:
    print("Wrong Choice !!")

    
#player 2 Turn to play
player2 = int(input("Player2 Turn :"))

if player2 == 1 or player2 == 2 or player2 == 3:
    board[0][player2-1] = "x"
    print(board)
elif player2 == 4 or player2 == 5 or player2 == 6:
    board[1][player2-4] = "x"
    print(board)
elif player2 == 7 or player2 == 8 or player2 == 9:
    board[2][player2-7] = "x"
    print(board)
else:
    print("Wrong Choice !!")

 
    
    
    
    
#player 1 Turn to play
player1 = int(input("Player1 Turn :"))

if player1 == 1 or player1 == 2 or player1 == 3:
    board[0][player1-1] = '0'
    print(board)
    
      #checking 3 zeros matching or not
    if board[0][0] == '0' and board[0][1] == '0' and board[0][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[1][0] == '0' and board[1][1]=='0' and board[1][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[2][0] == '0' and board[2][1] == '0' and board[2][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][0] == '0' and board[1][0] == '0' and board[2][0] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][1] == '0' and board[1][1] == '0' and board[2][1] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][2] == '0' and board[1][2] == '0' and board[2][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][0] == '0' and board[1][1] == '0' and board[2][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][2] == '0' and board[1][1] == '0' and board[2][0] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
        
        
elif player1 == 4 or player1 == 5 or player1 == 6:
    board[1][player1-4] = '0'
    print(board)
    
      #checking 3 zeros matching or not
    if board[0][0] == '0' and board[0][1] == '0' and board[0][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[1][0] == '0' and board[1][1] == '0' and board[1][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[2][0] == '0' and board[2][1] == '0' and board[2][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][0] == '0' and board[1][0] == '0' and board[2][0] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][1] == '0' and board[1][1] == '0' and board[2][1] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][2] == '0' and board[1][2] == '0' and board[2][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][0] == '0' and board[1][1] == '0' and board[2][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][2] == '0' and board[1][1] == '0' and board[2][0] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
        
        
elif player1 == 7 or player1 == 8 or player1 == 9:
    board[2][player1-7] = '0'
    print(board)
    
      #checking 3 zeros matching or not
    if board[0][0] == '0' and board[0][1] == '0' and board[0][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[1][0] == '0' and board[1][1] == '0' and board[1][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[2][0] == '0' and board[2][1] == '0' and board[2][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][0] == '0' and board[1][0] == '0' and board[2][0] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][1] == '0' and board[1][1] == '0' and board[2][1] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][2] == '0' and board[1][2] == '0' and board[2][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][0] == '0' and board[1][1] == '0' and board[2][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][2] == '0' and board[1][1] == '0' and board[2][0] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    
else:
    print("Wrong Choice !!")

    
    
    
    
#player 2 Turn to play
player2 = int(input("Player2 Turn :"))

if player2 == 1 or player2 == 2 or player2 == 3:
    board[0][player2-1] = "x"
    print(board)
    
     #checking 3 cross matching or not
    if board[0][0] == 'x' and board[0][1] == 'x' and board[0][2] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[1][0] and board[1][1] and board[1][2] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[2][0] and board[2][1] and board[2][2] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[0][0] and board[1][0] and board[2][0] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[0][1] and board[1][1] and board[2][1] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[0][2] and board[1][2] and board[2][2] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[0][0] and board[1][1] and board[2][2] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[0][2] and board[1][1] and board[2][0] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    
elif player2 == 4 or player2 == 5 or player2 == 6:
    board[1][player2-4] = "x"
    print(board)
    
    
      #checking 3 cross matching or not
    if board[0][0] and board[0][1] and board[0][2] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[1][0] and board[1][1] and board[1][2] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[2][0] and board[2][1] and board[2][2] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[0][0] and board[1][0] and board[2][0] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[0][1] and board[1][1] and board[2][1] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[0][2] and board[1][2] and board[2][2] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[0][0] and board[1][1] and board[2][2] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[0][2] and board[1][1] and board[2][0] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
        
        
elif player2 == 7 or player2 == 8 or player2 == 9:
    board[2][player2-7] = "x"
    print(board)
    
    
      #checking 3 cross matching or not
    if board[0][0] and board[0][1] and board[0][2] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[1][0] and board[1][1] and board[1][2] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[2][0] and board[2][1] and board[2][2] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[0][0] and board[1][0] and board[2][0] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[0][1] and board[1][1] and board[2][1] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[0][2] and board[1][2] and board[2][2] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[0][0] and board[1][1] and board[2][2] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[0][2] and board[1][1] and board[2][0] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
else:
    print("Wrong Choice !!")

 




    
#player 1 Turn to play
player1 = int(input("Player1 Turn :"))

if player1 == 1 or player1 == 2 or player1 == 3:
    board[0][player1-1] = '0'
    print(board)
    
      #checking 3 zeros matching or not
    if board[0][0] and board[0][1] and board[0][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[1][0] and board[1][1] and board[1][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[2][0] and board[2][1] and board[2][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][0] and board[1][0] and board[2][0] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][1] and board[1][1] and board[2][1] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][2] and board[1][2] and board[2][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][0] and board[1][1] and board[2][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][2] and board[1][1] and board[2][0] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
        
        
elif player1 == 4 or player1 == 5 or player1 == 6:
    board[1][player1-4] = '0'
    print(board)
    
      #checking 3 zeros matching or not
    if board[0][0] and board[0][1] and board[0][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[1][0] and board[1][1] and board[1][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[2][0] and board[2][1] and board[2][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][0] and board[1][0] and board[2][0] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][1] and board[1][1] and board[2][1] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][2] and board[1][2] and board[2][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][0] and board[1][1] and board[2][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][2] and board[1][1] and board[2][0] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
        
elif player1 == 7 or player1 == 8 or player1 == 9:
    board[2][player1-7] = '0'
    print(board)
    
      #checking 3 zeros matching or not
    if board[0][0] and board[0][1] and board[0][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[1][0] and board[1][1] and board[1][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[2][0] and board[2][1] and board[2][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][0] and board[1][0] and board[2][0] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][1] and board[1][1] and board[2][1] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][2] and board[1][2] and board[2][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][0] and board[1][1] and board[2][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][2] and board[1][1] and board[2][0] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    
else:
    print("Wrong Choice !!")

    
    

    
#player 2 Turn to play
player2 = int(input("Player2 Turn :"))

if player2 == 1 or player2 == 2 or player2 == 3:
    board[0][player2-1] = "x"
    print(board)
    
     #checking 3 zeros matching or not
    if board[0][0] and board[0][1] and board[0][2] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[1][0] and board[1][1] and board[1][2] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[2][0] and board[2][1] and board[2][2] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[0][0] and board[1][0] and board[2][0] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[0][1] and board[1][1] and board[2][1] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[0][2] and board[1][2] and board[2][2] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[0][0] and board[1][1] and board[2][2] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[0][2] and board[1][1] and board[2][0] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    
elif player2 == 4 or player2 == 5 or player2 == 6:
    board[1][player2-4] = "x"
    print(board)
    
    
      #checking 3 zeros matching or not
    if board[0][0] and board[0][1] and board[0][2] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[1][0] and board[1][1] and board[1][2] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[2][0] and board[2][1] and board[2][2] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[0][0] and board[1][0] and board[2][0] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[0][1] and board[1][1] and board[2][1] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[0][2] and board[1][2] and board[2][2] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[0][0] and board[1][1] and board[2][2] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[0][2] and board[1][1] and board[2][0] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
        
        
elif player2 == 7 or player2 == 8 or player2 == 9:
    board[2][player2-7] = "x"
    print(board)
    
    
      #checking 3 zeros matching or not
    if board[0][0] and board[0][1] and board[0][2] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[1][0] and board[1][1] and board[1][2] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[2][0] and board[2][1] and board[2][2] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[0][0] and board[1][0] and board[2][0] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[0][1] and board[1][1] and board[2][1] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[0][2] and board[1][2] and board[2][2] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[0][0] and board[1][1] and board[2][2] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
    elif board[0][2] and board[1][1] and board[2][0] == 'x':
        print("Player2 Won")
        print(time.sleep(1000))
else:
    print("Wrong Choice !!")


    
    
#player 1 Turn to play
player1 = int(input("Player1 Turn :"))

if player1 == 1 or player1 == 2 or player1 == 3:
    board[0][player1-1] = '0'
    print(board)
    
      #checking 3 zeros matching or not
    if board[0][0] and board[0][1] and board[0][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[1][0] and board[1][1] and board[1][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[2][0] and board[2][1] and board[2][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][0] and board[1][0] and board[2][0] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][1] and board[1][1] and board[2][1] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][2] and board[1][2] and board[2][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][0] and board[1][1] and board[2][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][2] and board[1][1] and board[2][0] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
elif player1 == 4 or player1 == 5 or player1 == 6:
    board[1][player1-4] = '0'
    print(board)
    
      #checking 3 zeros matching or not
    if board[0][0] and board[0][1] and board[0][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[1][0] and board[1][1] and board[1][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[2][0] and board[2][1] and board[2][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][0] and board[1][0] and board[2][0] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][1] and board[1][1] and board[2][1] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][2] and board[1][2] and board[2][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][0] and board[1][1] and board[2][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][2] and board[1][1] and board[2][0] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
        
elif player1 == 7 or player1 == 8 or player1 == 9:
    board[2][player1-7] = '0'
    print(board)
    
      #checking 3 zeros matching or not
    if board[0][0] and board[0][1] and board[0][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[1][0] and board[1][1] and board[1][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[2][0] and board[2][1] and board[2][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][0] and board[1][0] and board[2][0] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][1] and board[1][1] and board[2][1] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][2] and board[1][2] and board[2][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][0] and board[1][1] and board[2][2] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    elif board[0][2] and board[1][1] and board[2][0] == '0':
        print("Player1 Won")
        print(time.sleep(1000))
    
else:
    print("Wrong Choice !!")

     
