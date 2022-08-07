
name = input("Whats your name?").strip().title()

"""
 #To strip down the left and right spaces of input(ut does not 
 strip down sopaces in beteen words)
  name = name.strip()

#To capitalize the word(But it will only capitalize the first one)
  name = name.capitalize()

 #To Capitalize all the words of input
  name = name.title()

# All in one line
    name = name.strip().title()
"""

# TO split between first name or last name

first, last = name.split("    ")
# f string is special type of string, when code finds it it will
# treat it differently, it sits right before the " "
print(f"Hello, {first}")
