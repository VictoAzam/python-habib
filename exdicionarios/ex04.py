def criar_dicionario_quadrados(k):
    return {i: i**2 for i in range(1, k+1)}


k = 15
resultado = criar_dicionario_quadrados(k)
print(resultado)

