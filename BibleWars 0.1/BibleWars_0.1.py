import math
import random
import numpy as np

def d6():
    return random.randint(1, 6)
def d12():
    return random.randint(1, 12)

Poss = []
class table:
    def __init__(self):
        cleanline = 16*'[ ]'
        woods = 2*'[#]' + 12*'[ ]' + 2*'[#]'
        river = 2*'[ ]' + 12*'[*]' + 2*'[ ]'
        self.l1, self.l2, self.l7, self.l8 = cleanline, cleanline, cleanline, cleanline
        self.l9, self.l10, self.l15, self.l16 = cleanline, cleanline, cleanline, cleanline
        self.l3, self.l4, self.l13, self.l14 = woods, woods, woods, woods
        self.l5, self.l6, self.l11, self.l12 = river, river, river, river
        self.lines = [self.l1, self.l2, self.l3, self.l4,
                 self.l5, self.l6, self.l7, self.l8,
                 self.l9, self.l10, self.l11, self.l12,
                 self.l13, self.l14, self.l15, self.l16]

    def show(self):
        for line in self.lines:
            print(line)

    def change(self, pers):
        for p in Ps:
            if p.nome == pers.nome:
                x = p.x
                y = p.y
                lista = self.lines[y-1][:3*x-2]
                listb = self.lines[y-1][3*x -2:]
                listc = [lista, listb]
                lista = p.token.join(listc)
                self.lines[y-1] = lista

        self.show()

Mesa = table()

Ps = []
Psn = []
class Pers:
    def __init__(self, nome, pv, fé, ataque, defesa):
        self.nome = nome
        self.pv = pv
        self.fé = fé
        self.ataque = ataque
        self.defesa = defesa
        self.vel = 0
        self.pontos = 0
        self.kills = 0
        self.x = random.randint(1, 16)
        self.y = random.randint(1, 16)
        self.pos = [self.x, self.y]
        self.Itens = []
        self.Itensn = []
        self.Milagres = []
        self.Milagresn = []
        Ps.append(self)
        Psn.append(self.nome)
        Poss.append(self.pos)
        self.token = self.nome[0]
        
    def novo(self):
        poss = [A, I, E, M]


    def atacar(self, pers):
        d12 = random.randint(1,12)
        atq = self.ataque + d12
        d12 = random.randint(1,12)
        dff = pers.defesa + d12
        dif = atq - dff
        if dif > 0:
            print('Ataque bem sucedido! + ', dif)

            self.pontos += dif
            pers.pv -= dif
        elif dif == 0:
            print('Ataque bloqueado!')
        else:
            print('Defesa bem sucedida! -', abs(dif))
            self.pv += dif
            pers.pontos -= dif
        print(self.nome, 'pv: ', self.pv)
        print(pers.nome, 'pv: ', pers.pv)
        if pers.pv <= 0:
            print(pers.nome ,' EXECUTADO!')
            self.pontos += 10
            self.kills += 1

    def move(self, h, v):
        Poss.pop(Poss.index(self.pos))
        self.x += h
        self.y += v
        self.pos = [self.x, self.y]
        Poss.append(self.pos)
        Mesa.change(self)

    def usar(self, item):
        item.func(self.ataque, self.defesa)
    def convocar(self, Exerc):
        Exerc.inv(self.x, self.y)
    def mil(self, milagre):
        milagre.func()
    def mao(self):
        print('Itens: ', self.Itensn,'\nMilagres: ', self.Milagres)
    def carta(self):
        print(self.nome, '\n PV: ', self.pv, '\n Fé: ', self.fé, '\n Ataque: ',
              self.ataque, '\n Defesa: ', self.defesa)

Elias = Pers('Elias', 20, 10, 7, 6)
Davi = Pers('Davi', 14, 8, 9, 7)
Jesus = Pers('Jesus', 20, 10, 5, 10)
Moisés = Pers('Moisés', 18, 10, 6, 8)

Is = []
Isn = []
class Item:
    def __init__(self, nome, modpv, modfe, modmove):
        self.nome = nome
        self.modpv = modpv
        self.modfe = modfe
        self.modmove = modmove
        Is.append(self)
        Isn.append(self.nome)
    def usar(self, pv, fe):
        pv += self.modpv
        fe += self.modfe

    class Arma:
        def __init__(self, nome, modatk, moddef, alc = 1):
            self.nome = nome
            self.modatk = modatk
            self.moddef = moddef
            self.alc = alc
            Isn.append(self.nome)
            Is.append(self)
        def usar(self, ataque, defesa):
            if distance <= alc:
                ataque += self.modatk
                defesa += self.moddef
            else:
                print('Fora de alcance!')

    class Exerc:
        def __init__(self, nome, pv, ataque, defesa):
            self.nome = nome
            self.hp = pv
            self.ataque = ataque
            self.defesa = defesa
            Isn.append(self.nome)
            Is.append(self)
        def usar(self, x, y):
            self.x = x
            self.y = y

Agua = Item('Água', 3, 0, 0)
Comida = Item('Comida', 4, 0, 0)
Camelo = Item('Camelo', 0, 0, 5)
Barco = Item('Barco', 0, 0, 7)
Soldado = Item.Exerc('Soldado', 2, 1, 1)
Turba = Item.Exerc('Turba', 4, 2, 2)
Destacamento = Item.Exerc('Destacamento', 6, 3, 3)
Exército = Item.Exerc('Exército', 8, 4, 4)
EspadaI = Item.Arma('Espada Israelita', 2, 0)
EscudoP = Item.Arma('Escudo pequeno', 0, 2)
ArcoeFlecha = Item.Arma('Arco e flecha', 4, 0)
ArmaduraR = Item.Arma('Armadura Romana', 0, 6)

Ms = []
Msn = []
class Milagre:
    def __init__(self):
        self.nome = nome
        self.pf = pf
    class Diluvio:
        def __init__(self):
            self.nome = 'Dilúvio'
            self.pf = 20
            Ms.append(self)
            Msn.append(self.nome)
        def help(self):
            print('Causa um dilúvio destruidor em todo o campo de jogo! Quem não tiver proteção apropriada\nperecerá!',
                  ' Apenas possuidores de barcos ou da Arca sobreviverão.')
        def milagre(self, j1):
            for jog in Jogs:
                if Barco not in jog.Itens and Arca not in jog.Itens and jog.nome != j1.nome:
                    dano = random.randint(1, 8)
                    jog.pv -= dano
    class ChuvadeFogo:
        def __init__(self):
            self.nome = 'Chuva de Fogo'
            self.pf = 21
            print()
            Ms.append(self)
            Msn.append(self.nome)
        def help(self):
            print('Chuva de fogo caindo aleatoreamente sobre o campo. Você pode ter pouco dano... se tiver sorte.')
        def milagre(self, j1):
            for jog in Jogs:
                if Arca not in jog.Itens and jog.nome != j1.nome:
                    dano = random.randint(1, 6)
                    jog.pv -= dano
    class AnjodaMorte:
        def __init__(self):
            self.nome = 'Anjo da Morte'
            self.pf = 22
            Ms.append(self)
            Msn.append(self.nome)
        def help(self):
            print('Alguém vai morrer e não tem nada que você possa fazer! Mwahahahahahahahah!')
        def milagre(self, j1, j2):
            j2.pv = 0
    class Pragas:
        def __init__(self):
            self.nome = 'Pragas'
            self.pf = 19
            Ms.append(self)
            Msn.append(self.nome)
        def help(self):
            print('Um monte de coisa pode acontecer com qualquer um, desde sapos até perder 7 pontos de pv!')
        def milagre(self, j1):
            for jog in Jogs:
                if Arca not in jog.Itens and jog.nome != j1.nome:
                    dano = random.randint(1, 7)
                    jog.pv -= dano
                 


def jogo():
    while len(Jogs) > 1:
        Mortos = []
        Mortosn = []
        for Jog in Jogs:
            if Jog.pv <= 0:
                Jog.pv = 0
                Mortos.append(Jog)
                Mortosn.append(Jog.nome)
                i = Jogs.index(Jog)
                Jogs.pop(i)
                Jogns.pop(i)
        for Jog in Jogs:
            print('Turno de ', Jog.nome)
            GM0 = int(input('Você deseja: \n 1 - Nova carta \n 2 - Ver mão \n 3 - Ação \n 4 - Desistir'))
            while GM0 < 1 or GM0 > 4:
                GM0 = int(input('Você deseja: \n 1 - Nova carta \n 2 - Ver mão \n 3 - Ação \n 4 - Desistir'))
            if GM0 == 1:
                tipo = DeckType[random.randint(0,10)]
                if tipo == 'M':
                    mil = Ms[random.randint(0, len(Ms) - 1)]
                    Jog.Milagres.append(mil)
                    Jog.Milagresn.append(mil.nome)
                    print('NOVO MILAGRE: ', mil.nome)
                else:
                    carta = Is[random.randint(0,len(Is)-1)]
                    Jog.Itens.append(carta)
                    Jog.Itensn.append(carta.nome)
                    print('NOVO ITEM: ', carta.nome)

            elif GM0 == 2:
                    Jog.mao()

            elif GM0 == 3:
                GM = int(input('Qual a sua ação?\n 1 - Mover\n 2 - Atacar\n 3- Usar Item\n 4 - Tentar Milagre'))
                while GM < 1 or GM > 4:
                    GM = int(input('Qual a sua ação?\n 1 - Mover\n 2 - Atacar\n 3- Usar Item\n 4 - Tentar Milagre'))
                if GM == 1:
                    dado = d6()
                    print('D6 = ', dado)
                    print('Modificador de velocidade: ', Jog.vel)
                    print('Total: ', dado + Jog.vel)
                    GM2 = int(input('Insira como quer se mover horizontalmente em unidades, "-" é pra esquerda.'))
                    resto = dado + Jog.vel - abs(GM2)
                    while GM2 > dado:
                        print('Você só pode se mover ', dado, ' unidades.')
                        GM2 = int(input('Insira como quer se mover horizontalmente em unidades, "-" é pra esquerda.'))
                        resto = dado + Jog.vel - abs(GM2)
                    GM3 = int(input('Insira como quer se mover verticalmente em unidades, "-" é pra baixo.'))
                    while GM3 > resto:
                        print('Agora você só pode se mover ', resto, ' unidades.')
                        GM3 = int(input('Insira como quer se mover verticalmente em unidades, "-" é pra baixo.'))
                    while [Jog.x + GM2, Jog.y + GM3] in Poss:
                        print('Você não pode se mover para este lugar!')
                        GM2 = int(input('Insira como quer se mover horizontalmente em unidades, "-" é pra esquerda.'))
                        resto = dado + Jog.vel - abs(GM2)
                        while GM2 > dado:
                            print('Você só pode se mover ', dado, ' unidades.')
                            GM2 = int(input('Insira como quer se mover horizontalmente em unidades, "-" é pra esquerda.'))
                            resto = dado + Jog.vel - abs(GM2)
                        GM3 = int(input('Insira como quer se mover verticalmente em unidades, "-" é pra baixo.'))
                        while GM3 > resto:
                            print('Agora você só pode se mover ', resto, ' unidades.')
                            GM3 = int(input('Insira como quer se mover verticalmente em unidades, "-" é pra baixo.'))
                        Jog.move(GM2, GM3)
                        Mesa.show()
                elif GM == 2:
                    GM2 = input('Quem você quer atacar?')
                    while GM2 not in Jogsn:
                        GM2 = input('Quem você quer atacar?')
                    for jog in Jogs:
                        if jog.nome == GM2:
                            Jog.atacar(jog)
                elif GM == 3:
                    print(Jog.Itensn)
                    GM2 = input('Qual item você quer usar?')
                    while GM2 not in Jog.Itensn:
                        GM2 = input('Qual item você quer usar?')
                    for i in Jog.Itens:
                        if i.nome == GM2:
                            i.usar()
                elif GM == 4:
                    if len(Jog.Milagres) == 0:
                        print('Você não possui milagres.')
                    else:
                        print(Jog.Milagres)
                        GM2 = input('Qual milagre você quer tentar?')
                        while GM2 not in Msn:
                            GM2 = input('Qual milagre você quer tentar?')
                        for m in Jog.Milagres:
                            if m.nome == GM2:
                                Milagre.m.help()
                        GM3 = input('Há um alvo específico? Quem?')
                        while GM3 not in Jogsn:
                            GM3 = input('Há um alvo específico? Quem?')
                        for j in Jogs:
                            if j.nome == GM3:
                                Milagre.m.milagre(Jog, j)
                            else:
                                Milagre.m.milagre(Jog)
                        
            elif GM0 == 4:
                print('Vai tarde covarde!')
                Jog.pv = 0

            for Jog in Jogs:
                print(Jog.nome, ' PV : ', Jog.pv, ' pontos = ', Jog.pontos)
            print("Mortos: ", Mortosn)
        print('############# FIM DE JOGO #############')
        print('')
        print('VENCEDOR:')
        print('')
        print('*** *** PLACAR FINAL *** ***')
        for j in Mortos:
            print(j.nome, ' pontos = ', j.pontos, ' kills = ', j.kills )

Jogs = []
Jogsn = []
DeckType = ['I', 'I', 'I', 'I', 'I', 'I', 'I', 'I' , 'I', 'M']
def princ():
    global Jogs
    global Jogsn
    print(Psn)
    GM = input('Olá! Escolha seu personagem! Após todos terminarem digite "0". Qual é o seu?')
    while GM != '0':
        for p in Ps:
            if p.nome == GM:
                Jogs.append(p)
                Jogsn.append(p.nome)
        print(Psn)
        GM = input('Olá! Escolha seu personagem! Após todos terminarem digite "0". Qual é o seu?')
    
    jogo()

princ()
#def princ():
    #jogs()
#princ()

