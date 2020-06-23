from unittest import TestCase
from TDD.src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):

    def test_deve_retornar_o_menor_e_o_maior_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        gui = Usuario('Gui')
        yuri = Usuario('Yuri')

        lance_do_gui = Lance(gui, 100.0)
        lance_do_yuri = Lance(yuri, 150.0)

        leilao = Leilao('Celular')

        leilao.lances.append(lance_do_gui)
        leilao.lances.append(lance_do_yuri)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_o_menor_e_o_maior_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):
        gui = Usuario('Gui')
        yuri = Usuario('Yuri')

        lance_do_gui = Lance(gui, 500.0)
        lance_do_yuri = Lance(yuri, 150.0)

        leilao = Leilao('Celular')

        leilao.lances.append(lance_do_gui)
        leilao.lances.append(lance_do_yuri)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 150.0
        maior_valor_esperado = 500.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
