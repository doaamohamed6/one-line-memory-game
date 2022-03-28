from random import shuffle
list1 = ["P","R","O","G","y","Z","A","M","I","N"]*2
list2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

player1_score = 0
player2_score = 0

list.shuffle()
def choose_player1():
    global player1_score
    while True:
        print(list2)
        first_num = int(input("P1 please enter first num from 0 to 19"))
        second_num = int(input("P1 please enter second num from 0 to 19 "))
        if first_num ==second_num:
            print("this number is not valid")
            continue
        elif first_num not in range(0,20) or second_num not in range(0,20):
            print("this number is not valid")
            continue
        elif list1[first_num] == "*" or list1[second_num] == "*":
            print("this number is not valid")
            continue
        for i in range (0,20):
             if first_num != i  and second_num != i:
                 print(list2[i] , end=" ")
             elif first_num == i or second_num == i :
                print(list1[i] ,end=" ")
        print("\n")
        if list1[first_num] == list1[second_num]:
            player1_score +=1
            list1.remove(list1[first_num])
            list1.insert(first_num,"*")
            list2.remove(list2[first_num])
            list2.insert(first_num,"*")
            list1.remove(list1[second_num])
            list1.insert(second_num, "*")
            list2.remove(list2[second_num])
            list2.insert(second_num, "*")
        break



def choose_player2 ():
    global player2_score
    while True:
        print(list2)
        first_num = int(input("p2 please enter first num from 0 to 19"))
        second_num = int(input("p2 please enter second num from 0 to 19 "))
        if first_num == second_num:
            print("this number is not valid")
            continue
        elif first_num not in range(0, 20) or second_num not in range(0, 20):
            print("this number is not valid")
            continue
        elif list1[first_num] == "*" or list1[second_num] == "*":
            print("this number is not valid")
            continue
        for i in range(0, 20):
            if first_num != i and second_num != i:
                print(list2[i], end=" ")
            elif first_num == i or second_num == i:
                print(list1[i], end=" ")
        if list1[first_num] == list1[second_num]:
            player2_score += 1
            list1.remove(list1[first_num])
            list1.insert(first_num, "*")
            list2.remove(list2[first_num])
            list2.insert(first_num, "*")
            list1.remove(list1[second_num])
            list1.insert(second_num, "*")
            list2.remove(list2[second_num])
            list2.insert(second_num, "*")

        break



while True:
    choose_player1()
    print("player 1 score =", player1_score,"\n")
    print("player 2 score =", player2_score)
    if player1_score == 6 :
        print("player 1 wins")
        break
    elif player1_score == 5 and player2_score == 5:
        print("draw")
        break

    choose_player2()
    print("player 1 score =", player1_score, "\n")
    print("player 2 score =", player2_score)
    if player2_score == 6:
        print("player 2 wins")
        break
    elif player2_score == 5 and player2_score == 5:
        print("draw")
        break
