def print_pyramid(height):
    for i in range(1, height + 1):
        spaces = height - i
        stars = i
        print(f"{' ' * spaces}{'*' * stars}")


height = int(input("Enter the height  "))
print_pyramid(height)
