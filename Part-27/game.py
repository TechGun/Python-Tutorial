print("To quit game enter 0")

num = 50
guess = 0
attempt = 0

while True:
    guess = int(input("Guess a number: "))

    if guess == 0:
        print("You loose!")
        break

    attempt += 1

    if guess == num:
        print(f"You guessed it right! in {attempt} attempts")
        break
