from cpf_cnpj import CpfCnpj


cpf = "44452871801"
cnpj = "28945493000151"
doc = CpfCnpj(cnpj, "cnpj")
doc2 = CpfCnpj(cpf, "cpf")
print(doc, doc2)
