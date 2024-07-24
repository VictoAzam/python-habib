# Escreva uma função chamada nested_sum que receba uma lista de listas de
# números inteiros e adicione os elementos de todas as listas aninhadas.
def nested_sum(lista_de_listas):


    soma_total = 0
    for sublista in lista_de_listas:
        for numero in sublista:
            soma_total += numero
    return soma_total

t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))  # saida: 21
