

# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------  ALAN BURNS - SHOP ----------------------------------------------------- #
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
# Removing items from inventories [--DONE-- June 23 - Alan]
# Currency system: checking amount, incrementing or decrementing amount [Not started]
# Introducing more compact methods (loops?) [Not started]
# Let the user loop back to normal trade after giveaway (code currently exits after giveaway) [--DONE-- June 23 - Alan]
# Increase random number generator range to cover arbitrary sizes of the merchant's list [Not started]
# Generalizing user responses to account for capitalization and slight misspellings [Not started]
# Output text files to excel formats [Not started]
# Update inventories in real time [Not started]
# Prompt to buy/sell an arbitrary number of times [Near completion]
# Quantity of items in inventories [Not started]
# Generate text file to serve as a receipt for the user and merchant [Not started]


# NOTE
# INCLUDE A TEXT FILE "Merchant_Inventory.txt" with four preset items: sword, axe, potion, arrows.
# INCLUDE A TEXT FILE "Personal_Inventory.txt" with two preset items: mace and food.
# Written in PyCharm


# -------------------------------------------------------------------------------------------------------------------- #
#                                   OPEN TEXT FILES FOR READING FROM AND WRITING TO                                    #
# -------------------------------------------------------------------------------------------------------------------- #


import random                                           # Imports the random library to generate random integers.

#merchant_inventory = ["Sword", "Axe", "Potion", "Arrows"]
#user_inventory = ["Mace", "Food"]

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
    #user_inventory.append(merchant_inventory[roll])  # Add item to user inventory (broken)

else:
    print("Ah, unfortunate.")

buy_or_sell = input("Do you care to buy something today?\n")
if buy_or_sell == "yes":
    buy_or_sell = True
elif buy_or_sell == "no":
    buy_or_sell = False
else:
    buy_or_sell = True
    print("I'll just take that as you wanting to buy.")
    
    
          # --- Normal Purchasing Mode - Adds item to user inventory, deletes from merchant inventory --- #

while buy_or_sell:      
      
  print("\nHave a look at my wares: \n")    

  #for items in read_his_stuff.readlines(): # Print out merchant's inventory to the user
  #    print(items)

  for items in read_his_stuff.readlines():
      print(items)
  
  response1 = input("Which of these fancies you?")
  
  # SWORD #
  if response1 == "sword":
        print("Don't poke your eye out.")

        #user_inventory.append("Sword")
        #merchant_inventory.remove("Sword")


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

      #user_inventory.append("Axe")
      #merchant_inventory.remove("Axe")


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

      #user_inventory.append("Potion")
      #merchant_inventory.remove("Potion")


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

      #user_inventory.append("Arrows")
      #merchant_inventory.remove("Arrows")


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

      #user_inventory.append("Mace")
      #merchant_inventory.remove("Mace")


      add_your_stuff.write("\nMace")
      with open("Merchant_Inventory.txt", "r") as f:
          lines = f.readlines()
      with open("Merchant_Inventory.txt", "w") as f:
          for line in lines:
              if line.strip("\n") != "Mace":
                  f.write(line)


  # FOOD #
  elif response1 == "food":
      print("Bon appetit!")

      #user_inventory.append("Food")
      #merchant_inventory.remove("Food")


      add_your_stuff.write("\nFood")
      with open("Merchant_Inventory.txt", "r") as f:
          lines = f.readlines()
      with open("Merchant_Inventory.txt", "w") as f:
          for line in lines:
              if line.strip("\n") != "Food":
                  f.write(line)


  else:
      print("We only speak English here, kid.") # Response to unrecognizable input
      
  buy_or_sell = input("Do you care to purhase more?")
  if buy_or_sell == "no":
    buy_or_sell = False


# ---------------------------------------------------------------------------------------------------------------------#
#               SELL YOUR ITEMS TO THE MERCHANT BY APPENDING MERCHANT INVENTORY - Merchant_Inventory.txt               #
# ---------------------------------------------------------------------------------------------------------------------#

buy_or_sell = input("Care to sell?")
if buy_or_sell == "yes":
  buy_or_sell = False
else:
  buy_or_sell = True

while not buy_or_sell:

    print("Alright! Always looking to increase my inventory.")

    for items in read_your_stuff.readlines(): # Print out user inventory for selection
        print(items)
  
    response2 = input("What do you want to sell? \n")

    if response2 == "mace":
        print("I'd love to take that mace off your hands!")
        add_his_stuff.write("\nMace")
        with open("Personal_Inventory.txt", "r") as f:
            lines = f.readlines()
        with open("Personal_Inventory.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != "Mace":
                    f.write(line)

    if response2 == "food":
        print("I haven't eaten lunch today, thanks!")
        add_his_stuff.write("\nFood")
        with open("Personal_Inventory.txt", "r") as f:
            lines = f.readlines()
        with open("Personal_Inventory.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != "Food":
                    f.write(line)

    if response2 == "sword":
        print("I just sold this to you, but ok.")
        add_his_stuff.write("\nSword")
        with open("Personal_Inventory.txt", "r") as f:
            lines = f.readlines()
        with open("Personal_Inventory.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != "Sword":
                    f.write(line)

    if response2 == "axe":
        print("I thought you liked it...")
        add_his_stuff.write("\nAxe")
        with open("Personal_Inventory.txt", "r") as f:
            lines = f.readlines()
        with open("Personal_Inventory.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != "Axe":
                    f.write(line)

    if response2 == "potion":
        print("Well, fine. Give it back.")
        add_his_stuff.write("\nPotion")
        with open("Personal_Inventory.txt", "r") as f:
            lines = f.readlines()
        with open("Personal_Inventory.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != "Potion":
                    f.write(line)

    if response2 == "arrows":
        print("The point was to get rid of these, kid.")
        add_his_stuff.write("\nArrows")
        with open("Personal_Inventory.txt", "r") as f:
            lines = f.readlines()
        with open("Personal_Inventory.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != "Arrows":
                    f.write(line)

    else:
        print("\nEnglish, please!")
        
    buy_or_sell = input("Do you care to sell more?")
    if buy_or_sell == "yes":
        buy_or_sell = False
    else:
        buy_or_sell = True


# ---------------------------------------------------------------------------------------------------------------------#
#                                              END AND CLOSE TEXT FILES                                                #
# ---------------------------------------------------------------------------------------------------------------------#


read_his_stuff.close()
read_your_stuff.close()
