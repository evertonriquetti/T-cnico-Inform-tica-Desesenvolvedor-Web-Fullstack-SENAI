print('Digite seu nome: ')
nome = input()
print('Digite sua data de nascimento com as barras: ')
dataNascimento = input()
print('Digite sua idade: ')
idade = int(input())
print('Digite o número de seu telefone: ')
telefone = input()
print('Digite o número do seu CPF com números e hífen: ')
cpf = input()
print('Digite o número do seu RG com números e hífen: ')
rg = input()
print('Digite seu endereço: ')
endereco = input()
print('Digite seu E-mail: ')
email = input()
print('Digite seu sexo: ')
sexo = input()
print('Digite o seu salário: ')
salario = float(input())
imposto = salario*0.15
print('Você está empregado? (sim/não): ')
apoio = input()
ativo = (apoio =="sim")
print("Olá "+ nome +", bem vindo ao Sistema de Cálculo de Imposto de Renda!")
print("Nascido em: " + dataNascimento + " , sua idade é " + str(idade))
print("Portador do CPF: " + cpf + " e portador do RG: " + rg)
print("Você tem: ")
if not ativo:
    print("Emprego inativo. ")
else:
    print("Emprego ativo. ")
print("Seu salário é " + str(salario) + " e o imposto é " + str(imposto))
    
    

