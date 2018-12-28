low=0
high=100
print("Please think of a number between 0 and 100!")
ans= False
while not ans:
    mid=int((low+high)/2)
    print("Is your secret number"+" "+str(mid)+"?")
    userinput=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if userinput =='h':
        high=mid
        mid=int((low+high)/2)
    elif userinput =='l':
        low=mid
        mid=int((low+high)/2)
    elif userinput=='c':
        print("Game over. Your secret number was:"+" "+str(mid))
        ans=True
    else:
        print("Sorry, I did not understand your input.")
