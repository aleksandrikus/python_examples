secret = 42

while True:
    guess = int(input("Enter your guess number: "))
    if guess == secret:
        print("You lucky bastard! :)")
        break
    else:
        print("Suckeeeer!")