# Escreva uma função chamada chop que tome uma lista alterando-a para remover o primeiro e o último elementos, e retorne None
def chop(lista):
    if len(lista) > 1:
        del lista[0]
        del lista[-1]
    else:
        lista.clear()
    return None

t = [1, 2, 3, 4]
print(chop(t))  # saida: None
print(t)        # saida: [2, 3]
