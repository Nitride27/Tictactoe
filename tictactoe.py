
def board(Xstate,Ostate):
     print(f"| {'X' if Xstate[0]==1 else ('O' if Ostate[0]==1 else '0')} | {'X' if Xstate[1]==1 else ('O' if Ostate[1]==1 else '1')} | {'X' if Xstate[2]==1 else ('O' if Ostate[2]==1 else '2')} |")
     print(f"|---|---|---|")
     print(f"| {'X' if Xstate[3]==1 else ('O' if Ostate[3]==1 else '3')} | {'X' if Xstate[4]==1 else ('O' if Ostate[4]==1 else '4')} | {'X' if Xstate[5]==1 else ('O' if Ostate[5]==1 else '5')} |")
     print(f"|---|---|---|")
     print(f"| {'X' if Xstate[6]==1 else ('O' if Ostate[6]==1 else '6')} | {'X' if Xstate[7]==1 else ('O' if Ostate[7]==1 else '7')} | {'X' if Xstate[8]==1 else ('O' if Ostate[8]==1 else '8')} |")


def sum(a,b,c):
    return a+b+c

def checkwin(Xstate,Ostate):
    win=[[0,1,2],[0,3,6],[0,4,8],[6,7,8],[2,5,8],[2,4,6],[3,4,5],[1,4,7]]
    for i in win:
        if (sum(Xstate[i[0]],Xstate[i[1]],Xstate[i[2]])==3):
            return 1
            
        elif (sum(Ostate[i[0]],Ostate[i[1]],Ostate[i[2]])==3):
            return 0         
    return 2
        
    
def main():
    Xstate=[0,0,0,0,0,0,0,0,0]
    Ostate=[0,0,0,0,0,0,0,0,0]
    turn=1
    print("Welcome to tictactoe")
    print("--------------------")
    board(Xstate,Ostate)
    while (True):
       if(turn==1):
           print("\n")
           print("Player 1 turn:")
          
           x=int(input("Enter number of the position:"))
           if(x<0 or x>8):
               print('Invalid position , try again!')
            
           
           Xstate[x]=1
           turn=0
           board(Xstate,Ostate)
           c=checkwin(Xstate,Ostate)
           if (c==1):
               print("Player 1 wins!!!!!!!!!!!!!")
               break
           elif c==2 and all(Xstate[i] or Ostate[i] for i in range(9)):
               print("\nDraw!!!!!!!!!!")
               break
           print("\n")
       else:
           print("\n")
           print("Player 2 turn") 
           O=int(input("Enter number of the position:"))
           if(x<0 or x>8):
               print('Invalid position , try again!')
           Ostate[O]=1
           turn=1
           board(Xstate,Ostate)
           c=checkwin(Xstate,Ostate)
           if(c==0):
               print("\nPlayer 2 wins!!!!!!!!!!!!!!")
               break
           elif c==2 and all(Xstate[i] or Ostate[i] for i in range(9)):
               print("\nDraw!!!!!!!!!!")
               break
           print("\n")  
       

if __name__=="__main__":
    main()

    