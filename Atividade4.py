#Funções sem retorno e sem parametros:
# def soma():
#     print(5+5)
# soma()

#Função sem paramentro e com retorno:
# x = 5
# def mult():
#     return 5*5

# print(x + mult())

#função com parametro e com retorno:
# def media(unidade1, unidade2, unidade3, unidade4):
#     return (unidade1 + unidade2 + unidade3 +unidade4) / 4

# print(media(2,3,4,5))



# def cadastro(nome, sobrenome, idade):

#     return nome, sobrenome, idade


# print(cadastro(str(input("Escreva um nome: ")), str(input("Escreva seu sobrenome: ")), int(input("Digite sua idade: "))))

nome = 'Ilay'
sobrenome = 'Alexandre'
altura = 1.70
peso = 45

def imc(peso, altura):

    return peso/(altura*altura)

def mostrar(nome,sobrenome,imc):

    print(nome,sobrenome,imc)

mostrar(nome,sobrenome,imc(peso,altura))
    
    