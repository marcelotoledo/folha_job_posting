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

COGU   = ({ 'cometa': 'halley',  'grupo': 'amarelo'  },
          { 'cometa': 'encke',   'grupo': 'vermelho' },
          { 'cometa': 'wolf',    'grupo': 'preto'    },
          { 'cometa': 'kushida', 'grupo': 'azul'     })

DEPARA = { 'a':  1, 'b':  2, 'c':  3, 'd':  4, 'e':  5, 'f':  6, 
           'g':  7, 'h':  8, 'i':  9, 'j': 10, 'k': 11, 'l': 12, 
           'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 
           's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 
           'y': 25, 'z': 26 }

def translate_char(char):
    return DEPARA[char]

def translate(str):
    return reduce((lambda x, y: x * y), map(translate_char, list(str)))

for i in COGU:
    print('Cometa: %15s     -> %15d'   % (i['cometa'],            translate(i['cometa'])))
    print('Grupo:  %15s     -> %15d'   % (i['grupo'],             translate(i['grupo'])))
    print('Cometa: %15d / 45 = %15d'   % (translate(i['cometa']), translate(i['cometa']) % 45))
    print('Grupo:  %15d / 45 = %15d\n' % (translate(i['grupo']),  translate(i['grupo']) % 45))
