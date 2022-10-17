from argparse import RawTextHelpFormatter


txt = input("Escribe una palabra: ")
txt2 = txt
txt =list(txt)
txt2= list(txt2)
txt2.reverse()
if txt == txt2:
    print("Es un palindromo")
