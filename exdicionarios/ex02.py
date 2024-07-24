def juntar_dicionarios(dict1, dict2):
    dict3 = dict1.copy()  # Faz uma cópia de dict1
    dict3.update(dict2)   # Atualiza dict3 com os elementos de dict2
    return dict3

# Código de teste
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
resultado = juntar_dicionarios(dict1, dict2)
print(resultado) 
