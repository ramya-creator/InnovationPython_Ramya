#10_question

counter = 1

while counter <= 5:
    i = int(input("Enter your guess: "))
    if i == 8:
        print("Good guess!")
    else:
        print("Try again")
    counter += 1

print("Game over!")