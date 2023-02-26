# import random to create a random number between 1-2 with randint
import random

# import only system from os
from os import system, name
 
# define our clear function
def clear():
     # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
 

def display_board(my_board):
    
    print("")
    print("{:^5} | {:^5} | {:^5}".format(my_board[1],my_board[2],my_board[3]))
    print("_"*19)
    print("")
    print("{:^5} | {:^5} | {:^5}".format(my_board[4],my_board[5],my_board[6]))
    print("_"*19)
    print("")
    print("{:^5} | {:^5} | {:^5}".format(my_board[7],my_board[8],my_board[9]))
    print("")


def player_input():
    
    choice1 = 'wrong'

    while choice1 not in ['X','O']:
        
        choice1 = input("Oyuncu 1, 'X' mi olmak istersin yoksa 'O' mu? ('X' ya da 'O'): ")
        
        if choice1 not in ['X','O']:

            clear()
            
            print("Üzgünüm, sadece 'X' ya da 'O' seçmelisiniz!")

    if choice1 == "X":
        choice2 = "O"
    else:
        choice2 = "X"

    return (choice1,choice2)


def place_marker(board, marker, position):
    
    board[position]=marker
    
    return board

def win_check(my_board, marker):
    
        if ((my_board[1] == my_board[2] == my_board[3] == marker) or 
        (my_board[4] == my_board[5] == my_board[6] == marker) or
        (my_board[7] == my_board[8] == my_board[9] == marker) or
        (my_board[1] == my_board[4] == my_board[7] == marker) or
        (my_board[2] == my_board[5] == my_board[8] == marker) or
        (my_board[3] == my_board[6] == my_board[9] == marker) or
        (my_board[1] == my_board[5] == my_board[9] == marker) or
        (my_board[3] == my_board[5] == my_board[7] == marker) ):
            return True
        else:
            return False


def choose_first():
    choose_first_number=random.randint(1,2)
    print("Oyuncu {} ile oyuna başlayacağız!".format(choose_first_number))
    return choose_first_number

def space_check(board, position):
    
    if board[position] not in ["X","O"]:
        return True
    else:
        return False
    

def full_board_check(board):
    count=0
    for item in board:
        if item in ["X","O"]:
            count+=1
        else:
            pass
    if count == 9:
        return True
    else:
        return False
    
def player_choice(board):
        
    checking_space = False
    
    while not checking_space:
        
        choice = 'wrong'
        while choice not in ['1','2','3','4','5','6','7','8','9']:

            choice = input("Hangi kutucuğu seçmek istiyorsunuz? (1-9): ")

            if choice not in ['1','2','3','4','5','6','7','8','9']:
                
                print("Üzgünüm, sadece boşta olan (1-9) rakamlarından birini seçmelisiniz.")
   
        checking_space = space_check(board,int(choice))
    
    clear()
    
    return int(choice)


def replay():
    
    choice = 'wrong'

    while choice not in ['E','H']:
        
        choice = input("Oyuna devam etmek istiyor musunuz? Evet ya da Hayır için => E ya da H ")
        
        if choice not in ['E','H']:
                        
            print("Üzgünüm, anlayamadım. Lütfen Evet ya da Hayır için => E ya da H seçtiğinizden emin olun. ")
                
    if choice == "E":
        return True
    else:
        return False
    
print("Can Birlik'in Muhteşem Tic Tac Toe Oyununa Hoşgeldiniz!")

while True:
    # Set the game up here
 
    my_board = ["#","1","2","3","4","5","6","7","8","9"]
    display_board(my_board)
    game_on = True
    
    (marker_1,marker_2) = player_input()
            
    clear()
    
    turn=choose_first()
    
    while game_on:
        
        display_board(my_board)
        # Player 1 Turn
        if turn == 1:
                print("")
                print("Oyuncu 1'in sırası ve simgesi {} !".format(marker_1))
                position = player_choice(my_board)
                my_board = place_marker(my_board, marker_1, position)

                if win_check(my_board, marker_1):
                    game_on = False
                    print("Oyuncu 1 Kazandı, Tebrikler!")
                    display_board(my_board)
                    break
                else:
                    pass

                if full_board_check(my_board):
                    game_on = False
                    print("Oyun Berabere!")
                    display_board(my_board)
                    break
                else:
                    pass

                turn = 2

            # Player2's turn.
        elif turn == 2:    
                print("")
                print("Oyuncu 2'nin sırası ve simgesi {} !".format(marker_2))
                position = player_choice(my_board)
                my_board = place_marker(my_board, marker_2, position)

                if win_check(my_board, marker_2):
                    game_on = False
                    print("Oyuncu 2 Kazandı!")
                    display_board(my_board)
                    break
                else:
                    pass

                if full_board_check(my_board):
                    game_on = False
                    print("Berabere!")
                    display_board(my_board)
                    break
                else:
                    pass

                turn = 1
        
            
                
    if not replay():
        break
    else:
        clear() 
        print("Can Birlik'in Muhteşem Tic Tac Toe Oyununa Yeniden Hoşgeldiniz!")