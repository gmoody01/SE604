'''


           /\                                                                                               /\
 _         )( ________________________________________            ________________________________________  )(         _
(_)///////(**)________________________________________>          <________________________________________(**)\\\\\\\(_)
           )(                                                                                              )(
           \/                                                                                              \/
                                         ::::::::  :::    :::  ::::::::  :::::::::
                                        :+:    :+: :+:    :+: :+:    :+: :+:    :+:
                                        +:+        +:+    +:+ +:+    +:+ +:+    +:+
                                        +#++:++#++ +#++:++#++ +#+    +:+ +#++:++#+
                                               +#+ +#+    +#+ +#+    +#+ +#+
                                        #+#    #+# #+#    #+# #+#    #+# #+#
                                         ########  ###    ###  ########  ###

           /\                                                                                               /\
 _         )( ________________________________________            ________________________________________  )(         _
(_)///////(**)________________________________________>          <________________________________________(**)\\\\\\\(_)
           )(                                                                                              )(
           \/                                                                                              \/


CONTRIBUTORS

    Alan Burns - Creator
    Allan Lang - Editor


FUNCTION

    Implements a mock trade between a customer and a merchant (ye olden style). Purchasing items results in appending a
    text file, much like a growing inventory. Selling items results in appending a different text file (the merchant's)
    in a similar way.

    Implements the random library to determine a random number between 0 and 3. This is to determine a random giveaway
    at the merchant's shop, given that the user has a "luck stone" (user answers yes or no).


IN DEVELOPMENT
(Don't delete from list, note progress or say DONE)

    Import from .csv rather than .txt ---------------------------------------------------------------------[Not started]
    Removing items from inventories -------------------------------------------------------[DONE - June 23 - Alan Burns]
    Currency system: checking amount, incrementing or decrementing amount ---------------------------------[Not started]
    Introducing more compact methods (loops?) -------------------------------------------------------------[Not started]
    Let the user loop back to normal trade after giveaway ---------------------------------[DONE - June 23 - Alan Burns]
    Increase random number generator range to cover arbitrary sizes of the merchant's list ----------------[Not started]
    Generalizing user responses to account for capitalization and slight misspellings ---------------------[Not started]
    Output text files to excel formats (.csv) -------------------------------------------------------------[Not started]
    Update inventories in real time -------------------------------------------------------[DONE - June 25 - Allan Lang]
    Prompt to buy/sell an arbitrary number of times ---------------------------------------------------[Near completion]
    Quantity of items in inventories ----------------------------------------------------------------------[Not started]
    Generate text file to serve as a receipt for the user and merchant ------------------------------------[Not started]
    Random giveaway code is broken ----------------------------------------------------------------------------[Started]


NOTE
    INCLUDE A TEXT FILE "Merchant_Inventory.txt" with four preset items: sword, axe, potion, arrows.
    INCLUDE A TEXT FILE "Personal_Inventory.txt" with two preset items: mace and food.
    Written in PyCharm'''


# -------------------------------------------------------------------------------------------------------------------- #
#                                           IMPORT LIBRARIES AND MODULES                                               #
# -------------------------------------------------------------------------------------------------------------------- #


import random
import csv


# -------------------------------------------------------------------------------------------------------------------- #
#                           INTRODUCTION AND RANDOM GIVEAWAY - PROMPT BUYING OR SELLING                                #
# -------------------------------------------------------------------------------------------------------------------- #


# Introduction
print("\nWelcome to my shop, weary traveller.\nI have some things you may find helpful.\n")

# Prompt user input for random giveaway
luck_response = input("Are you carrying a luck stone? \n")

# Random giveaway
if luck_response == "yes":
    print("\nGreat! That means you get a free item from my shop!")
    roll = random.randint(0, 9)  # Generates random integer
    read_his_stuff = open("Merchant_Inventory.txt", "r")
    add_your_stuff = open("Merchant_inventory.txt", "a")
    print("Today you get................. a " + read_his_stuff.readlines()[roll]) # Declare item to be given
    #add_your_stuff.write(read_his_stuff.readlines()[roll])  # Add item to user inventory (broken)
    read_his_stuff.close()
    add_your_stuff.close()
else:
    print("Ah, unfortunate.")


# Prompt user to choose purchasing mode or selling mode
buy_or_sell = input("Do you care to buy something today?\n")
if buy_or_sell == "yes":
    buy_or_sell = True
elif buy_or_sell == "no":
    buy_or_sell = False
else:
    buy_or_sell = True
    print("I'll just take that as you wanting to buy.")


# -------------------------------------------------------------------------------------------------------------------- #
#               PURCHASE THE MERCHANT'S ITEMS BY APPENDING CUSTOMER INVENTORY - Personal_Inventory.txt                 #
# -------------------------------------------------------------------------------------------------------------------- #


# While buy_or_sell is True, proceed through lines 115 to 211
while buy_or_sell:

    # Open text files to read from the merchant and write to the user
    read_his_stuff = open("Merchant_Inventory.txt", "r")
    add_your_stuff = open("Personal_Inventory.txt", "a")
      
    print("\nHave a look at my wares: \n")

    # Print the merchant's inventory Merchant_inventory.txt
    for items in read_his_stuff.readlines():
          print(items)

    # Prompt user input to choose item listed
    response1 = input("Which of these fancies you?")

    # If user chooses sword...
    if response1 == "sword":
        print("Don't poke your eye out.")

        # Add "Sword" to Personal_Inventory.txt
        add_your_stuff.write("\nSword")

        # Delete "Sword" from Merchant_Inventory.txt
        with open("Merchant_Inventory.txt", "r") as f:
            lines = f.readlines()
        with open("Merchant_Inventory.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != "Sword":
                    f.write(line)

    # If user chooses axe...
    elif response1 == "axe":
        print("That's no hatchet, kid.")
        add_your_stuff.write("\nAxe")
        with open("Merchant_Inventory.txt", "r") as f:
            lines = f.readlines()
        with open("Merchant_Inventory.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != "Axe":
                    f.write(line)

    # If user chooses potion...
    elif response1 == "potion":
      print("You look like you need it.")
      add_your_stuff.write("\nPotion")
      with open("Merchant_Inventory.txt", "r") as f:
          lines = f.readlines()
      with open("Merchant_Inventory.txt", "w") as f:
          for line in lines:
              if line.strip("\n") != "Potion":
                  f.write(line)

    # If user chooses arrows...
    elif response1 == "arrows":
      print("It's because it's the cheapest, isn't it?")
      add_your_stuff.write("\nArrows")
      with open("Merchant_Inventory.txt", "r") as f:
          lines = f.readlines()
      with open("Merchant_Inventory.txt", "w") as f:
          for line in lines:
              if line.strip("\n") != "Arrows":
                  f.write(line)

    # If user chooses mace...
    elif response1 == "mace":
      print("Spiky!")
      add_your_stuff.write("\nMace")
      with open("Merchant_Inventory.txt", "r") as f:
          lines = f.readlines()
      with open("Merchant_Inventory.txt", "w") as f:
          for line in lines:
              if line.strip("\n") != "Mace":
                  f.write(line)

    # If user chooses food...
    elif response1 == "food":
      print("Bon appetit!")
      add_your_stuff.write("\nFood")
      with open("Merchant_Inventory.txt", "r") as f:
          lines = f.readlines()
      with open("Merchant_Inventory.txt", "w") as f:
          for line in lines:
              if line.strip("\n") != "Food":
                  f.write(line)

    # Response to unrecognizable input
    else:
      print("We only speak English here, kid.")

    # Close merchant's and user's inventories to update
    # for possible future purchasing
    read_his_stuff.close()
    add_your_stuff.close()

    # Prompt user to continue in the while loop or
    # move to selling mode
    buy_or_sell = input("Do you care to purchase more?")
    if buy_or_sell == "no":
        buy_or_sell = False


# ---------------------------------------------------------------------------------------------------------------------#
#               SELL YOUR ITEMS TO THE MERCHANT BY APPENDING MERCHANT INVENTORY - Merchant_Inventory.txt               #
# ---------------------------------------------------------------------------------------------------------------------#


# Update buy_or_sell boolean
buy_or_sell = input("Care to sell?")

if buy_or_sell == "yes":
    buy_or_sell = False
else:
    buy_or_sell = True


# Proceed to selling when buy_or_sell = False
while not buy_or_sell:

    # Open merchant's and user's inventories for reading
    # and writing
    read_your_stuff = open("Personal_Inventory.txt", "r")
    add_his_stuff = open("Merchant_Inventory.txt", "a")

    print("Alright! Always looking to increase my inventory.")

    # Print out user inventory for selection
    for items in read_your_stuff.readlines():
        print(items)

    # Prompt user to choose item to sell
    response2 = input("What do you want to sell? \n")

    # If user selects mace...
    if response2 == "mace":
        print("I'd love to take that mace off your hands!")

        # Add "Mace" to Merchant_inventory.txt
        add_his_stuff.write("\nMace")

        # Delete "Mace" from Personal_Inventory.txt
        with open("Personal_Inventory.txt", "r") as f:
            lines = f.readlines()
        with open("Personal_Inventory.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != "Mace":
                    f.write(line)

    # If user selects food...
    if response2 == "food":
        print("I haven't eaten lunch today, thanks!")
        add_his_stuff.write("\nFood")
        with open("Personal_Inventory.txt", "r") as f:
            lines = f.readlines()
        with open("Personal_Inventory.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != "Food":
                    f.write(line)

    # If user selects sword...
    if response2 == "sword":
        print("I just sold this to you, but ok.")
        add_his_stuff.write("\nSword")
        with open("Personal_Inventory.txt", "r") as f:
            lines = f.readlines()
        with open("Personal_Inventory.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != "Sword":
                    f.write(line)

    # If user selects axe...
    if response2 == "axe":
        print("I thought you liked it...")
        add_his_stuff.write("\nAxe")
        with open("Personal_Inventory.txt", "r") as f:
            lines = f.readlines()
        with open("Personal_Inventory.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != "Axe":
                    f.write(line)

    # If user selects potion...
    if response2 == "potion":
        print("Well, fine. Give it back.")
        add_his_stuff.write("\nPotion")
        with open("Personal_Inventory.txt", "r") as f:
            lines = f.readlines()
        with open("Personal_Inventory.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != "Potion":
                    f.write(line)

    # If user selects arrows...
    if response2 == "arrows":
        print("The point was to get rid of these, kid.")
        add_his_stuff.write("\nArrows")
        with open("Personal_Inventory.txt", "r") as f:
            lines = f.readlines()
        with open("Personal_Inventory.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != "Arrows":
                    f.write(line)

    # Response to unrecognizable input
    else:
        print("\nEnglish, please!")

    # Close inventories for possible future sales
    read_your_stuff.close()
    add_his_stuff.close()

    # Update buy_or_sell boolean to stay in the while loop
    # or exit code
    buy_or_sell = input("Do you care to sell more?")
    if buy_or_sell == "yes":
        buy_or_sell = False
    else:
        buy_or_sell = True


# ---------------------------------------------------------------------------------------------------------------------#
#                                                        END                                                           #
# ---------------------------------------------------------------------------------------------------------------------#
