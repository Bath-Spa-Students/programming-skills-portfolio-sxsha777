
#Heterogenous list
x=["Sasha", 18, "Bathspa", "Creative Computing"]
print(x)

#Homogenous list
y=["a", "b", "c"]
print(y)

#Repitition
z=[1,3,5,7,9]
print(z*3)

#negative and positive indexing
print(z[-3])
print("Number  of elements in the list: ", len(z))

#mutability
l=[1,3,4,5]
print(l)
l[3]=7
print(l)

#concatenation
m=[1,2,3,4]
n=[7,8,9,10]
q=m+n
print(q)

#list slicing
nl=[3,4,5,6,7]
print(nl[0:3])

#if in/not in
list_=[1,3,4,7,10]
if 5 not in list_:
    print("yes")
else:
    print("no")
if 7 in list_:
    print("item found")
else:
    print("not found")

#built-in method : append
k=(1204, 309, 218, 912, 1013, 1230, 901)
j=[613]
k.append(j)
k.remove(613)
k.reverse()