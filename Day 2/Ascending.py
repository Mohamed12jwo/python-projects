numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

print("The numbers you entered:", numbers)

ascending = sorted(numbers)
print("Ascending order:", ascending)

descending = sorted(numbers, reverse=True)
print("Descending order:", descending)
