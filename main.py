import csv

notas = []

with open("dados.csv","r")as arquivo:
    leitor = csv.reader(arquivo)

    next(leitor)

    for linha in leitor:
       nota = float(linha[1])
       notas.append(nota)

media = sum(notas) / len(notas)

print("total de alunos: ",len(notas))
print("Média da turna: ",media)
print("Menor nota: ",min(notas))
print("Maior nota: ",max(notas))