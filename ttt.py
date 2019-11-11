# This is a tic tac toe game

# Importz subprocesses to clear the command window between turns
# keeps things looking tidy :)
import subprocess as sp
def clearterminal():
    clearterminal = sp.call('clear',shell=True)


# This is where the magic happens
def play():
    global turns
    global brd
    clearterminal()
    print(msging('msg1'))
    exm_board()
    print(msging('msg2'))
    input('Press enter to continue')
    printboard(brd)

    while not winlogic() and turns < 9:
        placingcounter()

    if turns > 8 and not winlogic():
        print("It's a draw..")
    # pagain = input("Would you like to play again y/n?")
    pagain = func_input("Would you like to play again?",['y','n'],'text')
    if pagain  == 'n':
        clearterminal()
        print("\n\nOk, have a nice day now!\n")
    else:
        clearterminal()
        brd = resetboard()
        turns = 0
        play()

# resets the board for a fresh game
def resetboard():

    brd = []
    for i in range(0,9,1):
        brd.append(0)

    return brd

# prints an example board showing where you will place your counters
def exm_board():
    # prints example board
    brd = [[7,8,9],[4,5,6],[1,2,3]]
    for i in range(0,3,1):
        print(brd[i])

# checks that what people are entering is what the program expects
def func_input(msg,options,in_type):
    choice_made = False
    while choice_made == False:
        print(msg)
        # choice_input = input("Your choice >")
        choice_input = input("Your choice >")
        if in_type == 'num':
            while True:
                 try:
                     choice_input = int(choice_input)
                     break
                 except ValueError:
                     print("Oops!  That was no valid number.  Try again...")
                     break
        elif choice_input in options:
                return choice_input
                choice_made = True
        else:
                print(f"Please only enter {options} without [] or ''.")

# Takes the dict and prints the board out tic tac toe style
def printboard(brd):
    n=0
    start = 6
    end = 9
    print('')
    for n in range(0,3,1):
        for i in range(start,end,1):

            if brd[i] == 0:
                print('-',' ', end = '')
            elif brd[i] == -1:
                print('O',' ', end = '')
            elif brd[i] == 1:
                print('X',' ', end = '')
            else:
                print('printboard error')
                pass

        print('\n')
        start -= 3
        end -= 3
        n+=1


# Decides whose go it is
def whosego():
    global turns
    if (turns % 2) == 0:
        pturn = 1
    else:
        pturn = 2
    return pturn

# The logic to place counters
def placingcounter():
    global brd
    global turns
    pscore = {1 : 1, 2 : -1}

    print(f"Player {whosego()}, it's your go...")
    clearterminal
    goodplay = False
    while goodplay == False :

        choice = int(func_input("Where would you like to place your counter?",range(0,10,1),'num')) - 1
        if brd[choice] == 0:
            brd[choice] = pscore[whosego()]
            clearterminal()
            printboard(brd)
            turns += 1
            goodplay = True
        else:
            print("That's taken! Choose an empty space.")

# Defines the logic of how to win!
# Player 1 places 1s and player 2 places -1s
# If a row, column or diagonal equals 3, player 1 wins
# If a row , column or diagonal equals -3, player 2 wins
def winlogic():
    global brd
    winner = False
    win = {
    1 : brd[0] + brd[1] + brd[2],
    2 : brd[3] + brd[4] + brd[5],
    3 : brd[6] + brd[7] + brd[8],

    4 : brd[0] + brd[3] + brd[8],
    5 : brd[1] + brd[4] + brd[7],
    6 : brd[2] + brd[6] + brd[8],

    7 : brd[0] + brd[4] + brd[8],
    8 : brd[6] + brd[4] + brd[2]
    }

    for i in range(1,9,1):
        if win[i] > 2:
            print('Player 1 wins!')
            winner = True
        elif win[i] < -2:
            print('Player 2 wins!')
            winner = True
        else:
            pass
    return winner

# A handy place to store longer messages
def msging(i):
    messages = {
    'msg1' :
    """Welcome to Tic Tac Toe! Player 1 goes first...
    The first thing you need to know is where to place your counters.
        See an example board below:""",

    'msg2' :
    "You will need to remember these numbers to tell the computer where to place your counters"
    }

    return(messages[i])

brd = resetboard()
turns = 0
play()
