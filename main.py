import csv

def calcular_media(notas):
    return sum(notas) / len(notas)

def situacao_estudante(media):    
    if media >= 7.0:
        situacao = "Aprovado"
        return situacao
    else:
        situacao = "Reprovado"
        return situacao


estudantes = [
    {"NOME": "Ana", "NOTAS": [6.7, 7.4, 9.2]}, 
    {"NOME": "Carlos", "NOTAS": [6.0, 5.4, 7.6]},
    {"NOME": "João", "NOTAS": [5.4, 8.5, 7.8]}, 
    {"NOME": "Maria", "NOTAS": [4.3, 6.3, 5.5]},
    {"NOME": "Pedro", "NOTAS": [7.0, 7.5, 8.0]},
    {"NOME": "Lucas", "NOTAS": [3.5, 4.0, 5.0]},
    {"NOME": "Fernanda", "NOTAS": [9.0, 8.5, 9.5]},
    {"NOME": "Juliana", "NOTAS": [6.0, 7.2, 8.4]},
    {"NOME": "Rafael", "NOTAS": [5.0, 6.3, 7.2]},
    {"NOME": "Beatriz", "NOTAS": [8.1, 8.7, 9.8]},
    {"NOME": "Gabriel", "NOTAS": [4.2, 5.8, 6.4]},
    {"NOME": "Larissa", "NOTAS": [7.0, 8.3, 9.1]},
    {"NOME": "Thiago", "NOTAS": [6.0, 5.3, 4.1]},
    {"NOME": "Camila", "NOTAS": [9.0, 8.2, 7.4]},
    {"NOME": "Felipe", "NOTAS": [5.0, 6.5, 7.0]},
    {"NOME": "Isabela", "NOTAS": [8.2, 9.1, 9.4]},
    {"NOME": "Mateus", "NOTAS": [7.5, 10.0, 8.5]},
    {"NOME": "Isabel", "NOTAS": [3.3, 7.3, 8.2]},
    {"NOME": "Vinicius", "NOTAS": [6.6, 6.8, 7.2]},
    {"NOME": "Amanda", "NOTAS": [5.2, 6.4, 7.0]}
]

aprovados = 0
reprovados = 0
soma_media = 0

for estudante in estudantes:
    notas = estudante["NOTAS"]
    media = calcular_media(notas)
    situacao = situacao_estudante(media)
    print(estudante["NOME"]," - ", "média: ",f"{media:.2f}", " - ", situacao)

    estudante["MÉDIA"] = media
    estudante["SITUAÇÃO"] = situacao
    soma_media += media

    if situacao == "Aprovado":
        aprovados += 1
    else:
        reprovados += 1

print("\nTotal de aprovados: ", aprovados)
print("Total de reprovados: ", reprovados)
print("\nMédia total da turma: ", f"{soma_media/len(estudantes):.2f}")

melhor_estudante = max(estudantes, key=lambda estudante: estudante["MÉDIA"])
pior_estudante = min(estudantes, key=lambda estudante: estudante["MÉDIA"])

print("\nMelhor estudante: ", melhor_estudante['NOME'], " - ", "Média: ", f"{melhor_estudante['MÉDIA']:.2f}")
print("Pior estudante: ", pior_estudante['NOME'], " - ", "Média: ", f"{pior_estudante['MÉDIA']:.2f}")

ranking = sorted(estudantes, key=lambda estudante: estudante["MÉDIA"], reverse=True)
print("\n==== RANKING DA TURMA ====")

for i, estudante in enumerate(ranking, start=1):
    if i > 5:
        break
    else:
      print(f"{i}° lugar: {estudante["NOME"]} - Média: {estudante["MÉDIA"]:.2f}")

with open("estudantes.csv", "w", newline="", encoding="utf-8-sig") as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames= ["NOME", "NOTAS", "MÉDIA", "SITUAÇÃO"])

    escritor.writeheader()
    estudantes_csv = []

    for estudante in estudantes:
        estudante_formatado = estudante.copy()
        estudante_formatado["MÉDIA"] = f"{estudante['MÉDIA']:.2f}"
        estudante_formatado["SITUAÇÃO"] = estudante['SITUAÇÃO']
        estudantes_csv.append(estudante_formatado)

    escritor.writerows(estudantes_csv)

