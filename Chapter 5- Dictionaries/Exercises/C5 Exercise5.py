'''Make several dictionaries, where each dictionary represents a different pet. 
In each dictionary, include the kind of animal and the owner's name. 
Store these dictionaries in a list called pets. 
Next, loop through your list and as you do, print everything you know about each pet'''

pets_info=[]

pet={"Owner": "Anne", "Name": "Angel", "Type": "Cat", "Weight": "4kg"}
pets_info.append(pet)

pet={"Owner": "Mini", "Name": "Kylee", "Type": "Dog", "Weight": "5kg"}
pets_info.append(pet)

pet={"Owner": "Sasha", "Name": "Ruby", "Type": "Cat", "Weight": "5kg"}
pets_info.append(pet)

for pet in pets_info:
    print()
    for x, y in pet.items():
        print(x,": ",str(y))
