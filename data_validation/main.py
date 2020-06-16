#  Validação de CPF e CNPJ
from cpf_cnpj import Documento

cpf = "44452871801"
cnpj = "28945493000151"
doc = Documento.cria_documento(cnpj)
doc2 = Documento.cria_documento(cpf)
print(doc, doc2)


# Validação de Telefone
from telefones_br import Telefones_br


numero = "5511972218872"
objeto = Telefones_br(numero)
print(objeto)



