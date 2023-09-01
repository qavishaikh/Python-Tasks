mytuple = ("apple", "banana", "cherry")
print(mytuple)
print(len(mytuple))
print(type(mytuple))
for x in mytuple:
    print(x)

# update Tupple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

A = ("Qavi","Ali","Hamdan","Hussain")
B = ("Aliza","Iqra","Areena","Fiza")
C = A+B
print(C)