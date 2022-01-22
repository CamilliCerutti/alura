
palavras = []

arquivo = open('palavras.txt', 'r')


print(len(arquivo))

for linha in arquivo:
    linha = linha.strip()
    palavras.append(linha)

print()
