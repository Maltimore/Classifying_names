# this file was only used to extract names from the persondata_en dataset and is
# is not important anymore since I saved the extracted names

file = open("persondata_en.nt", "r")

names = set()
for i, line in enumerate(file.readlines()[1:-1]):
    if i%100000 == 0:
        print(str(i) + " lines processed")

    # some dataset specific splitting here, becomes obvious if you look at the file
    whole_string = line.split("/")[4].split(">")[0]
    
    # sometimes there was specific information about that person
    # in brackets directly behind the name (usually the occupation)
    whole_string = whole_string.split("(")[0]

    # remove commas
    whole_string = whole_string.replace(",", "")

    # there can be double names like argandas-carreras, in that case usually
    # both names are acceptable also as single names, so we split them
    whole_string = whole_string.replace("-", "_")

    # get all names separately
    words = whole_string.split("_")
    for word in words:
        names.add(word.lower())

with open("names.txt", "w") as f:
    for name in names:
        f.write(name + "\n")

file.close()

