'''
Write a program, which reads heights (inches.) of customers into a list and convert these
heights to centimeters in a separate list using:
1) Nested Interactive loop.
2) List comprehensions
Example: L1: [150,155, 145, 148]
Output: [68.03, 70.3, 65.77, 67.13]'''
#Inches = centimeter/2.54
#Centimeters=Inches×2.54
n = int(input("Enter no of items in list : "))
L1=[]
for i in range(n):
    L1.append(int(input("Enter heights of customers : ")))

L2 = []
for i in L1:
    L2.append(round(i*2.54))
print(L2)

#using List Comprehensions
listComphrensions = []
listComphrensions = [round(i * 2.54) for i in L1]
print(listComphrensions)
