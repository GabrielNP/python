from conta import cria_conta, deposita, saca, extrato

conta = cria_conta(123, "Fulano", 500, 1000)
print("Dados da conta: {}".format(conta))

deposita(conta, 300)
print("\nDepositando 300")

extrato(conta)

saca(conta, 400)
print("\nRetirando 400")

extrato(conta)