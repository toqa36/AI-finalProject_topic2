import random
import math

#check if move possible or not .
def canUp(Position):
    if Position in [3 ,4 ,5 ,6 ,7 ,8] :
        return True
    return False

def canDown(Position):
    if Position in [0 ,1 ,2 ,3 ,4 ,5] :
        return True
    return False

def canRight(Position):
    if Position in [0 ,1 ,3 ,4 ,6 ,7] :
        return True
    return False

def canLeft(Position):
    if Position in [1 ,2 ,4 ,5 ,7 ,8] :
        return True
    return False

    #all_moves


def direction(before, current):
    if before-current == 3 :
        return "up"
    if before-current == -3 :
        return "down"
    if before-current == -1 :
        return "right"
    if before-current == 1 :
        return "left"
        #possible move of current cell 
# print 
def output(board):
    print(str(board[0]) + " | " + str(board[1]) + " | " + str(board[2]))
    print("_____________")
    print(str(board[3]) + " | " + str(board[4]) + " | " + str(board[5]))
    print("_____________")
    print(str(board[6]) + " | " + str(board[7]) + " | " + str(board[8]))

#up down right left
def getBoardsPossibleMoves(board, Position):        #get MAX childs
    a,b,c,d = list(board),list(board),list(board),list(board)   #copy
    array = []
    if canUp(Position) :
        a[Position-3] = a[Position-3] + a[Position]
        array.append(a)
    if canDown(Position) :
        b[Position+3] = b[Position+3] + b[Position]
        array.append(b)
    if canRight(Position) :
        c[Position+1] = c[Position+1] + c[Position]
        array.append(c)
    if canLeft(Position) : 
        d[Position-1] = d[Position-1] + d[Position]
        array.append(d) 
    return array



def getpositionsPossibleMoves(Position):
    array = []
    if canUp(Position) :
        array.append(Position-3)
    if canDown(Position) :
        array.append(Position+3)
    if canRight(Position) :
        array.append(Position+1)
    if canLeft(Position) :
        array.append(Position-1) 
    return array

def getDirections(Position):
    array = []
    if canUp(Position) :
        array.append('up')
    if canDown(Position) :
        array.append('down')
    if canRight(Position) :
        array.append('right')
    if canLeft(Position) :
        array.append('left')
    return array

#get MIN childs
def getMINPossibleMoves(board, changePosition):        
    a,b,c = list(board),list(board),list(board)   #copy
    array = []
    c[changePosition] = 1
    b[changePosition] = 0
    a[changePosition] =-1
    array.append(a)
    array.append(b)
    array.append(c)
    return array


# alpha beta that choose the best move 
def alphabeta(board, Position, PreviousPosition, level, alpha, beta, maximizingPlayer, goal, moves, directions) :
    best = []
    if  level >= moves :
        #print("Testing")
        #print(directions)
        #print(board[Position])
        best = [str(board[Position]) , directions[0]]
        #print(best)
        return best

    if maximizingPlayer :       #MAX turn
        value = -1*math.inf
        bestMove = " "
        #[ up , down , right , left ]
        boards = list(getBoardsPossibleMoves(board, Position))
        Positions = list(getpositionsPossibleMoves(Position))
        newDirections = list(getDirections(Position))
        for i in range(len(boards)) :
            if level == 0:
                temp = value
                newDirec = list(directions) 
                newDirec.append(newDirections[i])
                returned = list(alphabeta(boards[i], Positions[i], Position, level+1, alpha, beta, False, goal, moves, newDirec))
                value = max(value, int(returned[0]))
                if temp != value :
                    bestMove = direction(Position, Positions[i])
            else:
                newDirec = list(directions) 
                newDirec.append(newDirections[i])
                returned = list(alphabeta(boards[i], Positions[i], Position, level+1, alpha, beta, False, goal, moves, newDirec))
                value = max(value, int(returned[0]))
            alpha = max(alpha, value)
            if alpha >= beta :
                break
        if level == 0 :
            best = [str(value) , bestMove]
        else :
            best = [str(value) , directions[0]]
        return best
        #return value
    else :                       #MIN turn
        value = math.inf
        boards = list(getMINPossibleMoves(board, PreviousPosition))
        for i in range(len(boards)) :
            returned = alphabeta(boards[i], Position, PreviousPosition, level, alpha, beta, True, goal, moves, directions)
            value = min(value, int(returned[0]))
            beta = min(beta, value)
            if alpha >= beta :
                break
        best = [str(value) , directions[0]]
        return best
        #return value

# new bord with new tile
def newBoard(board, Position, move):
    a,b,c,d = list(board),list(board),list(board),list(board)   #copy
    if move == 'up' :
        a[Position-3] = a[Position-3] + a[Position]
        return a
    if move == 'down' :
        b[Position+3] = b[Position+3] + b[Position]
        return b
    if move == 'right' :
        c[Position+1] = c[Position+1] + c[Position]
        return c
    if move == 'left' : 
        d[Position-1] = d[Position-1] + d[Position]
        return d


# the best next new position 
def newPosition( Position, move):
    if move == 'up' :
        return Position-3
    if move == 'down' :
        return Position+3
    if move == 'right' :
        return Position+1
    if move == 'left' : 
        return Position-1

# predicat that take goal and movement  then tell me if win or lose 
def main(board, moves,goal):
    print("\n")
    output(board)
    print("\n")
    Position = 6
    PreviousPosition = -1
    if (board[6] >= goal) :
        print("\nYOU ARE WIN\n")
    for i in range(moves):
        if (board[Position] >= goal):
            print("\nYOU ARE WIN  ")
            break
        arr = list(alphabeta(board, Position, PreviousPosition, 0, -1*math.inf, math.inf, True, goal, moves-i, []))
        new = newBoard(board, Position, arr[1])
        print("\nMove " + str(i+1) +" "+ arr[1] )
        PreviousPosition = Position
        Position = newPosition(Position, arr[1])
        new[PreviousPosition] = random.randrange(-1, 2)
        output(new)
        board = new
        if i == moves-1 and board[Position] >= goal :
            print("\nYOU ARE WIN " )
            break
        elif i == moves-1 :
            print("\nGAME OVER\nYOUR SCORE IS " + str(board[Position]) )
            break

# function that take goal and movement from user
if __name__ == "__main__": 
    G = int(input("\nGoal IS : "))
    M = int(input("Movments IS : "))
    #print(main([1,-1,0,1,0,1,0,1,-1], M, G))
    main([1,-1,0,1,0,1,-1,1,-1], M, G)
   # print("GOAL IS " + str(G))
    #print("MOVES IS " + str(M))
