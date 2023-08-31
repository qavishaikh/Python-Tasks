q = ["qavi","is","a","good","boy"]
print(q)

for a in q:
    print(a)

print("Second Statement")

numbers = [1,4,5,10,20]
sum = 0
for num in numbers:
    sum += num
print("Sum",sum)

print("Third Statement")

fruits = ["apple", "banana", "orange", "grape"]
for fruit in fruits:
    print("I like", fruit + "s")

print("4 Statement")

numbers1 = [17, 42, 822, 99, 23]
max_num = numbers1[0]
for num in numbers1:
    if num > max_num:
        max_num = num
print("Maximum:", max_num)

print("5 Statement")


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(element, end=" ")
    print() 

print("6 Statement")

fruits = ["apple", "banana", "orange", "grape"]
for index, fruit in enumerate(fruits):
    print("Fruit at index", index, ":", fruit)


