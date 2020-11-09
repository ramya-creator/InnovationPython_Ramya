#9_a_guess_lucky_number
number = int(input("Guess the lucky number "))
while True:
    if number ==7:
        print("That is the lucky number")
        break
    else:
        print("That is not the lucky number")
        answer=input("Do you want to continue Yes or No:").lower()
        if answer == "no":
            break
        else:
            number = int(input("Guess the lucky number "))
            continue
