'''Write a Python program that uses the break statement to exit a for loop when a specific
condition is met.'''

cars=("mustang", "bughatti", "hyundai", "porsche", "honda")
x=input("Enter a automobile brand: ")
for i in cars:
   print(i)
   if i == x:
      print("you love", x)
      break


      

   

   
