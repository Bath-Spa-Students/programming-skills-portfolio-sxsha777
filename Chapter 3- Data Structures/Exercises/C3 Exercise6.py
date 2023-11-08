'''You just found out that your new dinner table won’t arrive in time for the dinner, 
and you have space for only two guests.
•Start with your program from Exercise 3-5. Add a new line that prints a message saying 
that you can invite only two people for dinner.
•Use pop() to remove guests from your list one at a time until only two names remain in your list. 
Each time you pop a name from your list, print a message to that person letting them know 
you’re sorry you can’t invite them to dinner.
•Print a message to each of the two people still on your list, letting them know 
they’re still invited.
•Use del to remove the last two names from your list, so you have an empty list. 
Print your list to make sure you actually have an empty list at the end of your program.'''

guests=['Rona', 'Tom', 'Lyney']

name=guests[0]
print(name, ",", "please join me for dinner.")
name=guests[1]
print(name, ",", "please join me for dinner.")
name=guests[2]
print(name, ",", "please join me for dinner.")
name=guests[1]
print("\n", name, "can not make it to dinner.")

#Tom can't make it to dinner. Let's invite Aether instead.
del(guests[1])
guests.insert(1, "Aether")

#Resending Invitations.
print("\n")
name=guests[0]
print(name, ",", "please join me for dinner.")
name=guests[1]
print(name, ",", "please join me for dinner.")
name=guests[2]
print(name, ",", "please join me for dinner.")

print("\n")
print("We have now made a reservation for a bigger table")
guests.append("Loisa")
guests.insert(0, "Nyx")
print("\n")

name=guests[0]
print(name, ",", "please join me for dinner.")
name=guests[1]
print(name, ",", "please join me for dinner.")
name=guests[2]
print(name, ",", "please join me for dinner.")
name=guests[3]
print(name, ",", "please join me for dinner.")
name=guests[4]
print(name, ",", "please join me for dinner.")
print("\n")
x=guests.pop()
print("Sorry for the inconvience,", x, ". You have been uninvited.")
x=guests.pop()
print("Sorry for the inconvience,", x, ". You have been uninvited.")
x=guests.pop()
print("Sorry for the inconvience,", x, ". You have been uninvited.")

print("\n")
name=guests[0]
print(name, ",", "please join me for dinner.")
name=guests[1]
print(name, ",", "please join me for dinner.")
del(guests[0])
del(guests[0])

print(guests)