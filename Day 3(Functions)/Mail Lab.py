def namefu():
    while True:
        name = input("enter name: ")
        if name and not name.isdigit():
            return name
        else:
            print("Please enter a valid name (non-empty and not an integer).")
def mail():
    while True:
        email = input("enter mail: ")
        if '@' in email and '.' in email:
            
                username, domain = email.split('@')
                x, y = domain.split('.')
                if username and x and y:
                    return email
        print("Please enter a valid email address.")
x= namefu()
y= mail()
print("name:", x)
print("mail:", y)