print("welcome to the game")
print("winning rules of the game:")
print("Rock Vs Paper -> paper wins\n"+"Rock Vs Scissor -> rock wins\n"+"Paper Vs Scissor -> scissor wins\n")
print("Enter your choice :\n 1.Rock \n 2.Paper \n 3.Scissor\n")
choice=int(input("user1 turn:"))
if choice==1:
    choice_name='rock'
elif choice==2:
    choice_name='paper'
elif choice==3:
    choice_name="scissor"
else :
    choice_name=="invalid"
    print("enter valid input")
print("user1 choice is :"+choice_name)
print("now it's user2 turn.....")
uchoice=int(input("user2 turn:"))
if uchoice==1:
    uchoice_name='rock'
elif uchoice==2:
    uchoice_name='paper'
elif uchoice==3:
    uchoice_name="scissor"
else :
    uchoice_name=="invalid"
    print("enter valid input")
print("user2 choice is :"+uchoice_name)
print(choice_name+"vs"+uchoice_name)
if ((choice==1 and uchoice==2)or(choice==2 and uchoice==1)):
    res="paper"
elif  ((choice==1 and uchoice==3)or(choice==3 and uchoice==1)):
    res="rock"
else:
    res="scissor"
if res==choice_name:
    print("****USER1 WINS****")
else:
    print("****USER2 WINS****")
    
            
