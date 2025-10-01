from operator import index

ListOfThings = ["Egg", "Soap", "Chair", "Fan"]

print(ListOfThings[2])

# ListOfThings[3] = "TableFan"
# ListOfThings.remove(ListOfThings[1])
ListOfThings.insert(1, "Soap")
# ListOfThings.extend(["Item6", "Item7"])
indexToBeInserted = 1
ListOfThings[indexToBeInserted:indexToBeInserted] = ["Item2", "Item3","Item4"]

# ListOfThings.reverse()
# ListOfThings.sort()

print(ListOfThings)