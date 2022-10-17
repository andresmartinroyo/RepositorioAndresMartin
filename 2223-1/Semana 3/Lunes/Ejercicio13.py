asignaturas = ["Física 2", "Matemáticas Discretas", "Algoritmos y Programación", "Optimización 1"]
notas=[]
for i in asignaturas:
    n = input(f"Introducee la calificación que obtuviste en {i} ")
    notas.append(n)
for i in range(len(notas)):
    print("En " + asignaturas[i] +"obtuviste un " +notas[i])