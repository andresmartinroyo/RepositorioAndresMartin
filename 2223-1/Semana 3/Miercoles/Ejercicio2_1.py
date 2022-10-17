translate = {}
words = input("Introduce a list of words with their translation in the following format: <palabra>:<word>,\n\n")
for i in words.split(","):
    key, value=i.split(":")
    translate[key] = value
phrase= input("Insert a phrase: \n")
for i in phrase.split(" "):
    if i in translate:
        print(translate[i], end=" ")
    else:
        print(i, end=" ")