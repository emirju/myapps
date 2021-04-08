
### Guessing Game

secret_number = 9
guess_start = 0
guess_limit = 3

while guess_start < guess_limit:
    type_number = int(input("Guess the number : "))
    guess_start += 1
    if type_number == secret_number:
        print("!!!  YOU WON THE GAME  !!! ")
        break
else:
    print("Sorry, you have failed ")