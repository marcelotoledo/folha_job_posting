#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Source: http://hotsites.folha.com.br/2015/03/31/selecao/
#
# Sabe-se que por trás de cada cometa há um OVNI. Esses OVNIs
# frequentemente buscam bons desenvolvedores aqui na Terra.
# Infelizmente só têm espaço para levar um grupo de devs por vez. Para
# a seleção, há um engenhoso esquema, da associação do nome do cometa
# ao nome do grupo, que possibilita a cada grupo saber se será levado
# ou não.

# Os dois nomes, do grupo e do cometa, são convertidos em um número
# que representa o produto das letras do nome, onde "A" é 1 e "Z" é
# 26. Assim, o grupo "LARANJA" seria 12 * 1* 18 * 1 * 14 * 10 * 1 =
# 30240. Se o resto da divisão do número do grupo por 45 for igual ao
# resto da divisão do número do cometa por 45, então o grupo será
# levado.

# Para os cometas e grupos abaixo, qual grupo NÃO será levado?

# [COMETA]  [GRUPO]
#  HALLEY    AMARELO
#  ENCKE     VERMELHO
#  WOLF      PRETO
#  KUSHIDA   AZUL

import string

def translate(str):
    return reduce((lambda x, y: x * y), map((lambda char: string.ascii_lowercase.index(char) + 1), list(str)))

for cometa, grupo in [('halley','amarelo'), ('encke','vermelho'), ('wolf','preto'), ('kushida','azul')]:
    print('Cometa %10s (%10d / 45 = %d) \tGrupo: %10s (%10d / 45 = %d)' % (cometa, translate(cometa), translate(cometa) % 45, grupo, translate(grupo), translate(grupo) % 45))
