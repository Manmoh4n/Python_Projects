print("hello welcome in my game")

playing = input("you want to play this game")

if playing.lower() != "yes":
    quit()
    
print("ok lets play")
score = 0

answer = input("what is full form of cpu")
if answer.lower() == "central processing unit ":
    print("correct")
    score+=1
else:
    print("Incorrect")
answer = input("what is the capital of Bihar")
if answer.lower() == "patna":
    print("correct")
    score += 1
else:
    print("Incorrect")

answer = input("what is the capital of  Delhi")
if answer.lower() == "new delhi":
    print("correct")
    score +=1
else:
    print("Incorrect")

print("you got " + str(score) + "question correct!")
print("you got "+ str(score/3)*100+ "percent")