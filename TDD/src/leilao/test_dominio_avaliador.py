from unittest import TestCase
from TDD.src.leilao.dominio import Usuario, Lance, Leilao, Avaliador



class TestAvaliador(TestCase):

    def cria_cenario(self):
        self.gui = Usuario('Gui')
        self.yuri = Usuario('Yuri')
        self.lance_do_gui = Lance(self.gui, 100.0)
        self.lance_do_yuri = Lance(self.yuri, 150.0)
        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_menor_e_o_maior_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        self.cria_cenario()

        self.leilao.lances.append(self.lance_do_gui)
        self.leilao.lances.append(self.lance_do_yuri)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

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

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        gui = Usuario('Gui')

        lance = Lance(gui, 150.0)

        leilao = Leilao('Celular')
        leilao.lances.append(lance)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        self.assertEqual(150.0, avaliador.maior_lance)
        self.assertEqual(150.0, avaliador.menor_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_3_lances(self):
        gui = Usuario('Gui')
        yuri = Usuario('Yuri')
        vini = Usuario('Vini')

        lance_do_gui = Lance(gui, 200.0)
        lance_do_yuri = Lance(yuri, 150.0)
        lance_do_vini = Lance(vini, 100.0)

        leilao = Leilao('Celular')

        leilao.lances.append(lance_do_gui)
        leilao.lances.append(lance_do_yuri)
        leilao.lances.append(lance_do_vini)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)