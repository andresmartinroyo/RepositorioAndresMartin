translate = {}
traslation = input("Insert a words in spanish and its trsalation in english separated with two pints and at the end a coma: ")
translated_words = traslation.split(",")

for words in translated_words:
    translate[words.split(":")[0]] = words.split(":")[1]
phrase_to_translate=input("Introduce a phrase to translate: \n")
phrase_to_translate.split(" ")
phrase_transated=[]
for words in range(len(phrase_to_translate)):
    palabra=translate.get(words)
    phrase_transated.append(palabra)
for palabras in range(len(phrase_transated)):
    print(phrase_transated[palabra], end=" ")