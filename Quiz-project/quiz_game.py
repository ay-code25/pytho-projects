print("Welcome to my first quize_game")

playing = input("Do you want to play?  ")

if playing.lower() != "yes":
    quit()

print("Okay! Lets play :")
answer = input("What does HTML stands for?  ")
if answer.lower() == "Hypertext markup Language":
    print('Correct!')
else:
    print('Inorrect!')

answer = input("What is the atribiot for image in HTML?  ")
if answer.lower() == "src":
    print('Correct!')
else:
    print('Inorrect!')
    
answer = input("How to create form in HTML?  ")
if answer.lower() == "with form tag":
    print('Correct!')
else:
    print('Inorrect!')
    
    