from random import randint

secret = randint(1, 100)
guess = 0

print("Welcome!")

while guess != secret:
    g = input("Guess a number: ")
    guess = int(g)

    if guess == secret:
        print("Good job, you win!")
    else:
        if guess > secret:
            print("Your guess is too much!")
        else:
            print("Your guess is too little!")
print("Game over man!")
