
with open("mass.txt", "r") as inputFile:
    fileContent = inputFile.read()

# print(fileContent)
myDictionary = {} # inititialize the dictionaryrare_keys = []


for char in fileContent: # loop through every character of the file
    if char not in myDictionary:
        myDictionary[char] = 1
    if char in myDictionary:
        myDictionary[char] += 1


rare_keys = []
for key in myDictionary: # looping through keys of dictionary to get its values
    if myDictionary[key] == 2:
        rare_keys.append(key)

myString = "".join(rare_keys) # Joining the list into a string
print(myString)
