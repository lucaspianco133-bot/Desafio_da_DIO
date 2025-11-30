def saque(saldo, valor, limite, numero_saques, LIMITE_SAQUES, extrato):
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")
        
        return saldo, extrato, numero_saques 


def deposito(saldo, valor, extrato):
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")
        return saldo, extrato

def exibir_extrato(saldo, extrato):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        return saldo, extrato

def criar_usuario(lista, nome, cpf, data_nascimento, endereco): 
    for usuario in lista:
        if usuario["cpf"] == cpf: 
            print("Já existe um usuário com esse CPF!") 
            print("Crie outro usuário!")
        return lista
    else:
     usuario = {
          "nome": nome,
            "cpf": cpf,
            "data_nascimento": data_nascimento,
            "endereco": endereco
     }
    lista.append(usuario)
    return lista 

def criar_conta_corrente(agencia, numero_da_conta, usuario, lista): 

    for usuario in lista:
        if usuario["cpf"] == cpf: 
           conta_corrente = {
        "agencia": agencia,
        "numero_da_conta": numero_da_conta,
        "usuario": usuario
     }
           print("Conta criada com sucesso!")
           return conta_corrente
    else:
        print("Usuário não encontrado, por favor crie um usuário antes de criar uma conta corrente.")
        return None
    
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[c] Criar usuário
[cr] Criar conta corrente

=> """

AGENCIA = "0001"
saldo = 1000 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
lista_de_usuarios = []

while True:

    opcao = input(menu)

    if opcao == "d" or opcao == "D":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(saldo, valor, extrato)

    elif opcao == "s" or opcao == "S":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = saque(saldo=saldo, limite=limite, valor=valor, LIMITE_SAQUES= LIMITE_SAQUES, numero_saques=numero_saques, extrato=extrato)
 
    elif opcao == "e" or opcao == "E":
       saldo , extrato = exibir_extrato(saldo, extrato=extrato)

    elif opcao == "c" or opcao == "C":
        nome = input("Informe o nome completo: ")
        cpf = input("Informe o CPF (somente números): ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, número - bairro - cidade/sigla estado - CEP): ")
        lista_de_usuarios = criar_usuario(lista_de_usuarios, nome, cpf, data_nascimento, endereco)
       
    elif opcao == "cr" or opcao == "CR":
        cpf = input("Informe o CPF do usuário: ")
        numero_da_conta = len(lista_de_usuarios) + 1 
        conta = criar_conta_corrente(AGENCIA, numero_da_conta, cpf, lista_de_usuarios)

    elif opcao == "q" or opcao == "Q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")