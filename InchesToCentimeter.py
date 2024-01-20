'''
Write a program, which reads heights (inches.) of customers into a list and convert these
heights to centimeters in a separate list using:
1) Nested Interactive loop.
2) List comprehensions
Example: L1: [150,155, 145, 148]
Output: [68.03, 70.3, 65.77, 67.13]'''
#Centimeters=Inches×2.54
L1 = [150,155,145,148]
interactiveLoop = []
for i in L1:
    interactiveLoop.append(round(i*2.5))
print(interactiveLoop)

#using List Comprehensions
listComphrensions = []
listComphrensions = [round(i * 2.5) for i in L1]
print(listComphrensions)
