import random # We use the random module to generate random numbers

while True: # We use a whilebloop so the user can do it again if they want
    min_num = int(input("Minimum Number: ")) # We get the minimum number the user wants
    max_num = int(input("Maximum Number: ")) # We get the maximum number the user wants

    picked_num = random.randint(min_num, max_num) # We pick the number
    print(f"The number I picked is: {picked_num}") # We say the number

    answer = input("Do you wanna play again?\n") # We ask if the user wants to play again
    if answer.lower() == "yes": # If they reply with yes
        continue # we continue
    elif answer.lower() == "no": # If they reply with no
        break # we end the loop and thus break the program
    else: # If they dont say yes or no
        print("Bad Answer")  # we say bad answer and end the program