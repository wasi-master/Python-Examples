import random  We use the random module to generate random numbers

min_num = int(input("Minimum Number: ")) # We get the minimum number the user wants
max_num = int(input("Maximum Number: ")) # We get the maximum number the user wants

picked_num = random.randint(min_num, max_num) # We pick the number

while True: # We use a while loop so the user can do it again if they fail
    answer = int(input("Guess the number: "))
    if answer != picked_num: # If they don't reply with the correct number
        print("Wrong, try again") # We tell the user that they are wrong
    else:  # If they do reply with the correct number
        print(f"Yay you won, the number was {picked_num}") # We tell the user that he won
        break # we end the loop and thus break the program
