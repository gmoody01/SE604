

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------ ALAN BURNS - SHOP ------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #


# FUNCTION ------------------------------------------------------------------------------------------------------------#
# Implements a mock trade between a customer and a merchant (ye olden style). Purchasing items results in appending a  #
# text file, much like a growing inventory. Selling items results in appending a different text file (the merchant's)  #
# in a similar way.                                                                                                    #
#                                                                                                                      #
# Implements the random library to determine a random number between 0 and 3. This is to determine a random giveaway   #
# at the merchant's shop, given that the user has a "luck stone" (user answers yes or no).                             #
# ---------------------------------------------------------------------------------------------------------------------#


# IN DEVELOPMENT (Don't delete from list, note progress or say done)
# Removing items from inventories [Near completion]
# Currency system: checking amount, incrementing or decrementing amount [Not started]
# Introducing more compact methods (loops) [Not started]
# Let the user loop back to normal trade after giveaway (code currently exits after giveaway) [Not started]
# Increase random number generator range to cover arbitrary sizes of the merchant's list [Not started]
# Generalizing user responses to account for capitalization and slight misspellings [Not started]
# Output text files to excel formats [Not started]
# Update inventories in real time [Not started]
# Prompt to buy/sell an arbitrary number of times [Not started]
# Quantity of items in inventories [Not started]
# Generate text file to serve as a receipt for the user and merchant [Not started]


# NOTE
# Includes text file "Merchant_Inventory.txt" with four preset items: sword, axe, potion, arrows.
# Includes text file "Personal_Inventory.txt" with two preset items: mace and food.


# -------------------------------------------------------------------------------------------------------------------- #
#                                   OPEN TEXT FILES FOR READING FROM AND WRITING TO                                    #
# -------------------------------------------------------------------------------------------------------------------- #


import random                                           # Imports the random library to generate random integers.

read_his_stuff = open("Merchant_Inventory.txt", "r")    # Allows the merchant's inventory to be read from text file.
add_his_stuff = open("Merchant_Inventory.txt", "a")     # Allows the merchant's inventory to be appended.
read_your_stuff = open("Personal_Inventory.txt", "r")   # Allows the user's inventory to be read from a text file.
add_your_stuff = open("Personal_Inventory.txt", "a")    # Allows the user's inventory to be appended.



# -------------------------------------------------------------------------------------------------------------------- #
#               PURCHASE THE MERCHANT'S ITEMS BY APPENDING CUSTOMER INVENTORY - Personal_Inventory.txt                 #
# -------------------------------------------------------------------------------------------------------------------- #


print("\nWelcome to my shop, weary traveller.\nI have some things you may find helpful.\n")
luck_response = input("Are you carrying a luck stone? \n")


                                        # --- Random Giveaway of Item --- #

if luck_response == "yes":
    print("\nGreat! That means you get a free item from my shop!")
    roll = random.randint(0, 3)  # Generates random integer

    print("Today you get................. a " + read_his_stuff.readlines()[roll]) # Declare item to be given
    #add_your_stuff.write(read_his_stuff.readlines()[3])  # Add item to user inventory (broken)



          # --- Normal Purchasing Mode - Adds item to user inventory, deletes from merchant inventory --- #

else:
    print("Ah, unfortunate. Well, have a look at my wares.\n")

    for items in read_his_stuff.readlines(): # Print out merchant's inventory to the user
        print(items)

    response1 = input("\nChoose what you like: \n")

    # SWORD #
    if response1 == "sword":
        print("Don't poke your eye out.")
        add_your_stuff.write("\nSword") # Add "Sword" to Personal_Inventory.txt
        with open("Merchant_Inventory.txt", "r") as f:
            lines = f.readlines()
        with open("Merchant_Inventory.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != "Sword":
                    f.write(line) # Delete "Sword" from Merchant_Inventory.txt

    # AXE #
    elif response1 == "axe":
        print("That's no hatchet, kid.")
        add_your_stuff.write("\nAxe")
        with open("Merchant_Inventory.txt", "r") as f:
            lines = f.readlines()
        with open("Merchant_Inventory.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != "Axe":
                    f.write(line)

    # POTION #
    elif response1 == "potion":
        print("You look like you need it.")
        add_your_stuff.write("\nPotion")
        with open("Merchant_Inventory.txt", "r") as f:
            lines = f.readlines()
        with open("Merchant_Inventory.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != "Potion":
                    f.write(line)

    # ARROWS #
    elif response1 == "arrows":
        print("It's because it's the cheapest, isn't it?")
        add_your_stuff.write("\nArrows")
        with open("Merchant_Inventory.txt", "r") as f:
            lines = f.readlines()
        with open("Merchant_Inventory.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != "Arrows":
                    f.write(line)

    # MACE #
    elif response1 == "mace":
        print("Spiky!")
        add_your_stuff.write("\nMace")
    with open("Merchant_Inventory.txt", "r") as f:
        lines = f.readlines()
    with open("Merchant_Inventory.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != "Mace":
                f.write(line)

    # FOOD #
#    elif response1 == "food":                                      # Hard to figure out this error...
#        print("Bon appetit!")
#        add_your_stuff.write("\nFood")
#    with open("Merchant_Inventory.txt", "r") as f:
#        lines = f.readlines()
#    with open("Merchant_Inventory.txt", "w") as f:
#        for line in lines:
#            if line.strip("\n") != "Food":
#                f.write(line)

#    else:
#        print("We only speak English here, kid.") # Response to unrecognizable input


# ---------------------------------------------------------------------------------------------------------------------#
#               SELL YOUR ITEMS TO THE MERCHANT BY APPENDING MERCHANT INVENTORY - Merchant_Inventory.txt               #
# ---------------------------------------------------------------------------------------------------------------------#


print("\nHmm... seems like you got some good stuff on you...")

response2 = input("Would you like to sell your items? \n")

if response2 == "yes":
    print("\nThis is your inventory:\n")
    for items in read_your_stuff.readlines(): # Print out user inventory for selection
        print(items)

    response3 = input("\nWhat would you like to sell? \n")

    if response3 == "mace":
        print("I'd love to take that mace off your hands!")
        add_his_stuff.write("\nMace")
        with open("Personal_Inventory.txt", "r") as f:
            lines = f.readlines()
        with open("Personal_Inventory.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != "Mace":
                    f.write(line)

    if response3 == "food":
        print("I haven't eaten lunch today, thanks!")
        add_his_stuff.write("\nFood")
        with open("Personal_Inventory.txt", "r") as f:
            lines = f.readlines()
        with open("Personal_Inventory.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != "Food":
                    f.write(line)

    if response3 == "sword":
        print("I just sold this to you, but ok.")
        add_his_stuff.write("\nSword")
        with open("Personal_Inventory.txt", "r") as f:
            lines = f.readlines()
        with open("Personal_Inventory.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != "Sword":
                    f.write(line)

    if response3 == "axe":
        print("I thought you liked it...")
        add_his_stuff.write("\nAxe")
        with open("Personal_Inventory.txt", "r") as f:
            lines = f.readlines()
        with open("Personal_Inventory.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != "Axe":
                    f.write(line)

    if response3 == "potion":
        print("Well, fine. Give it back.")
        add_his_stuff.write("\nPotion")
        with open("Personal_Inventory.txt", "r") as f:
            lines = f.readlines()
        with open("Personal_Inventory.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != "Potion":
                    f.write(line)

    if response3 == "arrows":
        print("The point was to get rid of these, kid.")
        add_his_stuff.write("\nArrows")
        with open("Personal_Inventory.txt", "r") as f:
            lines = f.readlines()
        with open("Personal_Inventory.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != "Arrows":
                    f.write(line)

else:
    print("\nFine, I thought we were friends.")


# ---------------------------------------------------------------------------------------------------------------------#
#                                              END AND CLOSE TEXT FILES                                                #
# ---------------------------------------------------------------------------------------------------------------------#


read_his_stuff.close()
#add_his_stuff.close()  <------ ERROR ERROR
read_your_stuff.close()
#add_your_stuff.close() <----- FOUND THE ERROR! DON"T INCLUDE THIS LINE FOR WRITING TO FILES!
