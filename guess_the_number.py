import random

min_num = int(input("Minimum Number: "))
max_num = int(input("Maximum Number: "))

picked_num = random.randint(min_num, max_num)

while True:
    answer = int(input("Guess the number: "))
    if answer != picked_num:
        print("Wrong, try again")
    else:
        print(f"Yay you won, the number was {picked_num}")
        break
