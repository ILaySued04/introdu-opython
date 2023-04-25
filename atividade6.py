#Faça uma função que recebe por parâmetro o raio de uma esfera e calcula o seu volume (v = 4/3.P .R3).
# r = float(input("digite um numero: "))
# p = 3.14
# def parametro(r, p):
#      return 3*p*(r**3)/4
# print(parametro(r, p))

#Faça uma função que recebe a idade de uma pessoa em anos, meses e dias e retorna essa idade expressa em dias.

#tentativa 1
# print("Imforme dua idade em: ")
# def idade_anos(a):
#    return a*365
# print(idade_anos(a=int(input("Anos: "))))

# def idade_meses(m):
#    return m*30
# print(idade_meses(m=int(input("Meses: "))))

# def idade_dias(d):
#    return d*1
# print(idade_dias(d=int(input("Dias: "))))

# def calcular(idade_anos(a)):

#tentativa 2

# def calcular(a,m,d):
#     anos = a*365
#     meses = m*30
#     dias = d*1
#     return anos+meses+dias
# print(calcular(19,5,145))

#Faça uma função que recebe por parâmetro um valor inteiro e positivo e retorna o valor lógico Verdadeiro caso o valor seja primo e Falso em caso contrário.


#Faça uma função que recebe por parâmetro o tempo de duração de uma fábrica expressa em segundos e retorna também por parâmetro esse tempo em horas, minutos e segundos.
# tempo_segundos = int(input("digite o tempo em segundos: "))

#Faça uma função que recebe um valor inteiro e verifica se o valor é positivo ou negativo. A função deve retornar um valor booleano.
# entrada = int(input('Digite: '))

# def valor(n):
#     if n>0 :
#         return True
#     else:
#         return False
    
# print(valor(entrada))


#Faça um procedimento que recebe, por parâmetro, um valor N e calcula e escreve a tabuada de 1 até N. Mostre a tabuada na forma.

n = int(input("digite um numero: "))
def tabuada(n):
    
    c = 1
    while (c <= 10):
        v = n*c
        print(f"{n}*{c}={v}")
        c = c+1
tabuada(n)
