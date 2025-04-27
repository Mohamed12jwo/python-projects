user = input("Please enter name")

while user == "" or user.isdigit():
    print("Falsy Name ")
    user = input("Name again: ")

email = input("please enter Mail ")

if "@" in email and "." in email:
    print("mail is right.")
else:
    print("Mail not right.")

print("Name is :", user)
print("mail is :", email)