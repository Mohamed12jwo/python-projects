list = [{"name":"omar","pass":"123"},{"name":"ahmed","pass":"456"}]
def authenticate_user(List):
    for user in List:
        user["name"] = user["name"].lower()

    username = input("Enter name: ").lower()
    x = 0

    for user in List:
        if user["name"].lower() == username.lower():
            x = user
            break

    if x:
        while True:
            password = input("Enter pass: ")
            if password == x["pass"]:
                print("Right pass")
                break
            else:
                print("Wrong pass")
    else:
        print("User not here")
