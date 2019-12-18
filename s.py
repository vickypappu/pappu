print("welcome to the game")
print("winning rules of the game:")
print("Rock Vs Paper -> paper wins\n"+"Rock Vs Scissor -> rock wins\n"+"Paper Vs Scissor -> scissor wins\n")
while true:
    print("Enter your choice :\n 1.Rock \n 2.Paper \n 3.Scissor\n")
    choice=int(input("user turn:"))
    while choice>3 or choice<1 :
        print("enter valid input")
        if choice==1:
            choice_name='rock'
        elif choice==2:
            choice_name='paper'
        else:
            choice_name="scissor"
            print("user choice is :"+choice_name)
            print("now it's computer turn.....")
