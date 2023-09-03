myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)
print(myfamily["child2"]["name"])

for child_key, child_value in myfamily.items():
    print(f"Child: {child_key}")

    for key, value in child_value.items():
        print(f"{key}: {value}")
    print()