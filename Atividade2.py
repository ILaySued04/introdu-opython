numero = int(input("Número do funcionario: "))
horas = int(input("Horas trabalhadas: "))
valor_por_hora = float(input("Valor por hora: "))
salario = horas*valor_por_hora
print (f"Número = {numero}")
print (f"Sálario = R$ {salario:.2f}")