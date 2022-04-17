import random

line1 = """
  |   |  
"""
line2 = """
  |   |  
"""
line3 = """
  |   |  
"""
line = "---------"

chessboard = line1 + line + line2 + line + line3

game_continue = True
user_already_choose = []
computer_already_choose = []

def put_chess_in(chess_number, user_or_computer):
    global line1, line2, line3, chessboard, user_already_choose, computer_already_choose
    if user_or_computer == "user":
        chess_symbol = "O"
        user_already_choose.append(chess_number)
    else:
        chess_symbol = "X"
        computer_already_choose.append(chess_number)
    if chess_number == 1:
        line1 = line1[:1] + chess_symbol + line1[2:]
    elif chess_number == 2:
        line1 = line1[:5] + chess_symbol + line1[6:]
    elif chess_number == 3:
        line1 = line1[:9] + chess_symbol + line1[10:]
    elif chess_number == 4:
        line2 = line2[:1] + chess_symbol + line2[2:]
    elif chess_number == 5:
        line2 = line2[:5] + chess_symbol + line2[6:]
    elif chess_number == 6:
        line2 = line2[:9] + chess_symbol + line2[10:]
    elif chess_number == 7:
        line3 = line3[:1] + chess_symbol + line3[2:]
    elif chess_number == 8:
        line3 = line3[:5] + chess_symbol + line3[6:]
    elif chess_number == 9:
        line3 = line3[:9] + chess_symbol + line3[10:]
        
def check_who_win(chess_already_choose):
    global game_continue
    if 1 in chess_already_choose and 2 in chess_already_choose and 3 in chess_already_choose:
        game_continue = False
        return True
    elif 4 in chess_already_choose and 5 in chess_already_choose and 6 in chess_already_choose:
        game_continue = False
        return True
    elif 7 in chess_already_choose and 8 in chess_already_choose and 9 in chess_already_choose:
        game_continue = False
        return True
    elif 1 in chess_already_choose and 4 in chess_already_choose and 7 in chess_already_choose:
        game_continue = False
        return True
    elif 2 in chess_already_choose and 5 in chess_already_choose and 8 in chess_already_choose:
        game_continue = False
        return True
    elif 3 in chess_already_choose and 6 in chess_already_choose and 9 in chess_already_choose:
        game_continue = False
        return True
    elif 1 in chess_already_choose and 5 in chess_already_choose and 9 in chess_already_choose:
        game_continue = False
        return True
    elif 3 in chess_already_choose and 5 in chess_already_choose and 7 in chess_already_choose:
        game_continue = False
        return True

while game_continue:
    print(chessboard)
    
    user_choose = int(input("Please choose a position (1-9): "))
    if user_choose in user_already_choose or user_choose in computer_already_choose:
        print("The position is already selected, please choose another one.")
        continue
    else:
        put_chess_in(user_choose, "user")
        
        
    computer_choose = random.randint(1,9)
    if len(user_already_choose) + len(computer_already_choose) < 9:
        while computer_choose in user_already_choose or computer_choose in computer_already_choose:
            computer_choose = random.randint(1,9)
        put_chess_in(computer_choose, "computer")
        
    chessboard = line1 + line + line2 + line + line3
    
    if check_who_win(user_already_choose):
            print(chessboard)
            print("You win!")
            break
    if check_who_win(computer_already_choose):
            print(chessboard)
            print("Computer win!")
            break
    
    if len(user_already_choose) + len(computer_already_choose) == 9: 
        print("Draw!")
        user_already_choose = []
        computer_already_choose = []
        line1 = """
        |   |  
        """
        line2 = """
        |   |  
        """
        line3 = """
        |   |  
        """
        line = "---------"
        
    
    
    
    
    
    
    
    

