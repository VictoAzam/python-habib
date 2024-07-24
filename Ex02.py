# Escreva uma função chamada cumsum que receba uma lista de números e
# retorne a soma cumulativa; ou seja, uma nova lista onde o elemento com
# índice i é a soma dos primeiros i+1 elementos da lista original.
def cumsum(lista):
    soma_acumulada = 0
    resultado = []
    for numero in lista:
        soma_acumulada += numero
        resultado.append(soma_acumulada)
    return resultado

t = [1, 2, 3]
print(cumsum(t)) 
