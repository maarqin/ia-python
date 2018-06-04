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
        self.aposentos = [MundoAspiradorPo.SUJO, MundoAspiradorPo.SUJO]

    def isFimJogo(self):
        return not MundoAspiradorPo.SUJO in self.aposentos 

    def processarJogada(self, jogada):
        if jogada == MundoAspiradorPo.ASPIRAR:
            self.aposentos[self.posAspirador] = MundoAspiradorPo.LIMPO
        else:
            self.posAspirador += 1 if jogada == MundoAspiradorPo.MOVER_DIREITA else -1
            self.posAspirador = max(0, min(self.posAspirador, 1))

    def buildVisaoMundo(self):
        return VisaoAspirador(self)

class JogadorHumano():
    
    _jogadas = {
            'd' : MundoAspiradorPo.MOVER_DIREITA,
            'a' : MundoAspiradorPo.MOVER_ESQUERDA,
            's' : MundoAspiradorPo.ASPIRAR }
    
    def __init__(self):
        pass
    
    def render(self, visaoMundo):
        print("[{}]:{}".format( "|".join('X' if aposento == MundoAspiradorPo.SUJO else '0' 
        for aposento in visaoMundo.aposentos), 
        visaoMundo.posAspirador))

    def escolherJogada(self, visaoMundo):
        self.render(visaoMundo)
        entrada = 'inválida'
        while not entrada in('a', 's', 'd'):
            entrada = input("Escolha sua jogada (a/s/d): ")
        
        return JogadorHumano._jogadas[entrada]

def game(mundo):
    while not mundo.isFimJogo():
        jogada = jogador.escolherJogada(mundo.buildVisaoMundo())

        mundo.processarJogada(jogada)