# Brincando com coleções / Revisão

from collections import Counter


def analisa_frequencia_de_letras(texto):

    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print(f"{caractere} => {proporcao * 100 :.2f}%")

texto_1 = """
A SpaceX foi colocada numa sinuca de bico pela FCC (Federal Communications Commission), a agência de comunicações dos Estados Unidos equivalente à Anatel: a comissão acredita que a rede de satélites Starlink, lançada pela empresa e que promete fornecer internet do espaço aos consumidores, não é capaz de operar com baixa latência como diz ser.

SpaceX quer começar a prover internet do espaço já em 2020
SpaceX lança primeiros satélites do projeto Starlink
Dessa forma, a companhia de Elon Musk tem 30 dias para provar que o Starlink funciona, sob risco de perder a preferência em uma licitação que planeja distribuir até US$ 16 bilhões para empresas de comunicações, de modo a levar internet para o interior do país.

SpaceX / satélite da Starlink com painel solar

De acordo com uma notificação (cuidado, PDF) publicada pela FCC na última quinta-feira (12), a Starlink e outras provedoras de internet que operam com satélites de órbita baixa (em torno de 570 km de altitude, contra 35.786 km de uma órbita geoestacionária) foram colocadas no paredão, ao serem questionadas por uma possível incapacidade de fornecer uma conexão de dados a uma baixa latência, inferior a 100 ms.

Essa latência alta é o equivalente a uma conexão de dados fornecida por um satélite tradicional geoestacionário, a agência acredita que a altitude não influi em nada para reduzir o ping e dessa forma, o Starlink seria uma opção pior às companhias que oferecem internet via cabo ou fibra ótica, as preferenciais nos planos de expansão da banda larga nos EUA .

Originalmente o plano de expansão iria excluir a SpaceX e outras companhias de internet via satélites de órbita baixa completamente, mas este foi derrubado pelo diretor da FCC Ajit Pai. No entanto, conforme o documento agora explica, as empresas terão que provar sua capacidade de entregar uma conexão espacial decente. O prazo é de 30 dias, e caso não consigam se adequar, estarão fora da licitação.

A FCC defende que fatores como "roteamento, processamento e tráfego no transporte de informações" são fatores que influenciam na latência, que não seriam influenciados pela altitude dos satélites, se de órbita baixa ou geoestacionários. Elon Musk, por sua vez já argumentou anteriormente que a meta da Starlink é fornecer uma conexão similar à da internet cabeada, com latência por em torno de 20 ms. Isso permitiria até mesmo jogar online.
"""

analisa_frequencia_de_letras(texto_1)
