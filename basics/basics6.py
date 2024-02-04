## dictionaries are like arrays but they use key value pairs instead of indexes

phonebook1={}
phonebook1["name1"]="123"
phonebook1["name2"]="456"
phonebook1["name3"]="789"
## print("phonebook1", phonebook1, phonebook1["name2"])

phonebook2={
    "name1":"123",
    "name2":"456",
    "name3":"789",
}
##print("phonebook2", phonebook2, phonebook2["name2"])

for item in phonebook1:             ## iterates through keys
    print(item)

for item1, item2 in phonebook1.items():         ## item1 will be key and item2 will be value
    print(item1, item2)

del phonebook2["name2"]             ## deletes a key value pair from dictionary
phonebook1.pop("name1")             ## other way to delete a key value pair

print(phonebook1)