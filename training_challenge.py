saldo = 0
limite_saques = 3
saques_feitos = 0

def criaConta():
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    cpf = input("Digite seu CPF: ")
    max_cpf_length = 15
    if len(cpf) > max_cpf_length:
        return "CPF inválido."
    else:
        return f"{nome}, {idade}, {cpf}"

def depositaValor(saldo):
    deposito = float(input("Qual a quantia que deseja depositar? R$ "))
    saldo += deposito
    print(f"Foi feito um depósito de {deposito} Reais")
    print(f"Saldo atual: {saldo}")
    return saldo

def extratoBancario(saldo):
    print(f"Seu saldo é {saldo}")

def sacaValor(saldo):
    global limite_saques, saques_feitos
    if saques_feitos < limite_saques:
        valor = float(input("Qual valor deseja sacar? R$ "))
        if 0 < valor <= saldo and saques_feitos < limite_saques:
            saldo -= valor
            saques_feitos += 1
            print(f"Foi efetuado o saque de um valor de: R${valor}")
            print(f"Saldo atual: {saldo}")
        else:
            print("Valor para saque indisponível ou limite de saques atingido.")
    else:
        print("Limite de saques atingido.")

# Loop para exibir o menu e interação com o usuário
while True:
    print("""
    Escolha uma das operações:

    [1] - Criar conta
    [2] - Depositar
    [3] - Sacar
    [4] - Extrato
    [5] - Sair
    """)
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        dados_conta = criaConta()
    elif opcao == '2':
        saldo = depositaValor(saldo)
    elif opcao == '3':
        sacaValor(saldo)
    elif opcao == '4':
        extratoBancario(saldo)
    elif opcao == '5':
        print("Saindo...")
        # Salvando os dados no arquivo ao sair do programa
        with open('dados_bancarios.txt', 'a') as file:
            if 'dados_conta' in locals():
                file.write(f"Dados da conta: {dados_conta}\n")
            file.write(f"Saldo final: {saldo}\n")
        break
    else:
        print("Opção inválida. Escolha uma opção válida.")
