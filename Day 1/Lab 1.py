#Write a program that counts up the number of vowels [a, e, i, o, u]contained in the string.
x = input("Please enter your text : ")
word= str(x)
y=0
vowels = ['a','e','o','u','i']
for i in x:
    if i in vowels:
       y+=1
       print("no of vowels: ",y)

 
