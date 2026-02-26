notas = input("digite sus notas separadas por una ,: ")
notas = notas.split(",")
notas = [float (nota) for nota in notas]
promedio =sum(notas) / len(notas)
print(f"el promedio de sus notas es: {promedio}")
