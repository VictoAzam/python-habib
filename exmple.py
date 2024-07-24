# t=[[1,2] [3] [4,5,6]]
# i= 0

# for el in t:
#       print(el)
   
   
# #while i < len(t):
#     # print(t[i]):
#     # i+=1
    

# exemplo do ex2 não e eficiente !!2
def cumsum(lista):
    novalista = []
    for indice, elemento in enumerate(lista):
        soma = 0
        for j in range(indice + 1):  # incluindo o índice atual na soma
            soma += lista[j]         # somando elementos da lista original
        novalista.append(soma)       # ad icionando o resultado à novalista
    return novalista

t = [1, 2, 3]
print(cumsum(t))  
