import random
def Sample1():
    counter_win1=0
    counter_win2=0
    counter_tie=0
    xartia = []
    figures = ["J", "Q", "K"]
    xarti = [i for i in range(1, 11)] + figures
    color = ["H", "S", "C", "D"]
    for k in range(0,100):
        for i in xarti:
            for j in color:
                xartia.append([i,j])
        random.shuffle(xartia)
        player1=[]
        sum1=0
        while sum1<16:
            sum1=0
            player1.append(xartia.pop())
            print ("cards of player1:",player1)
            for card in player1:
                if card[0] in figures:
                    sum1=sum1+10
                else:
                    sum1=sum1+card[0]
            print("sum of player1:",sum1)
        if sum1>21:
            print("P2 wins!")
            counter_win2+=1
        else:
            print("P2 joins the game") #let me add one more player
            player2=[]
            sum2=0
            while sum2<16:
                sum2=0
                player2.append(xartia.pop())
                print ("cards of palyer2:",player2)
                for card in player2:
                    if card[0] in figures:
                        sum2=sum2+10
                    else:
                        sum2=sum2+card[0]
                print("sum of player2:",sum2)
            if sum2>21:
                sum2=0
            if sum1>sum2:
                print("P1 wins!")
                counter_win1+=1
            elif sum2>sum1:
                print("P2 wins!")
                counter_win2+=1
            else:
                print("draw!")
                counter_tie+=1
    print("player1 won",counter_win1,"times")
    print("player2 won",counter_win2,"times")
    print("Both players Tied",counter_tie,"times")

def Sample2():
    counter_win1=0
    counter_win2=0
    counter_tie=0
    xartia = []
    figures = ["J", "Q", "K"]
    xarti = [i for i in range(1, 11)] + figures
    color = ["H", "S", "C", "D"]
    for k in range(0,100):
        for i in xarti:
            for j in color:
                xartia.append([i,j])
        random.shuffle(xartia)
        player1=[]
        sum1=0
        first_turn=0
        while sum1<16:
            sum1=0
            hand=xartia.pop()
            print("player1",hand)
            while (first_turn==0):
                while ((((hand[0] in figures) or hand[0]==10))and(first_turn==0)):
                    first_turn+=1
                    player1.append(hand)
                else:
                    hand=xartia.pop()
                    print("player1",hand)

            if first_turn==1:
                player1.append(hand)
                for card in player1:
                    if card[0] in figures:
                        sum1=sum1+10
                    else:
                        sum1=sum1+card[0]

                print("cards of player1:",player1)
                print("sum of player1:",sum1)
        if sum1>21:
            print("P2 wins!")
            counter_win2+=1
        else:
            print("P2 joins the game") #let me add one more player
            player2=[]
            sum2=0
            first_turn=0
            while sum2<16:
                sum2=0
                hand=xartia.pop()
                print("player2",hand)
                if first_turn==0:
                    while (((hand[0] in figures) or hand[0]==10) and (first_turn==0)):
                        hand=xartia.pop()
                        print("player2",hand)
                    else:
                        first_turn+=1

                player2.append(hand)
                for card in player2:
                    if card[0] in figures:
                        sum2=sum2+10
                    else:
                        sum2=sum2+card[0]
                print("cards of player2:",player2)
                print("sum of player2:",sum2)
            if sum2>21:
                sum2=0
            if sum1>sum2:
                print("P1 wins!")
                counter_win1+=1
            elif sum2>sum1:
                print("P2 wins!")
                counter_win2+=1
            else:
                print("draw!")
                counter_tie+=1

    print("player1 won",counter_win1,"times")
    print("player2 won",counter_win2,"times")
    print("Both players Tied",counter_tie,"times")

print("Type 1 for normal sample:")
print("Type 2 for rigged sample:")
if input("either 1 or 2:")=="1":
    Sample1()
else:
    Sample2()
