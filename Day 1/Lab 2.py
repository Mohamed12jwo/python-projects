#Write a program that prints the locations of "i" character in any string you added.
x = input("Please enter your text: ")
word = str(x)
for i in range(len(word)):
    if word[i]== "i":
        print("Found i  at :", i)