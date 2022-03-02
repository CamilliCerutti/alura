# url = 'bytebank.com/cambio?moedaDestino=Dolar&Quantidade=100&moedaOrigem=Real'
url = ' '

# Sanitização da URL
url = url.strip()

# validação da URL
if url == '':
    raise ValueError('A url está vazia')


# Separa base e parametros
indice_interrogacao = url.find('?')

url_base = url[:indice_interrogacao]

url_parametros = url[indice_interrogacao + 1:]
print(url_parametros)


# Busca o valor de um parametro
paramtro_busca = 'Quantidade'
indice_parametro = url_parametros.find(paramtro_busca)
indice_valor = indice_parametro + len(paramtro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == - 1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)