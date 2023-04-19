# n = 5
# b = 0
# while b<=5 :
#     print(b)
#     b=b+1
# a = 0
# while True:
#     print("Olá")
#     a = a+1
#     if a==10:
#         break
# cidades = ['Mata de são João', 'Catu', 'Pojuca', 'Camaçari', 'Salvador']
# for cidade in cidades:
#     print(cidade)


# for n in range (11):
#     print(f'{5} x {n} = {5*n}')

# #Tabuada de 5
# nu = 5
# c = 1
# while (c <= 10):
#     v = nu*c
#     print(f"{nu}*{c}={v}")
#     c = c+1

# lista = [1,2,3]
# print("A soma do elementos é: ", sum(lista))

# lista = ['a','b','d']
# lista.insert(2,'c')
# print(lista)

# lista = [3, 6, 4]
# lista.remove(3)
# print( "maior valor", max(lista))

#lista ordenada
# f = ['laranja', 'pera', 'amora' ]
# f.sort()
# print(f)
# sorted(f)

#Adiciona um item a lista
# l = [1, 2, 3, 4, 5]
# l.append(6)
# print(l)

# # Mescla uma lista na outra
# l = [1, 2, 3, 4, 5]
# a = ['gato', 'passaro', 'peixe']
# l.extend(a)
# print(l)

soma = [1,2] + [3]
print(soma)
soma += (5,)
print(soma)

#Identificação e contagem de elementos de tuplas.
# exemplo = (9, 6, 0, 7, 8, 8, 2, 4) 
# # Retorna a posição da primeira ocorrência do elemento a na tupla
# print( 'O primeiro elemento a esta na posição:', exemplo.index(8) ) 
# # Retorna a quantidade do elemento a na tupla
# print( 'O quantidade do elemento a é:', exemplo.count(8) ) 