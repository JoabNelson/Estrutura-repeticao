'''
Estrutura de repetição

O que é uma estrutura de repetição ? 

-> serve para executar um bloco de codigo varias vezes
-> ENQUANTO UMA CONDIÇÃO FOR VERDADEIRA (TRUE)

'''

# variavel =  True # Boolean
#contador = 10

#while contador >= 0:
#    print(contador)
#    contador = contador - 1

'''
Qual a logica de uma tabuada ?  quero fazer uma tabuada do 5 e deve mostrar o seguinte
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15

'''

tabuada =  5
contador = 0

while  contador <= 10:
    print(tabuada, "x", contador, "+", contador * tabuada)
    contador += 1