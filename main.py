QTD_notas = int(input("Digite a quantidade de nota: "))
notas = []

for i in range(QTD_notas):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

total_notas=0
for nota in notas:
      total_notas+=nota

media = total_notas/ len(notas)

if media >=7:
      print ("Desempenho Satisfatório..  ")  
else:
      print ("Desempenho Insatisfatório..  ")