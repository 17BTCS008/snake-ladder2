import random
c=0
while(c<100):
    a=input("enter 'r' to roll the dice: ")
    if (a=='r'):
        r=random.randint(1,6)
        c=c+r
        print('Dice value=',r)
        print('count value=',c)

        if(c==8):
            c=37

            print('you have climbed the ladder')

        elif(c==13):
            c=34
            print('you have climbed the ladder')

        elif(c==40):
            c=68
            print('you have climbed the ladder')
        

        elif(c==52):
            c=81
            print('you have climbed the ladder')
        
        elif(c==76):
            c=97
            print('you have climbed the ladder')
        
        elif(c==11):
            c=2
            print('you were bitten by the snake')
        
        elif(c==25):
            c=4
            print('you were bitten by the snake')
        
        elif(c==38):
            c=9
            print('you were bitten by the snake')
        
        elif(c==65):
            c=46
            print('you were bitten by the snake')
        
        elif(c==89):
            c=70
            print('you were bitten by the snake')
        
        elif(c==93):
            c=64
            print('you were bitten by the snake')

        elif (c>100):
            c=c-r
        elif (c==100):
            print('you won')
        

        
