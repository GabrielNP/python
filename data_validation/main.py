#  Validação de CPF e CNPJ
from cpf_cnpj import Documento


cpf = "44452871801"
cnpj = "28945493000151"
doc = Documento.cria_documento(cnpj)
doc2 = Documento.cria_documento(cpf)
print(doc, doc2)


# Validação de Telefone
from telefones_br import TelefonesBr


numero = "5511972218872"
objeto = TelefonesBr(numero)
print(objeto)


# Validação de Datas
from datas_br import DatasBr

datas_br = DatasBr()
print("Objeto da classe DatasBr:", datas_br)
dia_da_semana = datas_br.dia_da_semana
print("Dia da semana:", dia_da_semana)
mes = datas_br.mes
print("Mês:", mes)
tempo_cadastro = datas_br.tempo_cadastro()
print(tempo_cadastro)


# Validação de CEP
from acesso_cep import BuscaEndereco

cep = "02402010"
objeto_cep = BuscaEndereco(cep)
print("CEP:", objeto_cep)
bairro, localidade, uf = objeto_cep.acessa_via_cep()
print(bairro, localidade, uf)
