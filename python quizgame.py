print("Hello Everyone")
print("Welcome to my quiz game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! let's play :)")
score = 0
answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print('correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GUI stands for? ")
if answer.lower() == "graphical user interface":
    print('correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print('correct!')
    score +=1
else:
    print("Incorrect!")

answer = input("What does SSD stands for? ")
if answer.lower() == "solid state drive":
    print('correct!')
    score +=1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
    
