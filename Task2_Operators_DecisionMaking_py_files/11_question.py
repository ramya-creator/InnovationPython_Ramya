#11_question

counter = 1

while counter <= 5:
    i = int(input("Enter your guess: "))
    if i == 8:
        print("Good guess!")
        break

    if counter != 5:
        print("Try again")
    else:
        print("Sorry but that was not very successful")

    counter += 1

print("Game over!")