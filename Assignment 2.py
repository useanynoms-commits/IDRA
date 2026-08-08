import random

num = random.randint(1, 100)
print("Guess a number between 1-100. You have 5 tries!")

for attempt in range(1, 6):
    guess = int(input(f"Attempt {attempt}: "))
    
    if guess == num:
        print(f"🎉 Winner! It took you {attempt} tries!")
        break
    print("Too high!" if guess > num else "Too low!")
    print(f"{5 - attempt} tries left\n")
else:
    print(f"\n💔 Game over! The number was {num}")