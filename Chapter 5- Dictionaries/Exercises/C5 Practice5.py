'''Write a Python program to merge two dictionaries into one.'''

dict1={1: "Ivy", 2: "Rani", 3: "Tom", 4: "Maria"}
dict2={5: "Anne", 6: "Gabrielle", 7: "Mia", 8: "Elsa"}

dict3=(dict1 | dict2)
print(dict3)
