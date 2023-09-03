print("DIctinory")
#Dictinory are use to store key value pairs 
#Dictinory are not allow duplicates
#Dictinory are changeable
dict = {
    "Fruit": "Apple",
    "Mobile": "Samsung",
    "Watch": "Touch"
}
dict.update({
    "vagetable": "Lady Finger",
    "Boy": "Girl"
})

print(dict)
dict.popitem()
print(dict)
print(dict.values())
print(dict.keys())
print(dict["Watch"])

for Dict in dict:
    print(Dict)
print(dict)
for Dict in dict:
    print(dict[Dict])
print("Dictinory in Loop")
for Dict1 in dict.keys():
    print(Dict1)

for Dict2 in dict.values():
    print(Dict2)

for Dict3 in dict.items():
    print(Dict3)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)