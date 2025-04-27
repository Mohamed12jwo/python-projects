"""#Write a program that generate a multiplication table from 1 to the number passed.
x = input("enter a number: ")
word= int(x)

for i in range(1, word):
    for j in range(1, i + 1):  
        print(f"{i}*{j}={i*j}")
    print(" ") 
"""

user = []
for i in range(5):
    num=int(input("enter "))
    user.append(num)
    asc = sorted(user)
    des= sorted(user, reverse=True)
print("Acending is ", asc)
print("descending is",des)



multi= int(input("enter no to multiply "))
for i in range(1,multi):
    for j in range(1,i):
        print(f"{i}*{j}={i*j}")
    
