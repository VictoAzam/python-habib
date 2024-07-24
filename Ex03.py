# Escreva uma função chamada middle que receba uma lista e retorne uma
# nova lista com todos os elementos originais, exceto o primeiro e o último
# elementos.
def middle(lista):
    return lista[1:-1]

t = [1, 2, 5, 7, 3, 4]
print(middle(t))  
