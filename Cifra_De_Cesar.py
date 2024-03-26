contagem = 0
casos = int(input())
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
palavras = []

while contagem < casos:
    palavra = str(input()).upper()
    numero = int(input())
    tamanho = len(palavra)
    nova_palavra = ""

    for pos in range(0, len(palavra)):
        index = alfabeto.index(palavra[pos]) - numero

        if index <= 25:
            nova_palavra += alfabeto[index]
        else:
            nova_palavra += alfabeto[index-25]

    palavras.append(nova_palavra)
    contagem += 1

for i, p in enumerate(palavras):
    print(p)
