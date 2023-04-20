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

# soma = [1,2] + [3]
# print(soma)
# soma += (5,)
# print(soma)

#Identificação e contagem de elementos de tuplas.
# exemplo = (9, 6, 0, 7, 8, 8, 2, 4) 
# # Retorna a posição da primeira ocorrência do elemento a na tupla
# print( 'O primeiro elemento a esta na posição:', exemplo.index(8) ) 
# # Retorna a quantidade do elemento a na tupla
# print( 'O quantidade do elemento a é:', exemplo.count(8) ) 

# Cria o dicionário
# dic = { 'a' : 1, 'b' : 2, 'c' : 3 } 
# # Imprime a quantidade de elementos do dicionário
# print( 'Tamanho do dicionário:', len(dic), 'elemento(s)' ) 
# # Deleta o elementos do dicionário chave b
# del(dic['b']) 
# # Imprime o novo dicionario
# print( 'Novo dicionário', dic )
# Cria o dicionário

# dic = [1, 2, 3, 4, 5]
# print(dic[3])
# dic = {'nome':'ILay'}
# print(dic['nome'])

# colecao = {'ilay', 1, 1,6}
# print(colecao)
# print(type())

#listas
# frutas = ['pera','uva','maça']
# print(type(frutas))
# print(frutas[0])

# #Tuplas
# numeros = (1, 2, 3)
# print(type(numeros))
# print(numeros[0])

# #Dicionario
# dicionario = {"nome":"Ilay", "objeto":"caneta", "numero":1}
# print(type (dicionario))
# print(dicionario["nome"])

# #colecao
# colecao = {"garrafa","teclado","pc"}
# print(type(colecao))]

# Tabuada de 5
# nu = 5
# c = 1
# while (c <= 10):
#      v = nu*c
#      print(f"{nu}*{c}={v}")
#      c = c+1

# for n in range (11):
#     print(f'{5} x {n} = {5*n}')

#atividade utilizando while e listas
# listas = []
# while True:

#     nome = str(input("Digite o nome do aluno: "))
#     unidade_1 = float(input("Digite a nota da unidade 1: "))
#     unidade_2 = float(input("Digite a nota da unidade 2: "))
#     unidade_3 = float(input("Digite a nota da unidade 3: "))
#     unidade_4 = float(input("Digite a nota da unidade 4: "))
    
#     media = (unidade_1 + unidade_2 + unidade_3 + unidade_4) / 4

#     listas.append(f"O aluno(a) {nome} possui a média {media}")
    
#     x = str(input("Deseja contunuar? S-sim ou N-não: "))
    
#     if x == "N":
#         break
#     else:
#         print("Digite apenas S ou N")
    
# for lista in listas:
#     print(lista)

