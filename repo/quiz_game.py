print("Welcome to my computer quiz!")

playing = input("do you want to play? ")

if playing != "yes":
    quit()
    
print ("okay! let's play :)")
score = 0
answer = input("what does cpu stand for? ")
if answer . lower() == "central processing unit":
    print('correct!')
    score += 1
else:
    print('false')
answer = input("what does ML stand for? ")
if answer  . lower() == "machine learning":
    print('correct!')
    score += 1
else:
    print('false')
answer  = input("what does AI stand for? ")
if answer . lower()== "artificial intelliegence":
    print('correct!')
    score += 1
else:
    print('false')
    print("you got " + str(score) + "questions correct!")
    print("you got " + str(score / 3))



