from dominio import Usuario, Leilao, Lance, Avaliador

gui = Usuario('Gui')
yuri = Usuario('Yuri')
print(f'Gui: {gui}')
print(f'Yuri: {yuri}')

lance_do_gui = Lance(gui, 100.0)
lance_do_yuri = Lance(yuri, 150.0)
print(f'Lance do Gui {lance_do_gui}')
print(f'Lance do Yuri {lance_do_yuri}')

leilao = Leilao('Celular')
print(f'Leilão: {leilao}')

leilao.lances.append(lance_do_gui)
leilao.lances.append(lance_do_yuri)
print(f'Leilão após append:{leilao}')

for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} deu um lance de {lance.valor}')

avaliador = Avaliador()
print(f'Avaliador {avaliador}')
avaliador.avalia(leilao)
print(f'Avaliador {avaliador}')
print(f'O menor lance foi de {avaliador.menor_lance} e o maior foi de {avaliador.maior_lance}')

