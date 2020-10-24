import random # We use this ro pick the item

items = [] # We make a empty list

print("Say \"pick\" if you want to pick\n") # We tell the user that they can say pick to pick

while True: # So the user can add as many items as they want
    item = input("What do you want to add:\n") # We ask what the user wants to add
    if item.lower() == "pick": # If the user says to pick
        picked_item = random.choice(items) # We pick the item
        print("The item I picked is: " + picked_item) # We tell the picked item
        break # we end the loop and thus break the program
    else: # If the user didn't say to pick
        items.append(item) # Add the item to the list
