#Criar um programa que calcule a média 
nome = str(input("Digite o nome do aluno: "))
u1 = float(input("Digite a nota da I unidade: "))
u2 = float(input("Digite a nota da II unidade: "))
u3 = float(input("Digite a nota da III unidade: "))
u4 = float(input("Digite a nota da VI unidade: "))
media = (u1+u2+u3+u4)/4
if media > 7:      
    print("aluno aprovado")
elif (media < 7) and (media > 5): 
    print("Aluno em recuperaçaõ")
else :
    print("aluno reprovado")
