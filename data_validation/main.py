from cpf_cnpj import Documento


cpf = "44452871801"
cnpj = "28945493000151"
doc = Documento.cria_documento(cnpj)
doc2 = Documento.cria_documento(cpf)
print(doc, doc2)
