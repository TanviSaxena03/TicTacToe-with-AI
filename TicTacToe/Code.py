def constb(board):
    print("Current state: \n\n")
    for i in range(0,9):
        if ((i>0) and (i%3==0)):
            print("\n")
        if (board[i]==0):
            print("_ ", end=" ")
        if (board[i]==-1):
            print("X ", end=" ")
        if (board[i]==1):
            print("O ", end=" ")
    print(" \n")


def userA(board):
    p=input("Enter position of X from 1 to 9: ")
    p=int(p)
    if (board[p-1]!=0):
        print("Wrong move \n")
        exit(0)
    board[p-1]=-1


def userB(board):
    p=input("Enter position of O from 1 to 9: ")
    p=int(p)
    if (board[p-1]!=0):
        print("Wrong move")
        exit(0)
    board[p-1]=1


def minmax(board,pl):
    x=analyzeb(board)
    if (x!=0):
        return x*pl
    p=-1
    val=-2
    for i in range(0,9):
        if (board[i]==0):
            board[i]=pl
            s=-minmax(board,pl*-1)
            board[i]=0
            if (s>val):
                val=s
                p=i
    if p==-1:
        return 0
    return val


def ai(board):
    p=-1
    val=-2
    for i in range(0,9):
        if (board[i]==0):
            board[i]=1
            s=-minmax(board,-1)
            board[i]=0
            if (s>val):
                val=s
                p=i
    board[p]=1


def analyzeb(board):
    cb=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in range(0,8):
        if(board[cb[i][0]]!=0 and board[cb[i][0]]==board[cb[i][1]] and board[cb[i][0]]==board[cb[i][2]]):
            return board[cb[i][0]]
    return 0


def main():
    ch=input("Enter 1 for single player and 2 for multiplayer: ")
    ch=int(ch)
    board=[0,0,0,0,0,0,0,0,0]
    if (ch==1):
        print("Computer: O vs. You: X")
        pl=input("Enter 1 to play 1st and 2 to play 2nd: " )
        pl=int(pl)
        for i in range(0,9):
            if (analyzeb(board)!=0):
                break
            if ((i+pl)%2==0):
                ai(board)
            else:
                constb(board)
                userA(board)
    else:
        for i in range (0,9):
            if (analyzeb(board)!=0):
                break
            if (i%2==0):
                constb(board)
                userA(board)
            else:
                constb(board)
                userB(board)
    x=analyzeb(board)
    if (x==0):
        constb(board)
        print("Draw!!")
    if (x==-1):
        constb(board)
        print("X wins!!")
    if (x==1):
        constb(board)
        print("O wins!!")
    
main()
