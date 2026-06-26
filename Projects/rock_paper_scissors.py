import random 
choice = ['rock','paper','scissor']
computer_choice = random.choice(choice)
print("Enter your choice= Rock, Paper, Scissor")
user_choice=input("Enter here: ")

print(f"User choice is: {user_choice} , Computer choice is: {computer_choice}")
if(user_choice==computer_choice):
    print("Both chooses same: Match tie")
elif(user_choice=='rock' and computer_choice=='scissor'):
    print("computer won")
elif(user_choice=='rock' and computer_choice=='paper'):
    print('computer won')
elif(user_choice=='paper' and computer_choice=='scissor'):
    print('computer won')
elif(user_choice=='paper' and computer_choice=='rock'):
    print('user won')
elif(user_choice=='scissor' and computer_choice=='paper'):
    print('user won')
elif(user_choice=='scissor' and computer_choice=='rock'):
    print('user won')


