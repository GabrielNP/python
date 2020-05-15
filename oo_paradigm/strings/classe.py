# -*- coding: utf-8 -*-
class ExtratorArgumentosUrl:
    def __init__(self, url):
        if self.url_eh_valida(url):
            self.url = url
        else:
            raise LookupError("URL inválida")


    @staticmethod
    def url_eh_valida(url):

        if url:
            return True
        else:
            return False


    def extrai_argumentos(self):

        busca_moeda_origem = "moedaorigem="
        busca_moeda_destino = "moedadestino="

        indice_inicial_moeda_origem = self.encontra_indice_inicial(busca_moeda_origem)
        indice_final_moeda_origem = self.url.find("&")
        moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]

        if moeda_origem == "moedadestino":
            self.troca_moeda_origem()
            indice_inicial_moeda_origem = self.encontra_indice_inicial(busca_moeda_origem)
            indice_final_moeda_origem = self.url.find("&")
            moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]

        indice_inicial_moeda_destino = self.encontra_indice_inicial(busca_moeda_destino)
        moeda_destino = self.url[indice_inicial_moeda_destino:]

        return moeda_origem, moeda_destino


    def encontra_indice_inicial(self, moeda_buscada):

        return self.url.find(moeda_buscada) + len(moeda_buscada)


    def troca_moeda_origem(self):
        self.url = self.url.replace("moedadestino","real",1)


    def retornaValor(self):

        buscaValor = "Valor".lower()
        inicioSubstringValor = self.encontraIndiceInicioSubstring(buscaValor)
        valor = self.url[inicioSubstringValor:]

        return valor