nome_alunos = ["Antonio", "Idalguinho", "Fefe", "Eztefania", "Luzkinha", "Rapaizinho de rosa", "Didi", "Leandrinho do Grau", "Lele"]

print(f"{nome_alunos} ")

for aluno in nome_alunos:
    print(aluno)

veiculos = ["Fusca", "Doblo", "Marea Turbo", "Tiggo", "Uno", "Gol Bolinha", "d20", "Veraneio", "chevette"]

#Outros carros: Nome de carro + carro legal
# D20, Veraneio e chevette: nome do carro + carro classico

for veiculo in veiculos:
    if veiculo in ("d20", "Veraneio", "chevette"):
        print(f"{veiculo} carro classico!")
    else:
        print(f"{veiculo} carro legal!")