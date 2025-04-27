number= int(input("please enter no "))
table = []

for i in range(1, number+1):
    listt=[]
    for j in range(1, i+1):
        listt.append(i * j)
        table.append(listt)
print(table)
