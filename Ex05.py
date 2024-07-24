# Escreva uma função chamada is_sorted que tome uma lista como parâmetro e retorne True se a lista estiver classificada em ordem ascendente, e
# False se não for o caso.
def is_sorted(lista):
    return lista == sorted(lista)

print(is_sorted([1, 2, 2]))  # Saída: True
print(is_sorted(['h', 'a']))  # Saída: False
