from datetime import datetime


class DatasBr:

    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.formata_data()

    def formata_data(self):
        return self.momento_cadastro.strftime('%d/%m/%Y %H:%M')

    @property
    def mes(self):
        return self.momento_cadastro.strftime('%B')

    @property
    def dia_da_semana(self):
        return self.momento_cadastro.strftime('%A')


