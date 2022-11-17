import requests
import json

informacion=requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json")
file=open("prueba.txt","w")
file.write(informacion.text)
file.close()