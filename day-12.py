import random
print("welcome to the number guessing game")
print("I'M thinking of number between 1 to 100:")
difficulty_level=input("choose difficulty level .type hard or easy ")
print(difficulty_level)
random_choice=random.randint(1,100)
# print(random_choice)
if difficulty_level=='hard':
    attempts=6
    for i in range(0,attempts):
        attempts=attempts-1
        print(f"you have left with your {attempts} attempts")
        if i==5:
            print("ooops you are going out of chances")
            break
        guess_number=int(input("guess the number"))
        if guess_number==random_choice:
            print("you guessed it correctly")
            break
        elif guess_number>random_choice:
            print("guessed number is too high")
        elif guess_number<random_choice:
            print("guessed number is too low")
        else:
            print("guess the number again")
if difficulty_level=='easy':
        attempts = 11
        for i in range(0, attempts):
            attempts=attempts-1
            print(f"you have left with your {attempts} attempts")
            if i == 10:
                print("ooops you are going out of chances")
                break
            guess_number = int(input("guess the number"))
            if guess_number == random_choice:
                print("you guessed it correctly")
                break
            elif guess_number > random_choice:
                print("guessed number is too high")
            elif guess_number < random_choice:
                print("guessed number is too low")
            else:
                print("guess the number again")

