#!/usr/env python3

class VisaoAspirador():
    def __init__(self, mundoAspirador):
        self.posAspirador = mundoAspirador.posAspirador
        self.aposentos = list(mundoAspirador.aposentos)

class MundoAspiradorPo():
    SUJO = True
    LIMPO = False

    MOVER_DIREITA = hash('mover_direita')
    MOVER_ESQUERDA = hash('mover_esquerda')
    ASPIRAR = hash('aspirar')

    def __init__(self):
        self.posAspirador = 0
        self.aposentos = [SUJO, SUJO]

    def isFimJogo(self):
        return not SUJO in self.aposentos 

    def processarJogada(self, jogada):
        if jogada == ASPIRAR:
            self.aposentos[self.posAspirador] = LIMPO
        else:
            jogada += 1 if jogada == MOVER_DIREITA else -1
            jogada = max(0, min(jogada, 1))

    def buildVisaoMundo(self):
        return VisaoAspirador(self)

class JogadorHumano():
    
    _jogadas = {
            'd' : MundoAspiradorPo.MOVER_DIREITA,
            'a' : MundoAspiradorPo.MOVER_ESQUERDA,
            's' : MundoAspiradorPo.ASPIRAR
    }
    
    def __init__(self):
        pass
    
    def render(self, visaoMundo):
        print("[" + "|".join('X' if aposento == SUJO else '0' for aposento in visaoMundo.aposentos) + "]" )

    def escolherJogada(self, visaoMundo):
        self.render(visaoMundo)
        entrada = 'inválida'
        while not entrada in('a', 's', 'd'):
            entrada = input("Escolha sua jogada (a/s/d): ")
        
        return _jogadas[entrada]

def game(mundo):
    while not mundo.isFimJogo():
        jogada = jogador.escolherJogada(mundo.buildVisaoMundo())

        mundo.processarJogada(jogada)