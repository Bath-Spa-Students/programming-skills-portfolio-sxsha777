'''Given a Python list, write a program to remove all occurrences 
of item 20. Given list:
 list1 = [5, 20, 15, 20, 25, 50, 20]'''

list1 = [5, 20, 15, 20, 25, 50, 20]
def remove_num(list, number):
    return [val for val in list if val!=number]

a = remove_num(list1, 20)
print(a)