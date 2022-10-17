def word_counter(phrase):
    phrase=phrase.split(" ")
    counter={}
    for i in phrase:
        if i in counter:
            counter[i]+=1
        else:
            counter[i]=1
    return counter

def most_repeated(counter):
    max_word=""
    max_frquency=0
    for word,frequency in counter.items():
        if frequency>max_frquency:
            max_frquency=frequency
            max_word=word
    return(max_word, max_frquency)

print(word_counter('Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'))
print(most_repeated(word_counter('Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera')))