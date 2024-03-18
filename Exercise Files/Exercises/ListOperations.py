# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("\n========List Operations========\n")

motorcycles = ['honda','suzuki','yamaha']
print(motorcycles)

print(f"motorcycles[2] = {motorcycles[2]}")

print("motorcycles[1] = {}".format(motorcycles[1]))

print(f"motorcycles[-1] = {motorcycles[-1]}")
print(f"title case motorcycles[-1] = {motorcycles[-1].title()}")
print(f"upper case motorcycles[-1] = {motorcycles[-1].upper()}")

message = f"My favourite motorcycle is {motorcycles[-1].title()}"
print(message)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('bajaj')
print(motorcycles)

# append elements end of the list
planes = []
planes.append('hornet')
planes.append('falcon')
planes.append('growler')
print(planes)

# inserting elemets at index position
planes.insert(0, 'rafale')
print(planes)

# removing elemets from list
del planes[0]
print(planes)

# removing elements using pop method
popped_plane = planes.pop()
print(planes)
print(popped_plane)

popped_plane = planes.pop(0)
print(planes)
print(popped_plane)

print(len(planes))

planes.insert(len(planes), 'typhoon')
print(planes)

print(f"in reverse {motorcycles.reverse()}")
print(f"sorted motorcycles = {motorcycles.sort()}")
print(f"Reversely sorted motorcycles = {motorcycles.sort(reverse=True)}")

listOfProgLanguages = ['Perl','C','Java']
print('=====Printing list of programming languages. =====')
print(f"listOfProgLanguages   {listOfProgLanguages}")
print("listOfProgLanguages    {}".format(listOfProgLanguages))


listOfJunkCharacters = ['abcd', 'efgh', 'ijk']
print(f"Printing the list of junk characters     {listOfJunkCharacters}")
print("Printing the list of junk characters    {}".format(listOfJunkCharacters))

print(f"Last index of listOfJunkCharacters      {listOfJunkCharacters[-1]}")
print("Last index of listOfJunkCharacters     {}".format(listOfJunkCharacters[-1]))