from validate_docbr import CPF, CNPJ

class CpfCnpj:

    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)

        if self.tipo_documento == "cpf":
            if self.cpf_eh_valido(documento):
                self.cpf_cnpj = documento
            else:
                raise ValueError("CPF inválido!")
        elif self.tipo_documento == "cnpj":
            if self.cnpj_eh_valido(documento):
                self.cpf_cnpj = documento
            else:
                raise ValueError("CNPJ inválido!")
        else:
            raise ValueError("Documento inválido!")

    def __str__(self):
        return self.format_document()

    def cpf_eh_valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("CPF deve conter 11 dígitos!")

    def cnpj_eh_valido(self, cnpj):
        if len(cnpj) == 14:
            validador = CNPJ()
            return validador.validate(cnpj)

    def format_document(self):
        if self.tipo_documento == "cpf":
            mascara = CPF()
            # return mascara.mask(self.cpf)
        elif self.tipo_documento == "cnpj":
            mascara = CNPJ()
        return mascara.mask(self.cpf_cnpj)
