'''
Tipo de Dados - python

Int = Números Inteiros
Float = Números Quebrados (Flutuantes)
String = Texto
Boolean =  Afirmação (TRUE ou FALSE)

List = lista
Uma coleção de valores que podemos guarda juntos em uma unica variável

'''

mochila = ["caderno", "dinheiro", "baralho", "relogio", 18000, "rtx 5080"]

compras = ["Abacaxi", "kiwi", "Arroz", "Goiaba", "Peixe"]

print(compras[0])
print(compras[2])
print(compras[4])

#item = input("Qual Item? ")
compras.append("Leite")
compras.append("Água Mineral")

print(len(compras))

print(compras)
'''
1. cada item da lista ocupa uma posição
2. Cada posição tem um número (índice)
3. Dá para pegar o item pela posição

// 5 Items

//0: Abacaxi
//1: Kiwi
//2: Arroz
...
compras = ["Abacaxi", "kiwi", "Arroz", "Goiaba", "Peixe"]

'''