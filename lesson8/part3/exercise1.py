dictionary = {
    "ιταμός": "Προκλητικός, αυθάδης, αναιδής",
    "όνειδος":"ντροπή, καταισχύνη",
    "πομφόλυγες":"αερολογίες, ανοησίες",
}

print(dictionary)
dictionary["φληναφήματα"] = "ανοησίες, σαχλαμάρες"
dictionary_key = input("type a dictionary-key: ")
dictionary_value = input("type a dictionary-value: ")

dictionary[dictionary_key] = dictionary_value
print(dictionary)
