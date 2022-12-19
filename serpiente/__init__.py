movements = {"U": [-1,0], "D": [1,0], "R": [0,1], "L": [0,-1]}

def moveSnake(snake,direction):
    head=snake[0]

    snake = [[head[0]+direction[0], head[1]+direction[1]]] + snake[:-1]

    return snake

def calculateNumPaths(board,snake,snakeCopy,nPaths,depth,head):
    for x in movements.values():
            new_position=[head[0]+x[0], head[1]+x[1]]
            if new_position[0]>=0 and new_position[1]>=0:
                if new_position not in snake[:-1] and 0<=new_position[0]<board[0] and 0<=new_position[1]<board[1]:
                    snakeCopy=moveSnake(snake,x)
                    if depth==1:
                        nPaths+=1
                    else:
                        nPaths+=possiblePaths(board,snakeCopy,depth-1)
    return nPaths

def possiblePaths(board,snake,depth):
    snakeCopy=snake
    nPaths=0
    head=snake[0]
    
    if depth==1:
        nPaths = calculateNumPaths(board,snake,snakeCopy,nPaths,depth,head)
        return nPaths
    
    if depth==0:
        return 0

    nPaths = calculateNumPaths(board,snake,snakeCopy,nPaths,depth,head)
    return nPaths

def numberOfAvailableDifferentPaths(board,snakeMain,depth):
    return possiblePaths(board,snakeMain,depth)