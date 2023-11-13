'''Assume the lists numbers1 has 100 elements and numbers2 is an empty list. Write code that
copies the values in numbers to numbers2.'''

numbers1=[7]*100
print(numbers1)

numbers2=[]
numbers2.append(numbers1)
print("numbers2: \n", numbers2)
print("numbers1: \n", numbers1)
