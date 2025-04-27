def sort_nu():
    numbers = []
    
    for i in range(5):
        num = int(input("Enter a number: "))
        numbers.append(num)
    
    print(f"The numbers you entered: {numbers}")
    
    ascending = sorted(numbers)
    print(f"Ascending order: {ascending}")   
    descending = sorted(numbers, reverse=True)
    print(f"Descending order: {descending}")

sort_nu()
