menu = """

Escolha uma das operações

[1] = depositar
[2] = sacar
[3] = extrato
[4] = sair1

"""
saldo_inicial = 0
saldo = 0
limite = 500
LIMITE_SAQUE = 3
numero_de_saques = 0
valor_saque = 0

while True:
    escolha = input(menu)

    if escolha == '1':
        print("Você escolheu depositar")
        deposito = float(input("Insira um valor para depositar: "))
        saldo += deposito
        print(f"Seu saldo: R$ {saldo}")
        saldo_inicial = saldo

    elif escolha == "2":
        if numero_de_saques < LIMITE_SAQUE:
            valor_saque = float(input("Digite um valor para sacar: "))
            if saldo >= valor_saque <= limite:
                saldo -= valor_saque
                numero_de_saques += 1
                print(f"Você escolheu sacar R$ {valor_saque}. Novo saldo: R$ {saldo}")
                saldo_inicial = saldo
            else:
                print("Saldo insuficiente ou valor de saque excede o limite permitido.")
        else:
            print("Limite de saques atingido.")

    elif escolha == "3":
        if saldo > 0 or valor_saque > 0:
            print("Você escolheu olhar extrato")
            print(f"Seu saldo anterior era de: R${saldo_inicial}")
            print(f"Seu novo saldo é de: R${saldo}")
            print(f"Seu saque foi de: R${valor_saque}")
        else:
            print("Seu saldo está em branco")

    elif escolha == "4":
        print("Saindo")
        break

    else:
        print("Operação inválida")

