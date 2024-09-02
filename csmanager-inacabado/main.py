from tkinter import*
from tkinter import messagebox
import random
from random import randint

class app:
    def __init__(self, root):
        self.root = root
        self.saldo = 100000
        self.dia = 0
        self.patrocinador1 = ''
        self.patrocinadores1 = ['Pichau','iFood','Bauducco','oBoticário']
        self.patrocinador1_pagamento = 0
        self.patrocinador2 = ''
        self.patrocinador2_pagamento = 0
        self.patrocinador3 = ''
        self.patrocinador3_pagamento = 0
        self.conquista1 = ''
        self.conquista2 = ''
        self.conquista3 = ''
        self.conquista4 = ''
        self.vitorias = 0
        self.yalla = 0
        self.mapas = ['Dust2','Mirage','Nuke','Anubis','Ancient','Vertigo','Inferno']
        self.mouz = 96
        self.vitality = 97
        self.faze = 96
        self.g2 = 95
        self.spirit = 97
        self.navi = 94
        self.astralis = 93
        self.heroic = 93
        self.virtuspro = 92
        self.complexity = 90
        self.themongolz = 86
        self.liquid = 89
        self.eternalfire = 89
        self.novez = 85
        self.falcons = 86
        self.big = 85
        self.furia = 82
        self.betboom = 87
        self.mibr = 83
        self.flyquest = 80
        self.nip = 86
        self.m80 = 85
        self.pain = 84
        self.imperial = 85
        self.gamerlegion = 83
        self.monte = 83
        self.tresdmax = 81
        self.saw = 84
        self.fnatic = 83
        self.ence = 84
        self.sashi = 79
        self.gaimingladiators = 80
        self.aurora = 81
        self.amkal = 80
        self.novepandas = 78
        self.boito = 77
        self.bestia = 78
        self.boss = 75
        self.wildcard = 74
        self.partyastronauts = 73
        self.legacy = 75
        self.redcanids = 77
        self.fluxo = 77
        self.bleed = 79
        self.og = 78
        self.sharks = 74
        self.teams = [
    {"name": "MOUZ", "score": self.mouz},
    {"name": "Vitality", "score": self.vitality},
    {"name": "FaZe", "score": self.faze},
    {"name": "G2", "score": self.g2},
    {"name": "Spirit", "score": self.spirit},
    {"name": "NAVI", "score": self.navi},
    {"name": "Astralis", "score": self.astralis},
    {"name": "HEROIC", "score": self.heroic},
    {"name": "Virtus.pro", "score": self.virtuspro},
    {"name": "Complexity", "score": self.complexity},
    {"name": "The MongolZ", "score": self.themongolz},
    {"name": "Liquid", "score": self.liquid},
    {"name": "Eternal Fire", "score": self.eternalfire},
    {"name": "9z", "score": self.novez},
    {"name": "Falcons", "score": self.falcons},
    {"name": "BIG", "score": self.big},
    {"name": "FURIA", "score": self.furia},
    {"name": "BetBoom", "score": self.betboom},
    {"name": "MIBR", "score": self.mibr},
    {"name": "FlyQuest", "score": self.flyquest},
    {"name": "Ninjas in Pyjamas", "score": self.nip},
    {"name": "M80", "score": self.m80},
    {"name": "paiN", "score": self.pain},
    {"name": "Imperial", "score": self.imperial},
    {"name": "GamerLegion", "score": self.gamerlegion},
    {"name": "Monte", "score": self.monte},
    {"name": "3DMAX", "score": self.tresdmax},
    {"name": "SAW", "score": self.saw},
    {"name": "fnatic", "score": self.fnatic},
    {"name": "ENCE", "score": self.ence},
    {"name": "Sashi", "score": self.sashi},
    {"name": "Gaimin Gladiators", "score": self.gaimingladiators},
    {"name": "Aurora", "score": self.aurora},
    {"name": "AMKAL", "score": self.amkal},
    {"name": "9 pandas", "score": self.novepandas},
    {"name": "B8", "score": self.boito},
    {"name": "BESTIA", "score": self.bestia},
    {"name": "BOSS", "score": self.boss},
    {"name": "Wildcard", "score": self.wildcard},
    {"name": "Party Astronauts", "score": self.partyastronauts},
    {"name": "Legacy", "score": self.legacy},
    {"name": "RED Canids", "score": self.redcanids},
    {"name": "Fluxo", "score": self.fluxo},
    {"name": "BLEED", "score": self.bleed},
    {"name": "OG", "score": self.og},
    {"name": "Sharks", "score": self.sharks}
]
        self.primeira_vez = 0
        self.ranking()
        self.criacao1()


    def criacao1(self):
        self.num_criacao = Label(text='1', font=('Roboto',56),bg='#222331',fg='#44feb8')
        self.num_criacao.grid(column=0,row=0)
        self.label_criador = Label(text='CRIADOR DA EQUIPE',font=('Roboto',24),bg='#222331',fg='white')
        self.label_criador.grid(column=1,row=0)
        self.label_seu_nome = Label(text='Seu nome:',font=('Roboto',18),bg='#222331',fg='white')
        self.label_seu_nome.grid(column=2,row=1,pady=(150,0),padx=(85,24))
        self.entry_seu_nome = Entry(width=16,font=('Roboto',18))
        self.entry_seu_nome.grid(column=3,row=1,pady=(150,0))
        self.label_nome_equipe = Label(text='Nome da equipe:',font=('Roboto',18),bg='#222331',fg='white')
        self.label_nome_equipe.grid(column=2,row=2,padx=16,pady=(16,0))
        self.entry_nome_equipe = Entry(width=16,font=('Roboto',18))
        self.entry_nome_equipe.grid(column=3,row=2,padx=16,pady=(16,0))
        self.label_regiao = Label(text='Região:',font=('Roboto',18),bg='#222331',fg='white')
        self.label_regiao.grid(column=2,row=3,padx=(115,16),pady=(16,0))
        self.label_selected_regiao = Label(text='Américas',font=('Roboto',18),bg='#222331',fg='white')
        self.label_selected_regiao.grid(column=3,row=3,padx=16,pady=(16,0))
        self.button_avancar = Button(text='Avançar',font=('Roboto',18),bg='#1a1b26',fg='#44feb8',width=8,command=self.criacao2)
        self.button_avancar.grid(column=3,row=4,padx=16,pady=(24,0))

    def voltar_criacao1(self):
        self.label_rifler.grid_forget()
        self.label_awper.grid_forget()
        self.label_lurker.grid_forget()
        self.label_suporte.grid_forget()
        self.label_entryfragger.grid_forget()
        self.entry_rifler.grid_forget()
        self.entry_awper.grid_forget()
        self.entry_suporte.grid_forget()
        self.entry_lurker.grid_forget()
        self.entry_entryfragger.grid_forget()
        self.button_voltar.grid_forget()
        self.button_avancar.grid_forget()
        self.num_criacao.grid_forget()
        self.label_criador.grid_forget()
        self.criacao1()

    def criacao2(self):
        self.label_seu_nome.grid_forget()
        self.entry_seu_nome.grid_forget()
        self.label_nome_equipe.grid_forget()
        self.label_regiao.grid_forget()
        self.entry_nome_equipe.grid_forget()
        self.label_selected_regiao.grid_forget()
        self.num_criacao.config(text='2')
        self.button_avancar.grid(column=3,row=6,padx=16,pady=(24,0))
        self.label_rifler = Label(text='RIFLER',font=('Roboto',18),bg='#222331',fg='white')
        self.label_rifler.grid(column=2,row=1,pady=(120,0),padx=(85,24))
        self.entry_rifler = Entry(width=16,font=('Roboto',18))
        self.entry_rifler.grid(column=3,row=1,padx=16,pady=(120,0))
        self.label_awper = Label(text='AWPER',font=('Roboto',18),bg='#222331',fg='white')
        self.label_awper.grid(column=2,row=2,padx=(85,24),pady=(16,0))
        self.entry_awper = Entry(width=16,font=('Roboto',18))
        self.entry_awper.grid(column=3,row=2,padx=16,pady=(16,0))
        self.label_suporte = Label(text='SUPORTE',font=('Roboto',18),bg='#222331',fg='white')
        self.label_suporte.grid(column=2,row=3,padx=(85,24),pady=(16,0))
        self.entry_suporte = Entry(width=16,font=('Roboto',18))
        self.entry_suporte.grid(column=3,row=3,padx=16,pady=(16,0))
        self.label_lurker = Label(text='LURKER',font=('Roboto',18),bg='#222331',fg='white')
        self.label_lurker.grid(column=2,row=4,padx=(85,24),pady=(16,0))
        self.entry_lurker = Entry(width=16,font=('Roboto',18))
        self.entry_lurker.grid(column=3,row=4,padx=16,pady=(16,0))
        self.label_entryfragger = Label(text='ENTRY',font=('Roboto',18),bg='#222331',fg='white')
        self.label_entryfragger.grid(column=2,row=5,padx=(85,24),pady=(16,0))
        self.entry_entryfragger = Entry(width=16,font=('Roboto',18))
        self.entry_entryfragger.grid(column=3,row=5,padx=16,pady=(16,0))
        self.button_voltar = Button(text='Voltar',font=('Roboto',18),bg='#1a1b26',fg='#44feb8',width=8,command=self.voltar_criacao1)
        self.button_voltar.grid(column=2,row=6,pady=(24,0),padx=(80,0))
        self.button_avancar.config(command=self.criacao3)

    def voltar_criacao2(self):
        self.label_fimcriacao.grid_forget()
        self.button_avancar.grid_forget()
        self.button_voltar.grid_forget()
        self.criacao2()

    def criacao3(self):
        self.nome = self.entry_seu_nome.get()
        self.equipe = self.entry_nome_equipe.get()
        self.player1 = self.entry_rifler.get()
        self.player2 = self.entry_awper.get()
        self.player3 = self.entry_suporte.get()
        self.player4 = self.entry_lurker.get()
        self.player5 = self.entry_entryfragger.get()
        self.over_player1 = randint(65,75)
        self.over_player2 = randint(65,75)
        self.over_player3 = randint(65,75)
        self.over_player4 = randint(65,75)
        self.over_player5 = randint(65,75)
        self.over_equipe = (self.over_player1+self.over_player2+self.over_player3+self.over_player4+self.over_player5) / 5
        self.label_rifler.grid_forget()
        self.label_awper.grid_forget()
        self.label_lurker.grid_forget()
        self.label_suporte.grid_forget()
        self.label_entryfragger.grid_forget()
        self.entry_rifler.grid_forget()
        self.entry_awper.grid_forget()
        self.entry_suporte.grid_forget()
        self.entry_lurker.grid_forget()
        self.entry_entryfragger.grid_forget()
        self.button_voltar.grid(column=2,row=2,padx=(0,160))
        self.button_voltar.config(command=self.voltar_criacao2)
        self.button_avancar.grid(column=2,row=2,padx=(160,0))
        self.button_avancar.config(command=self.menu)
        self.num_criacao.config(text='3')
        self.label_fimcriacao = Label(text=f'{self.nome}, sua equipe {self.equipe}, situada na região Américas\nestá pronta para começar!',font=('Roboto',18),bg='#222331',fg='white')
        self.label_fimcriacao.grid(column=2,row=1,pady=(160,80),padx=(85,0))
        self.dia = int(input('escolher dia'))

    def ranking(self):
        self.ranking1 = max(self.teams, key=lambda x: x['score'])
        self.teams.remove(self.ranking1)
        self.ranking2 = max(self.teams, key=lambda x: x['score'])
        self.teams.remove(self.ranking2)
        self.ranking3 = max(self.teams, key=lambda x: x['score'])
        self.teams.remove(self.ranking3)
        self.ranking4 = max(self.teams, key=lambda x: x['score'])
        self.teams.remove(self.ranking4)
        self.ranking5 = max(self.teams, key=lambda x: x['score'])
        self.teams.remove(self.ranking5)
        self.ranking6 = max(self.teams, key=lambda x: x['score'])
        self.teams.remove(self.ranking6)
        self.ranking7 = max(self.teams, key=lambda x: x['score'])
        self.teams.remove(self.ranking7)
        self.ranking8 = max(self.teams, key=lambda x: x['score'])
        self.teams.remove(self.ranking8)
        self.ranking9 = max(self.teams, key=lambda x: x['score'])
        self.teams.remove(self.ranking9)
        self.ranking10 = max(self.teams, key=lambda x: x['score'])
        self.teams.remove(self.ranking10)
        self.teams.append(self.ranking1)
        self.teams.append(self.ranking2)
        self.teams.append(self.ranking3)
        self.teams.append(self.ranking4)
        self.teams.append(self.ranking5)
        self.teams.append(self.ranking6)
        self.teams.append(self.ranking7)
        self.teams.append(self.ranking8)
        self.teams.append(self.ranking9)
        self.teams.append(self.ranking10)

    def menu(self):
        if self.primeira_vez == 0:
            self.teams.append({"name": f"{self.equipe}", "score": self.over_equipe})
            self.primeira_vez = 1
        self.ranking()
        self.button_voltar.grid_forget()
        self.button_avancar.grid_forget()
        self.num_criacao.grid_forget()
        self.label_fimcriacao.grid_forget()
        self.label_criador.grid_forget()
        self.button_campeonatos = Button(text='CAMPEONATOS',font=('Roboto',18),bg='#1a1b26',fg='white',width=16,command=self.campeonatos)
        self.button_campeonatos.grid(column=1,row=0,pady=(16,0))
        self.button_treinamento = Button(text='TREINAMENTO',font=('Roboto',18),bg='#1a1b26',fg='white',width=16,command=self.treinamentos)
        self.button_treinamento.grid(column=2,row=0,pady=(16,0),padx=(0,0))
        self.button_transferencias = Button(text='TRANSFERÊNCIAS',font=('Roboto',18),bg='#1a1b26',fg='white',width=16)
        self.button_transferencias.grid(column=3,row=0,pady=(16,0),padx=(24,0))
        self.label_saldo = Label(text=f'$ {self.saldo}',font=('Roboto',18),bg='#222331',fg='white')
        self.label_saldo.grid(column=4,row=0,pady=(16,0),padx=(24,0))
        self.label_dia = Label(text=f'DIA {self.dia}',font=('Roboto',18),bg='#222331',fg='white')
        self.label_dia.grid(column=5,row=0,pady=(16,0),padx=(24,0))
        self.button_avancar2 = Button(text='AVANÇAR',font=('Roboto',18),bg='#44feb8',fg='black',command=self.calendario)
        self.button_avancar2.grid(column=6,row=0,pady=(16,0),padx=(8,0))
        self.frame_patrocinadores = Frame(bg='#1a1b26',height=200,width=250)
        self.frame_patrocinadores.grid(column=1,row=1,pady=(48,0),padx=(48,24)) 
        self.label_patrocinadores = Label(text=f'PATROCINADORES\n\n{self.patrocinador1}\n{self.patrocinador2}\n{self.patrocinador3}\n',font=('Roboto',16),bg='#1a1b26',fg='white')
        self.label_patrocinadores.grid(column=1,row=1,pady=48,padx=(48,24))
        self.frame_conquistas = Frame(bg='#1a1b26',height=200,width=250)
        self.frame_conquistas.grid(column=2,row=1,pady=(48,0),padx=(48,24))
        self.label_conquistas = Label(text=f'CONQUISTAS\n\n{self.conquista1}\n{self.conquista2}\n{self.conquista3}\n{self.conquista4}',font=('Roboto',16),bg='#1a1b26',fg='white')
        self.label_conquistas.grid(column=2,row=1,pady=24,padx=(48,24))
        self.frame_rating = Frame(bg='#1a1b26',height=200,width=250)
        self.frame_rating.grid(column=3,row=1,pady=(48,0),padx=(48,24))
        self.label_rating = Label(text='RATING\n\n\n\n\n',font=('Roboto',16),bg='#1a1b26',fg='white')
        self.label_rating.grid(column=3,row=1,pady=24)
        self.frame_ranking = Frame(bg='#1a1b26',height=350,width=250)
        self.frame_ranking.grid(column=1,row=2,pady=(48,24),padx=(48,24))
        self.label_ranking = Label(text=f'RANKING\n\n#1 {self.ranking1['name']}\n#2 {self.ranking2['name']}\n#3 {self.ranking3['name']}\n#4 {self.ranking4['name']}\n#5 {self.ranking5['name']}\n#6 {self.ranking6['name']}\n#7 {self.ranking7['name']}\n#8 {self.ranking8['name']}\n#9 {self.ranking9['name']}\n#10 {self.ranking10['name']}',font=('Roboto',18),bg='#1a1b26',fg='white')
        self.label_ranking.grid(column=1,row=2,pady=(48,24),padx=(48,24))
        self.frame_posicoes = Frame(bg='#1a1b26',height=350,width=250)
        self.frame_posicoes.grid(column=2,row=2,pady=(48,24),padx=(48,24))
        self.label_posicoes = Label(text='EQUIPE:\n\nRIFLER:\n\nAWPER:\n\nSUPORTE:\n\nLURKER:\n\nENTRY:',font=('Roboto',18),bg='#1a1b26',fg='white')
        self.label_posicoes.grid(column=2,row=2,pady=(48,24),padx=(48,24))
        self.frame_nomes = Frame(bg='#1a1b26',height=350,width=250)
        self.frame_nomes.grid(column=3,row=2,pady=(48,24),padx=(48,24))
        self.label_nomes = Label(text=f'{self.equipe}\n\n{self.player1}\n\n{self.player2}\n\n{self.player3}\n\n{self.player4}\n\n{self.player5}',font=('Roboto',18),bg='#1a1b26',fg='white')
        self.label_nomes.grid(column=3,row=2,pady=(48,24),padx=(48,24))
        self.frame_overalls = Frame(bg='#1a1b26',height=350,width=100)
        self.frame_overalls.grid(column=4,row=2,pady=(48,24),padx=(24,24))
        self.label_overalls = Label(text=f'{self.over_equipe}\n\n{self.over_player1}\n\n{self.over_player2}\n\n{self.over_player3}\n\n{self.over_player4}\n\n{self.over_player5}',font=('Roboto',18),bg='#1a1b26',fg='white')
        self.label_overalls.grid(column=4,row=2,pady=(48,24),padx=(24,24))

    def calendario(self):
        self.dia += 1
        self.label_dia.config(text=f'DIA {self.dia}')
        self.label_saldo.config(text=f'$ {self.saldo}')
        if 9 < self.dia < 15:
            self.camp = 'Qualifier IEM Changdu'
            self.qualifieriemchengdu()
        elif 17 < self.dia < 23:
            self.camp = 'RMR Major Copenhagen'
            self.rmr_major_copenhagen()
        elif 24 < self.dia < 28:
            self.camp = 'Qualifier PRO League'
            self.qualifierproleague()
        elif 32 < self.dia < 37:
            self.camp = 'Play In IEM Katowice'
            self.playin_iem_katowice()
        elif 39 < self.dia < 48:
            self.camp = 'IEM Katowice'
            self.iem_katowice()
        elif 54 < self.dia < 60:
            self.camp = 'Qualifier IEM Dallas'
            self.qualifieriemdallas()
        elif 66 < self.dia < 71:
            self.camp = 'RES LATAM'
            self.res_latam()
        elif 76 < self.dia < 80:
            self.camp = 'Qualifier Challenger League'
            self.qualifierchallengerleague()
        elif 89 < self.dia < 99:
            self.camp = 'YaLLa Compass'
            self.yalla_compass()
        elif self.dia == 104:
            self.camp = 'IEM Changdu'
        elif self.dia == 114:
            self.camp = 'PRO League'
        elif self.dia == 115:
            self.camp = 'Challenger League'
        elif self.dia == 128:
            self.camp = 'Qualifier BET Boom Dacha'
        elif self.dia == 130:
            self.camp = 'Qualifier CCT Global Finals'
        elif self.dia == 140:
            self.camp = 'Major Copenhagen'
        elif self.dia == 156:
            self.camp = 'IEM Dallas'
        elif self.dia == 166:
            self.camp = 'BET BOOM Dacha'
        elif self.dia == 172:
            self.camp = 'Qualifier BLAST Premier'
        elif self.dia == 178:
            self.camp = 'CCT Global Finals'
        elif self.dia == 188:
            self.camp = 'Qualifier Esports World Cup'
        elif self.dia == 193:
            self.camp = 'FireLeague'
        elif self.dia == 200:
            self.camp = 'Play In IEM Cologne'
        elif self.dia == 210:
            self.camp = 'Qualifier Pro League 2'
        elif self.dia == 215:
            self.camp = 'Qualifier Challenger League 2'
        elif self.dia == 220:
            self.camp = 'Esports World Cup'
        elif self.dia == 228:
            self.camp = 'BLAST Premier'
        elif self.dia == 240:
            self.camp = 'RMR Major Xangai'
        elif self.dia == 247:
            self.camp = 'IEM Cologne'
        elif self.dia == 260:
            self.camp = 'Qualifier IEM Rio'
        elif self.dia == 265:
            self.camp = 'Pro League 2'
        elif self.dia == 266:
            self.camp = 'Challenger League 2'
        elif self.dia == 280:
            self.camp = 'Qualifier IESF World'
        elif self.dia == 285:
            self.camp = 'RES WORLD'
        elif self.dia == 300:
            self.camp = 'Qualifier Thunderpick World'
        elif self.dia == 306:
            self.camp = 'IEM Rio'
        elif self.dia == 320:
            self.camp = 'IESF World'
        elif self.dia == 325:
            self.camp = 'CBCS'
        elif self.dia == 338:
            self.camp = 'Major Xangai'

    def atualizar_overs(self):
        self.mouz += randint(-1,1)
        self.vitality += randint(-1,1)
        self.faze += randint(-1,1)
        self.g2 += randint(-1,1)
        self.spirit += randint(-1,1)
        self.navi += randint(-1,1)
        self.astralis += randint(-1,1)
        self.heroic += randint(-1,1)
        self.virtuspro += randint(-1,1)
        self.complexity += randint(-1,1)
        self.themongolz += randint(-1,1)
        self.liquid += randint(-1,1)
        self.eternalfire += randint(-1,1)
        self.novez += randint(-1,1)
        self.falcons += randint(-1,1)
        self.big += randint(-1,1)
        self.furia += randint(-1,1)
        self.betboom += randint(-1,1)
        self.mibr += randint(-1,1)
        self.flyquest += randint(-1,1)
        self.nip += randint(-1,1)
        self.m80 += randint(-1,1)
        self.pain += randint(-1,1)
        self.imperial += randint(-1,1)
        self.gamerlegion += randint(-1,1)
        self.monte += randint(-1,1)
        self.tresdmax += randint(-1,1)
        self.saw += randint(-1,1)
        self.fnatic += randint(-1,1)
        self.ence += randint(-1,1)
        self.sashi += randint(-1,1)
        self.gaimingladiators += randint(-1,1)
        self.aurora += randint(-1,1)
        self.amkal += randint(-1,1)
        self.novepandas += randint(-1,1)
        self.boito += randint(-1,1)
        self.bestia += randint(-1,1)
        self.boss += randint(-1,1)
        self.wildcard += randint(-1,1)
        self.partyastronauts += randint(-1,1)
        self.legacy += randint(-1,1)
        self.redcanids += randint(-1,1)
        self.fluxo += randint(-1,1)
        self.bleed += randint(-1,1)
        self.og += randint(-1,1)
        self.sharks += randint(-1,1)           
        self.teams = [
    {"name": "MOUZ", "score": self.mouz},
    {"name": "Vitality", "score": self.vitality},
    {"name": "FaZe", "score": self.faze},
    {"name": "G2", "score": self.g2},
    {"name": "Spirit", "score": self.spirit},
    {"name": "NAVI", "score": self.navi},
    {"name": "Astralis", "score": self.astralis},
    {"name": "HEROIC", "score": self.heroic},
    {"name": "Virtus.pro", "score": self.virtuspro},
    {"name": "Complexity", "score": self.complexity},
    {"name": "The MongolZ", "score": self.themongolz},
    {"name": "Liquid", "score": self.liquid},
    {"name": "Eternal Fire", "score": self.eternalfire},
    {"name": "9z", "score": self.novez},
    {"name": "Falcons", "score": self.falcons},
    {"name": "BIG", "score": self.big},
    {"name": "FURIA", "score": self.furia},
    {"name": "BetBoom", "score": self.betboom},
    {"name": "MIBR", "score": self.mibr},
    {"name": "FlyQuest", "score": self.flyquest},
    {"name": "Ninjas in Pyjamas", "score": self.nip},
    {"name": "M80", "score": self.m80},
    {"name": "paiN", "score": self.pain},
    {"name": "Imperial", "score": self.imperial},
    {"name": "GamerLegion", "score": self.gamerlegion},
    {"name": "Monte", "score": self.monte},
    {"name": "3DMAX", "score": self.tresdmax},
    {"name": "SAW", "score": self.saw},
    {"name": "fnatic", "score": self.fnatic},
    {"name": "ENCE", "score": self.ence},
    {"name": "Sashi", "score": self.sashi},
    {"name": "Gaimin Gladiators", "score": self.gaimingladiators},
    {"name": "Aurora", "score": self.aurora},
    {"name": "AMKAL", "score": self.amkal},
    {"name": "9 pandas", "score": self.novepandas},
    {"name": "B8", "score": self.boito},
    {"name": "BESTIA", "score": self.bestia},
    {"name": "BOSS", "score": self.boss},
    {"name": "Wildcard", "score": self.wildcard},
    {"name": "Party Astronauts", "score": self.partyastronauts},
    {"name": "Legacy", "score": self.legacy},
    {"name": "RED Canids", "score": self.redcanids},
    {"name": "Fluxo", "score": self.fluxo},
    {"name": "BLEED", "score": self.bleed},
    {"name": "OG", "score": self.og},
    {"name": "Sharks", "score": self.sharks},
    {"name": f"{self.equipe}", "score": self.over_equipe}
]
        print('overs atualizados')

    def treinamentos(self):
        self.button_campeonatos.grid_forget()
        self.button_avancar2.grid_forget()
        self.button_treinamento.grid_forget()
        self.button_transferencias.grid_forget()
        self.label_saldo.grid_forget()
        self.label_dia.grid_forget()
        self.label_patrocinadores.grid_forget()
        self.frame_patrocinadores.grid_forget()
        self.frame_conquistas.grid_forget()
        self.frame_nomes.grid_forget()
        self.frame_overalls.grid_forget()
        self.frame_posicoes.grid_forget()
        self.frame_ranking.grid_forget()
        self.frame_rating.grid_forget()
        self.label_conquistas.grid_forget()
        self.label_rating.grid_forget()
        self.label_ranking.grid_forget()
        self.label_posicoes.grid_forget()
        self.label_nomes.grid_forget()
        self.label_overalls.grid_forget()
        self.button_voltar_trei = Button(text='Voltar',font=('Roboto',18),bg='#1a1b26',fg='#44feb8',command=self.voltar_menu_trei)
        self.button_voltar_trei.grid(column=0,row=0,pady=(24,12),padx=(24,24))
        self.button_bootcamp1 = Button(text='BOOTCAMP 1',font=('Roboto',18),bg='#1a1b26',fg='white',command=self.bootcamp1)
        self.button_bootcamp1.grid(column=1,row=2,pady=(48,24),padx=(24,24))
        self.button_bootcamp2 = Button(text='BOOTCAMP 2',font=('Roboto',18),bg='#1a1b26',fg='white',command=self.bootcamp2)
        self.button_bootcamp2.grid(column=2,row=2,pady=(48,24),padx=(24,24))
        self.button_bootcamp3 = Button(text='BOOTCAMP 3',font=('Roboto',18),bg='#1a1b26',fg='white',command=self.bootcamp3)
        self.button_bootcamp3.grid(column=3,row=2,pady=(48,24),padx=(24,24))
        self.button_treinosimples = Button(text='TREINO SIMPLES',font=('Roboto',18),bg='#1a1b26',fg='white',command=self.treino_simples)
        self.button_treinosimples.grid(column=4,row=2,pady=(48,24),padx=(24,24))
        self.label_bootcamp1 = Label(text='Bootcamp de 3 dias\n\n-20000',font=('Roboto',18),bg='#222331',fg='white')
        self.label_bootcamp1.grid(column=1,row=3,pady=(24,12),padx=(24,24))
        self.label_bootcamp2 = Label(text='Bootcamp de 5 dias\n\n-35000',font=('Roboto',18),bg='#222331',fg='white')
        self.label_bootcamp2.grid(column=2,row=3,pady=(24,12),padx=(24,24))
        self.label_bootcamp3 = Label(text='Bootcamp de 10 dias\n\n-65000',font=('Roboto',18),bg='#222331',fg='white')
        self.label_bootcamp3.grid(column=3,row=3,pady=(24,12),padx=(24,24))
        self.label_treinosimples = Label(text='Treino simples\n\n-10000',font=('Roboto',18),bg='#222331',fg='white')
        self.label_treinosimples.grid(column=4,row=3,pady=(24,12),padx=(24,24))
        self.frame_posicoes2 = Frame(bg='#1a1b26',height=350,width=250)
        self.frame_posicoes2.grid(column=1,row=4,pady=(48,24),padx=(48,24))
        self.label_posicoes2 = Label(text='EQUIPE:\n\nRIFLER:\n\nAWPER:\n\nSUPORTE:\n\nLURKER:\n\nENTRY:',font=('Roboto',18),bg='#1a1b26',fg='white')
        self.label_posicoes2.grid(column=1,row=4,pady=(48,24),padx=(48,24))
        self.frame_nomes2 = Frame(bg='#1a1b26',height=350,width=250)
        self.frame_nomes2.grid(column=2,row=4,pady=(48,24),padx=(48,24))
        self.label_nomes2 = Label(text=f'{self.equipe}\n\n{self.player1}\n\n{self.player2}\n\n{self.player3}\n\n{self.player4}\n\n{self.player5}',font=('Roboto',18),bg='#1a1b26',fg='white')
        self.label_nomes2.grid(column=2,row=4,pady=(48,24),padx=(48,24))
        self.frame_overalls2 = Frame(bg='#1a1b26',height=350,width=100)
        self.frame_overalls2.grid(column=3,row=4,pady=(48,24),padx=(24,24))
        self.label_overalls2 = Label(text=f'{self.over_equipe}\n\n{self.over_player1}\n\n{self.over_player2}\n\n{self.over_player3}\n\n{self.over_player4}\n\n{self.over_player5}',font=('Roboto',18),bg='#1a1b26',fg='white')
        self.label_overalls2.grid(column=3,row=4,pady=(48,24),padx=(24,24))

    def bootcamp1(self):
        self.winner = 0
        self.dia += 3
        self.saldo -= 20000
        self.over_player1 += randint(0,1)
        self.over_player2 += randint(0,1)
        self.over_player3 += randint(0,1)
        self.over_player4 += randint(0,1)
        self.over_player5 += randint(0,1)
        self.over_equipe = (self.over_player1+self.over_player2+self.over_player3+self.over_player4+self.over_player5) / 5
        self.label_overalls2.config(text=f'{self.over_equipe}\n\n{self.over_player1}\n\n{self.over_player2}\n\n{self.over_player3}\n\n{self.over_player4}\n\n{self.over_player5}')

    def bootcamp2(self):
        self.winner = 0
        self.dia += 5
        self.saldo -= 35000
        self.over_player1 += randint(0,2)
        self.over_player2 += randint(0,2)
        self.over_player3 += randint(0,2)
        self.over_player4 += randint(0,2)
        self.over_player5 += randint(0,2)
        self.over_equipe = (self.over_player1+self.over_player2+self.over_player3+self.over_player4+self.over_player5) / 5
        self.label_overalls2.config(text=f'{self.over_equipe}\n\n{self.over_player1}\n\n{self.over_player2}\n\n{self.over_player3}\n\n{self.over_player4}\n\n{self.over_player5}')
        self.atualizar_overs()

    def bootcamp3(self):
        self.winner = 0
        self.dia += 10
        self.saldo -= 65000
        self.over_player1 += randint(1,3)
        self.over_player2 += randint(1,3)
        self.over_player3 += randint(1,3)
        self.over_player4 += randint(1,3)
        self.over_player5 += randint(1,3)
        self.over_equipe = (self.over_player1+self.over_player2+self.over_player3+self.over_player4+self.over_player5) / 5
        self.label_overalls2.config(text=f'{self.over_equipe}\n\n{self.over_player1}\n\n{self.over_player2}\n\n{self.over_player3}\n\n{self.over_player4}\n\n{self.over_player5}')
        self.atualizar_overs()

    def treino_simples(self):
        self.dia += 1
        self.saldo -= 10000
        self.possiveis = [0,0,0,0,1]
        self.over_player1 += random.choice(self.possiveis)
        self.over_player2 += random.choice(self.possiveis)
        self.over_player3 += random.choice(self.possiveis)
        self.over_player4 += random.choice(self.possiveis)
        self.over_player5 += random.choice(self.possiveis)
        self.over_equipe = (self.over_player1+self.over_player2+self.over_player3+self.over_player4+self.over_player5) / 5
        self.label_overalls2.config(text=f'{self.over_equipe}\n\n{self.over_player1}\n\n{self.over_player2}\n\n{self.over_player3}\n\n{self.over_player4}\n\n{self.over_player5}')

    def voltar_menu_trei(self):
        self.button_voltar_trei.grid_forget()
        self.button_bootcamp1.grid_forget()
        self.button_bootcamp2.grid_forget()
        self.button_bootcamp3.grid_forget()
        self.button_treinosimples.grid_forget()
        self.label_treinosimples.grid_forget()
        self.label_bootcamp1.grid_forget()
        self.label_bootcamp2.grid_forget()
        self.label_bootcamp3.grid_forget()
        self.frame_nomes2.grid_forget()
        self.frame_overalls2.grid_forget()
        self.frame_posicoes2.grid_forget()
        self.label_posicoes2.grid_forget()
        self.label_nomes2.grid_forget()
        self.label_overalls2.grid_forget()
        self.menu()

    def campeonatos(self):
        self.button_campeonatos.grid_forget()
        self.button_avancar2.grid_forget()
        self.button_treinamento.grid_forget()
        self.button_transferencias.grid_forget()
        self.label_saldo.grid_forget()
        self.label_dia.grid_forget()
        self.label_patrocinadores.grid_forget()
        self.frame_patrocinadores.grid_forget()
        self.frame_conquistas.grid_forget()
        self.frame_nomes.grid_forget()
        self.frame_overalls.grid_forget()
        self.frame_posicoes.grid_forget()
        self.frame_ranking.grid_forget()
        self.frame_rating.grid_forget()
        self.label_conquistas.grid_forget()
        self.label_rating.grid_forget()
        self.label_ranking.grid_forget()
        self.label_posicoes.grid_forget()
        self.label_nomes.grid_forget()
        self.label_overalls.grid_forget()
        self.prox_camp1 = 'Próximo campeonato1'
        self.prizepool1 = 0
        self.data1 = 0
        self.quant_times1 = 0
        self.prox_camp2 = 'Próximo campeonato2'
        self.prizepool2 = 0
        self.data2 = 0
        self.quant_times2 = 0
        self.definir_proxms_camps()
        self.button_voltar_camp = Button(text='Voltar',font=('Roboto',18),bg='#1a1b26',fg='#44feb8',command=self.voltar_menu_camp)
        self.button_voltar_camp.grid(column=0,row=0,pady=(24,24),padx=(24,24))
        self.label_prox_camp = Label(text='Próximos campeonatos:',font=('Roboto',18),bg='#222331',fg='white')
        self.label_prox_camp.grid(column=1,row=1,pady=(48,12),padx=(24,24))
        self.frame_campeonatos1 = Frame(bg='#1a1b26',height=200,width=350)
        self.frame_campeonatos1.grid(column=2,row=1,pady=(48,12),padx=(24,24))
        self.frame_campeonatos2 = Frame(bg='#1a1b26',height=200,width=350)
        self.frame_campeonatos2.grid(column=3,row=1,pady=(48,12),padx=(24,24))
        self.label_campeonatos1 = Label(text=f'{self.prox_camp1}\n\nPrize pool: {self.prizepool1}\n\nData: dia {self.data1}\n\nTimes: {self.quant_times1}',font=('Roboto',18),bg='#1a1b26',fg='white')
        self.label_campeonatos1.grid(column=2,row=1,pady=(48,12),padx=(24,24))
        self.label_campeonatos2 = Label(text=f'{self.prox_camp2}\n\nPrize pool: {self.prizepool2}\n\nData: dia {self.data2}\n\nTimes: {self.quant_times2}',font=('Roboto',18),bg='#1a1b26',fg='white')
        self.label_campeonatos2.grid(column=3,row=1,pady=(48,12),padx=(24,24))
        self.button_inscrever1 = Button(text='INSCREVER-SE',font=('Roboto',18),bg='#1a1b26',fg='white',command=self.inscrever1)
        self.button_inscrever1.grid(column=2,row=2,pady=(24,12),padx=(24,24))
        self.button_inscrever2 = Button(text='INSCREVER-SE',font=('Roboto',18),bg='#1a1b26',fg='white',command=self.inscrever2)
        self.button_inscrever2.grid(column=3,row=2,pady=(24,12),padx=(24,24))

    def inscrever1(self):
        if 0 <= self.dia < 18:
            self.qualiiemchengdu = 1
        elif 18 <= self.dia < 33:
            self.qualiproleague = 1
        elif 55 <= self.dia < 77:
            self.reslatam = 1
        elif 77 <= self.dia < 104:
            self.yallacomppass = 1
        elif 104 <= self.dia < 115 and self.challengerleague == 0 and self.proleague == -1:
            self.proleague = 1
        elif 115 <= self.dia < 130:
            self.qualibbdacha = 1
        elif 188 <= self.dia < 200:
            self.fireleague = 1
        elif 200 <= self.dia < 215:
            self.qualiproleague2 = 1
        elif 228 <= self.dia < 247:
            self.rmrmajorxangai = 1
        elif 247 <= self.dia < 265:
            self.qualiiemrio = 1
        elif 265 <= self.dia < 280 and self.proleague2 == 0 and self.proleague2 == -1:
            self.challengerleague2 = 1
        elif 320 <= self.dia < 365:
            self.cbcs = 1
        else:
            messagebox.showerror('Alerta','Você já está inscrito ou não pode\nse inscrever nesse torneio!')

    def inscrever2(self):
        if 0 <= self.dia < 18:
            self.rmrmajorcopenhagen = 1
        elif 18 <= self.dia < 33:
            self.playiniemkatowice = 1
        elif 33 <= self.dia < 55:
            self.qualiiemdallas = 1
        elif 55 <= self.dia < 77:
            self.qualichallengerleague = 1
        elif 104 <= self.dia < 115 and self.proleague == 0 and self.challengerleague == -1:
            self.challengerleague = 1
        elif 115 <= self.dia < 130:
            self.qualicct = 1
        elif 156 <= self.dia < 172:
            self.qualiblastpremier = 1
        elif 172 <= self.dia < 188:
            self.qualiesportswc = 1
        elif 188 <= self.dia < 200:
            self.playiniemcologne = 1
        elif 200 <= self.dia < 215:
            self.qualichallengerleague2 = 1
        elif 247 <= self.dia < 265 and self.challengerleague2 == 0 and self.challengerleague2 == -1:
            self.proleague2 = 1
        elif 265 <= self.dia < 280:
            self.qualiiesfworld = 1
        elif 280 <= self.dia < 300:
            self.qualithunderpickworld = 1
        else:
            messagebox.showerror('Alerta','Você já está inscrito ou não pode\nse inscrever nesse torneio!')


    def voltar_menu_camp(self):
        self.button_voltar_camp.grid_forget()
        self.label_prox_camp.grid_forget()
        self.frame_campeonatos1.grid_forget()
        self.frame_campeonatos2.grid_forget()
        self.label_campeonatos2.grid_forget()
        self.label_campeonatos1.grid_forget()
        self.button_inscrever1.grid_forget()
        self.button_inscrever2.grid_forget()
        self.menu()

    def definir_proxms_camps(self):
        if 0 <= self.dia < 18:
            self.prox_camp1 = 'Qualifier IEM Changdu'
            self.quant_times1 = 4
            self.data1 = 10
            self.prizepool1 = 'IEM Changdu'
            self.prox_camp2 = 'RMR Major Copenhagen'
            self.quant_times2 = 16
            self.data2 = 18
            self.prizepool2 = 'Major Copenhagen'
        elif 18 <= self.dia < 33:
            self.prox_camp1 = 'Qualifier PRO League'
            self.quant_times1 = 8
            self.data1 = 25
            self.prizepool1 = 'PRO League'
            self.prox_camp2 = 'Play In IEM Katowice'
            self.quant_times2 = 16
            self.data2 = 33
            self.prizepool2 = 'IEM Katowice'
        elif 33 <= self.dia < 55:
            self.prox_camp1 = 'IEM Katowice'
            self.quant_times1 = 16
            self.data1 = 40
            self.prizepool1 = 1000000
            self.prox_camp2 = 'Qualifier IEM Dallas'
            self.quant_times2 = 4
            self.data2 = 55
            self.prizepool2 = 'IEM Dallas'
        elif 55 <= self.dia < 77:
            self.prox_camp1 = 'RES LATAM'
            self.quant_times1 = 8
            self.data1 = 67
            self.prizepool1 = 50000
            self.prox_camp2 = 'Qualifier Challenger League'
            self.quant_times2 = 4
            self.data2 = 77
            self.prizepool2 = 'Challenger League'
        elif 77 <= self.dia < 104:
            self.prox_camp1 = 'YaLLa Compass'
            self.quant_times1 = 12
            self.data1 = 90
            self.prizepool1 = 400000
            self.prox_camp2 = 'IEM Changdu'
            self.quant_times2 = 16
            self.data2 = 104
            self.prizepool2 = 250000
        elif 104 <= self.dia < 115:
            self.prox_camp1 = 'PRO League'
            self.quant_times1 = 32
            self.data1 = 114
            self.prizepool1 = 750000
            self.prox_camp2 = 'Challenger League'
            self.quant_times2 = 8
            self.data2 = 115
            self.prizepool2 = 50000
        elif 115 <= self.dia < 130:
            self.prox_camp1 = 'Qualifier BET Boom Dacha'
            self.quant_times1 = 4
            self.data1 = 128
            self.prizepool1 = 'BET Boom Dacha'
            self.prox_camp2 = 'Qualifier CCT Global Finals'
            self.quant_times2 = 6
            self.data2 = 130
            self.prizepool2 = 'CCT Global Finals'
        elif 130 <= self.dia < 156:
            self.prox_camp1 = 'Major Copenhagen'
            self.quant_times1 = 24
            self.data1 = 140
            self.prizepool1 = 1250000
            self.prox_camp2 = 'IEM Dallas'
            self.quant_times2 = 16
            self.data2 = 156
            self.prizepool2 = 250000
        elif 156 <= self.dia < 172:
            self.prox_camp1 = 'BET BOOM Dacha'
            self.quant_times1 = 8
            self.data1 = 166
            self.prizepool1 = 500000
            self.prox_camp2 = 'Qualifier BLAST Premier'
            self.quant_times2 = 6
            self.data2 = 172
            self.prizepool2 = 'BLAST Premier'
        elif 172 <= self.dia < 188:
            self.prox_camp1 = 'CCT Global Finals'
            self.quant_times1 = 16
            self.data1 = 178
            self.prizepool1 = 500000
            self.prox_camp2 = 'Qualifier Esports World Cup'
            self.quant_times2 = 4
            self.data2 = 188
            self.prizepool2 = 'Esports World Cup'
        elif 188 <= self.dia < 200:
            self.prox_camp1 = 'Fire League'
            self.quant_times1 = 8
            self.data1 = 193
            self.prizepool1 = 150000
            self.prox_camp2 = 'Play In IEM Cologne'
            self.quant_times2 = 16
            self.data2 = 200
            self.prizepool2 = 'IEM Cologne'
        elif 200 <= self.dia < 215:
            self.prox_camp1 = 'Qualifier PRO League 2'
            self.quant_times1 = 12
            self.data1 = 210
            self.prizepool1 = 'PRO League 2'
            self.prox_camp2 = 'Qualifier Challenger League 2'
            self.quant_times2 = 8
            self.data2 = 215
            self.prizepool2 = 'Challenger League 2'
        elif 215 <= self.dia < 228:
            self.prox_camp1 = 'Esports World Cup'
            self.quant_times1 = 15
            self.data1 = 220
            self.prizepool1 = 1000000
            self.prox_camp2 = 'BLAST Premier'
            self.quant_times2 = 8
            self.data2 = 228
            self.prizepool2 = 425000
        elif 228 <= self.dia < 247:
            self.prox_camp1 = 'RMR Major Xangai'
            self.quant_times1 = 16
            self.data1 = 240
            self.prizepool1 = 'Major Xangai'
            self.prox_camp2 = 'IEM Cologne'
            self.quant_times2 = 16
            self.data2 = 247
            self.prizepool2 = 1000000
        elif 247 <= self.dia < 265:
            self.prox_camp1 = 'Qualifier IEM Rio'
            self.quant_times1 = 4
            self.data1 = 260
            self.prizepool1 = 'IEM Rio'
            self.prox_camp2 = 'PRO League 2'
            self.quant_times2 = 32
            self.data2 = 265
            self.prizepool2 = 750000
        elif 265 <= self.dia < 280:
            self.prox_camp1 = 'Challenger League 2'
            self.quant_times1 = 24
            self.data1 = 266
            self.prizepool1 = 50000
            self.prox_camp2 = 'Qualifier IESF World'
            self.quant_times2 = 8
            self.data2 = 280
            self.prizepool2 = 'IESF World'
        elif 280 <= self.dia < 300:
            self.prox_camp1 = 'RES World'
            self.quant_times1 = 8
            self.data1 = 285
            self.prizepool1 = 250000
            self.prox_camp2 = 'Qualifier Thunderpick World'
            self.quant_times2 = 16
            self.data2 = 300
            self.prizepool2 = 'Thunderpick World'
        elif 300 <= self.dia < 320:
            self.prox_camp1 = 'IEM Rio'
            self.quant_times1 = 16
            self.data1 = 306
            self.prizepool1 = 250000
            self.prox_camp2 = 'IESF World'
            self.quant_times2 = 12
            self.data2 = 320
            self.prizepool2 = 240000
        elif 320 <= self.dia < 365:
            self.prox_camp1 = 'CBCS'
            self.quant_times1 = 8
            self.data1 = 325
            self.prizepool1 = 50000
            self.prox_camp2 = 'Major Xangai'
            self.quant_times2 = 24
            self.data2 = 338
            self.prizepool2 = 1250000

    def qualifieriemchengdu(self):
        self.times_camp = [{"name": "9z", "score": self.novez},{"name": "RED Canids", "score": self.redcanids},{"name": "MIBR", "score": self.mibr}]
        if self.dia == 10 and self.qualiiemchengdu == 1:
            self.camp = 'Qualifier IEM Changdu\n-\nOpening round'
            self.adversario = random.choice(self.times_camp)
            self.overadversario = self.adversario["score"]
            self.nomeadversario = self.adversario["name"]
            self.tipo_partida = 'MD3'
            self.jogar_partida()
        elif self.dia == 11 and self.qualiiemchengdu == 1:
            if self.winner == 1:
                self.upper = 1
                self.camp = 'Qualifier IEM Changdu\n-\nUpper final'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.times_camp.append(self.adversario)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.jogar_partida()
            elif self.winner == 0:
                self.upper = 0
                self.camp = 'Qualifier IEM Changdu\n-\nLower final'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.times_camp.append(self.adversario)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.jogar_partida()
        elif self.dia == 12 and self.qualiiemchengdu == 1:
            if self.winner == 1 and self.upper == 1:
                messagebox.showinfo('Info','Qualifier IEM Changdu\n-\nGrand final\n\nDia 13')
            elif self.winner == 1 and self.upper == 0:
                self.camp = 'Qualifier IEM Changdu\n-\nConsolidation final'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.times_camp.append(self.adversario)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.jogar_partida()
            elif self.winner == 0 and self.upper == 1:
                self.camp = 'Qualifier IEM Changdu\n-\nConsolidation final'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.times_camp.append(self.adversario)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.jogar_partida()
            elif self.winner == 0 and self.upper == 0:
                messagebox.showinfo('Info',f'{self.equipe} eliminado do Qualifier IEM Chengdu')
                self.qualiiemchengdu = 0
                self.atualizar_overs()
        elif self.dia == 13 and self.qualiiemchengdu == 1:
            if self.winner == 1:
                self.camp = 'Qualifier IEM Changdu\n-\nGrand final'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.times_camp.append(self.adversario)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.jogar_partida()
            elif self.winner == 0:
                messagebox.showinfo('Info',f'{self.equipe} eliminado do Qualifier IEM Chengdu')
                self.qualiiemchengdu = 0
                self.atualizar_overs()
        elif self.dia == 14 and self.qualiiemchengdu == 1:
            if self.winner == 1:
                messagebox.showinfo('Info',f'{self.equipe} classificado para a IEM Chengdu')
                self.qualiiemchengdu = 0
                self.iemchengdu = 1
                self.atualizar_overs()
            elif self.winner == 0:
                messagebox.showinfo('Info',f'{self.equipe} eliminado do Qualifier IEM Chengdu')
                self.qualiiemchengdu = 0
                self.iemchengdu = 0
                self.atualizar_overs()

    def rmr_major_copenhagen(self):
        self.times_camp = [{"name": "9z", "score": self.novez},{"name": "RED Canids", "score": self.redcanids},{"name": "MIBR", "score": self.mibr},{"name": "Imperial", "score": self.imperial},{"name": "FURIA", "score": self.furia},{"name": "Complexity", "score": self.complexity},{"name": "paiN", "score": self.pain},{"name": "M80", "score": self.m80},{"name": "Liquid", "score": self.liquid},{"name": "Legacy", "score": self.legacy},{"name": "Wildcard", "score": self.wildcard},{"name": "BOSS", "score": self.boss},{"name": "BESTIA", "score": self.bestia},{"name": "Party Astronauts", "score": self.partyastronauts},{"name": "Fluxo", "score": self.fluxo}]
        if self.dia == 18 and self.rmrmajorcopenhagen == 1:
            self.patrocinador1 = random.choice(self.patrocinadores1)
            self.patrocinador1_pagamento = 25000
            self.patrocinadores1.remove(self.patrocinador1)
            self.camp = 'RMR Major Copenhagen\n-\nRecord 0 - 0'
            self.adversario = random.choice(self.times_camp)
            self.overadversario = self.adversario["score"]
            self.nomeadversario = self.adversario["name"]
            self.tipo_partida = 'MD1'
            self.jogar_partida()
        elif self.dia == 19 and self.rmrmajorcopenhagen == 1:
            if self.winner == 1:
                self.camp = 'RMR Major Copenhagen\n-\nRecord 1 - 0'
                self.upper = 1
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD1'
                self.jogar_partida()
            elif self.winner == 0:
                self.camp = 'RMR Major Copenhagen\n-\nRecord 0 - 1'
                self.upper = 0
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.times_camp.append(self.adversario)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.jogar_partida()
        elif self.dia == 20 and self.rmrmajorcopenhagen == 1:
            if self.winner == 1 and self.upper == 1:
                self.camp = 'RMR Major Copenhagen\n-\nRecord 2 - 0'
                self.times_camp = [{"name": "9z", "score": self.novez},{"name": "FURIA", "score": self.furia},{"name": "Complexity", "score": self.complexity},{"name": "Imperial", "score": self.imperial},]
                if self.adversario in self.times_camp:
                    self.times_camp.remove(self.adversario)
                    self.adversario2 = random.choice(self.times_camp)
                else:
                    self.adversario2 = random.choice(self.times_camp)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.upper = 2
                self.jogar_partida()
            elif self.winner == 0 and self.upper == 1:
                self.camp = 'RMR Major Copenhagen\n-\nRecord 1 - 1'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.times_camp.append(self.adversario)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.jogar_partida()
            elif self.winner == 1 and self.upper == 0:
                self.camp = 'RMR Major Copenhagen\n-\nRecord 1 - 1'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.times_camp.append(self.adversario)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.upper = 1
                self.jogar_partida()
            elif self.winner == 0 and self.upper == 0:
                messagebox.showinfo('Info',f'{self.equipe} eliminado do RMR Major Copenhagen')
                self.rmrmajorcopenhagen = 0
                self.majorcopenhagen = 0
                self.atualizar_overs()
        elif self.dia == 21 and self.rmrmajorcopenhagen == 1:
            if self.winner == 1 and self.upper == 2:
                messagebox.showinfo('Info',f'{self.equipe} classificado para o Major Copenhagen')
                self.rmrmajorcopenhagen = 0
                self.majorcopenhagen = 1
                self.atualizar_overs()
            elif self.winner == 1 and self.upper == 1:
                self.camp = 'RMR Major Copenhagen\n-\nRecord 2 - 1'
                self.times_camp = [{"name": "9z", "score": self.novez},{"name": "FURIA", "score": self.furia},{"name": "Complexity", "score": self.complexity},{"name": "Imperial", "score": self.imperial},]
                if self.adversario in self.times_camp:
                    self.times_camp.remove(self.adversario)
                    self.adversario2 = random.choice(self.times_camp)
                else:
                    self.adversario2 = random.choice(self.times_camp)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.upper = 2
                self.jogar_partida()
            elif self.winner == 0 and self.upper == 2:
                self.camp = 'RMR Major Copenhagen\n-\nRecord 2 - 1'
                self.times_camp = [{"name": "9z", "score": self.novez},{"name": "FURIA", "score": self.furia},{"name": "Complexity", "score": self.complexity},{"name": "Imperial", "score": self.imperial},]
                if self.adversario in self.times_camp:
                    self.times_camp.remove(self.adversario)
                    self.adversario2 = random.choice(self.times_camp)
                else:
                    self.adversario2 = random.choice(self.times_camp)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.upper = 2
                self.jogar_partida() 
            elif self.winner == 0 and self.upper == 1:
                messagebox.showinfo('Info',f'{self.equipe} eliminado do RMR Major Copenhagen')
                self.rmrmajorcopenhagen = 0
                self.majorcopenhagen = 0
                self.atualizar_overs() 
        elif self.dia == 22 and self.rmrmajorcopenhagen == 1:
            if self.winner == 1:
                messagebox.showinfo('Info',f'{self.equipe} classificado para o Major Copenhagen')
                self.rmrmajorcopenhagen = 0
                self.majorcopenhagen = 1
                self.atualizar_overs()
            elif self.winner == 0:
                messagebox.showinfo('Info',f'{self.equipe} eliminado do RMR Major Copenhagen')
                self.rmrmajorcopenhagen = 0
                self.majorcopenhagen = 0
                self.atualizar_overs()   

    def qualifierproleague(self):
        self.times_camp = [{"name": "9z", "score": self.novez},{"name": "RED Canids", "score": self.redcanids},{"name": "MIBR", "score": self.mibr},{"name": "paiN", "score": self.pain},{"name": "Imperial", "score": self.imperial},{"name": "Legacy", "score": self.legacy},{"name": "BESTIA", "score": self.bestia}]
        if self.dia == 25 and self.qualiproleague == 1:
            self.camp = 'Qualifier Pro League\n-\nQuarter-finals'
            self.adversario = random.choice(self.times_camp)
            self.overadversario = self.adversario["score"]
            self.nomeadversario = self.adversario["name"]
            self.tipo_partida = 'MD3'
            self.jogar_partida()
        elif self.dia == 26 and self.qualiproleague == 1:
            if self.winner == 1:
                self.camp = 'Qualifier Pro League\n-\nSemi-finals'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.times_camp.append(self.adversario)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.jogar_partida()
            elif self.winner == 0:
                messagebox.showinfo('Info',f'{self.equipe} eliminado do Qualifier PRO LEAGUE')
                self.qualiproleague = 0
                self.proleague = 0
                self.atualizar_overs()
        elif self.dia == 27 and self.qualiproleague == 1:
            if self.winner == 1:
                messagebox.showinfo('Info',f'{self.equipe} classificado para a PRO LEAGUE')
                self.qualiproleague = 0
                self.proleague = -1
                self.atualizar_overs()
            elif self.winner == 0:
                messagebox.showinfo('Info',f'{self.equipe} eliminado do Qualifier PRO LEAGUE')
                self.qualiproleague = 0
                self.proleague = 0
                self.atualizar_overs()

    def playin_iem_katowice(self):
        self.times_camp = [{"name": "GamerLegion", "score": self.gamerlegion},{"name": "Spirit", "score": self.spirit},{"name": "HEROIC", "score": self.heroic},{"name": "Eternal Fire", "score": self.eternalfire},{"name": "ENCE", "score": self.ence},{"name": "BIG", "score": self.big},{"name": "M80", "score": self.m80},{"name": "The MongolZ", "score": self.themongolz},{"name": "Virtus.pro", "score": self.virtuspro},{"name": "FURIA", "score": self.furia},{"name": "Astralis", "score": self.astralis},{"name": "BetBoom", "score": self.betboom},{"name": "FlyQuest", "score": self.flyquest},{"name": "3DMAX", "score": self.tresdmax},{"name": "B8", "score": self.boito}]
        if self.dia == 33 and self.playiniemkatowice == 1:
            self.camp = 'Play-in IEM Katowice\n-\nOpening round'
            self.adversario = random.choice(self.times_camp)
            self.overadversario = self.adversario["score"]
            self.nomeadversario = self.adversario["name"]
            self.tipo_partida = 'MD1'
            self.jogar_partida()
        elif self.dia == 34 and self.playiniemkatowice == 1:
            if self.winner == 1:
                self.upper = 1
                self.camp = 'Play-in IEM Katowice\n-\nUpper round'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.times_camp.append(self.adversario)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.jogar_partida()
            elif self.winner == 0:
                self.upper = 0
                self.camp = 'Play-in IEM Katowice\n-\nLower round 1'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.times_camp.append(self.adversario)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.jogar_partida()
        elif self.dia == 35 and self.playiniemkatowice == 1:
            if self.winner == 1 and self.upper == 1:
                messagebox.showinfo('Info',f'{self.equipe} classificado para a IEM Katowice')
                self.playiniemkatowice = 0
                self.iemkatowice = 1
                self.atualizar_overs()
            elif self.winner == 1 and self.upper == 0:
                self.camp = 'Play-in IEM Katowice\n-\nLower round 2'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.times_camp.append(self.adversario)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.jogar_partida()
            elif self.winner == 0 and self.upper == 1:
                self.camp = 'Play-in IEM Katowice\n-\nLower round 2'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.times_camp.append(self.adversario)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.jogar_partida()
            elif self.winner == 0 and self.upper == 0:
                messagebox.showinfo('Info',f'{self.equipe} eliminado do Play-in IEM Katowice')
                self.playiniemkatowice = 0
                self.iemkatowice = 0
                self.atualizar_overs()
        elif self.dia == 36 and self.playiniemkatowice == 1:
            if self.winner == 1:
                messagebox.showinfo('Info',f'{self.equipe} classificado para a IEM Katowice')
                self.playiniemkatowice = 0
                self.iemkatowice = 1
                self.atualizar_overs()
            elif self.winner == 0:
                messagebox.showinfo('Info',f'{self.equipe} eliminado do Play-in IEM Katowice')
                self.playiniemkatowice = 0
                self.iemkatowice = 0
                self.atualizar_overs()

    def iem_katowice(self):
        self.times_camp = [{"name": "GamerLegion", "score": self.gamerlegion},{"name": "Spirit", "score": self.spirit},{"name": "HEROIC", "score": self.heroic},{"name": "Eternal Fire", "score": self.eternalfire},{"name": "MOUZ", "score": self.mouz},{"name": "monte", "score": self.monte},{"name": "Complexity", "score": self.complexity},{"name": "NAVI", "score": self.navi},{"name": "Virtus.pro", "score": self.virtuspro},{"name": "Falcons", "score": self.falcons},{"name": "G2", "score": self.g2},{"name": "Vitality", "score": self.vitality},{"name": "FlyQuest", "score": self.flyquest},{"name": "ENCE", "score": self.ence},{"name": "FaZe", "score": self.faze}] 
        if self.dia == 40 and self.iemkatowice == 1:
            self.camp = 'IEM Katowice\n-\nOpening round'
            self.adversario = random.choice(self.times_camp)
            self.overadversario = self.adversario["score"]
            self.nomeadversario = self.adversario["name"]
            self.tipo_partida = 'MD3'
            self.jogar_partida()
        elif self.dia == 41 and self.iemkatowice == 1:
            if self.winner == 1:
                self.upper = 1
                self.camp = 'IEM Katowice\n-\nUpper semi-finals'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.times_camp.append(self.adversario)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.jogar_partida()
            elif self.winner == 0:
                self.upper = 0
                self.camp = 'IEM Katowice\n-\nLower round 1'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.times_camp.append(self.adversario)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.jogar_partida()
        elif self.dia == 42 and self.iemkatowice == 1:
            if self.winner == 1 and self.upper == 1:
                self.upper = 2
                self.camp = 'IEM Katowice\n-\nUpper final'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.jogar_partida()
            elif self.winner == 1 and self.upper == 0:
                self.camp = 'IEM Katowice\n-\nLower semi-finals'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.times_camp.append(self.adversario)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.jogar_partida()
            elif self.winner == 0 and self.upper == 1:
                self.camp = 'IEM Katowice\n-\nLower semi-finals'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.jogar_partida()
            elif self.winner == 0 and self.upper == 0:
                self.iemkatowice == 0
                self.saldo += 10000 + self.patrocinador1_pagamento + self.patrocinador2_pagamento + self.patrocinador3_pagamento
                messagebox.showinfo('Info',f'{self.equipe} eliminado da IEM Katowice\nPosição: 13-16\nPrêmio: 10000\nBônus dos patrocinadores: {self.patrocinador1_pagamento+self.patrocinador2_pagamento+self.patrocinador3_pagamento}')
        elif self.dia == 43 and self.iemkatowice == 1:
            if self.upper == 2 and self.winner == 1:
                self.upper = 3
                messagebox.showinfo('Info',f'{self.equipe} classificado para as semi finais da IEM Katowice(dia 45)')
            elif self.upper == 2 and self.winner == 0:
                self.upper = -1
                messagebox.showinfo('Info',f'{self.equipe} classificado para as quartas de final da IEM Katowice(dia 44)')
            elif self.upper == 0 and self.winner == 1:
                self.upper = -1
                self.camp = 'IEM Katowice\n-\nLower final'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.jogar_partida()
            elif self.upper == 0 and self.winner == 0:
                self.iemkatowice == 0
                self.saldo += 16000 + self.patrocinador1_pagamento + self.patrocinador2_pagamento + self.patrocinador3_pagamento
                messagebox.showinfo('Info',f'{self.equipe} eliminado da IEM Katowice\nPosição: 9-12\nPrêmio: 16000\nBônus dos patrocinadores: {self.patrocinador1_pagamento+self.patrocinador2_pagamento+self.patrocinador3_pagamento}')
            elif self.upper == 1 and self.winner == 1:
                self.upper = -1
                self.camp = 'IEM Katowice\n-\nLower final'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.jogar_partida()
            elif self.upper == 1 and self.winner == 0:
                self.iemkatowice == 0
                self.saldo += 24000 + self.patrocinador1_pagamento + self.patrocinador2_pagamento + self.patrocinador3_pagamento
                messagebox.showinfo('Info',f'{self.equipe} eliminado da IEM Katowice\nPosição: 9-12\nPrêmio: 24000\nBônus dos patrocinadores: {self.patrocinador1_pagamento+self.patrocinador2_pagamento+self.patrocinador3_pagamento}')
        elif self.dia == 44 and self.iemkatowice == 1:
            if self.upper == -1 and self.winner == 0:
                self.iemkatowice == 0
                self.saldo += 24000 + self.patrocinador1_pagamento + self.patrocinador2_pagamento + self.patrocinador3_pagamento
                messagebox.showinfo('Info',f'{self.equipe} eliminado da IEM Katowice\nPosição: 7-8\nPrêmio: 24000\nBônus dos patrocinadores: {self.patrocinador1_pagamento+self.patrocinador2_pagamento+self.patrocinador3_pagamento}')
            elif self.upper == -1 and self.winner == 1:
                self.camp = 'IEM Katowice\n-\nQuarter-finals'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.jogar_partida()
        elif self.dia == 45 and self.iemkatowice == 1:
            if self.upper == -1 and self.winner == 1:
                self.camp = 'IEM Katowice\n-\nSemi-finals'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.jogar_partida()
            elif self.upper == -1 and self.winner == 0:
                self.iemkatowice == 0
                self.saldo += 40000 + self.patrocinador1_pagamento + self.patrocinador2_pagamento + self.patrocinador3_pagamento
                messagebox.showinfo('Info',f'{self.equipe} eliminado da IEM Katowice\nPosição: 5-6\nPrêmio: 40000\nBônus dos patrocinadores: {self.patrocinador1_pagamento+self.patrocinador2_pagamento+self.patrocinador3_pagamento}')
            elif self.upper == 3:
                self.camp = 'IEM Katowice\n-\nSemi-finals'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.jogar_partida()
        elif self.dia == 46 and self.iemkatowice == 1:
            if self.winner == 0:
                self.iemkatowice == 0
                self.saldo += 80000 + self.patrocinador1_pagamento + self.patrocinador2_pagamento + self.patrocinador3_pagamento
                messagebox.showinfo('Info',f'{self.equipe} eliminado da IEM Katowice\nPosição: 3-4\nPrêmio: 80000\nBônus dos patrocinadores: {self.patrocinador1_pagamento+self.patrocinador2_pagamento+self.patrocinador3_pagamento}')
            elif self.winner == 1:
                self.camp = 'IEM Katowice\n-\nGrand final'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD5'
                self.jogar_partida()
        elif self.dia == 47 and self.iemkatowice == 1:
            if self.winner == 1:
                self.iemkatowice == 0
                self.conquista1 = 'IEM Katowice'
                self.saldo += 400000 + self.patrocinador1_pagamento + self.patrocinador2_pagamento + self.patrocinador3_pagamento
                messagebox.showinfo('Info',f'{self.equipe.upper()} É CAMPEÃO DA IEM Katowice\nPosição: 1\nPrêmio: 400000\nBônus dos patrocinadores: {self.patrocinador1_pagamento+self.patrocinador2_pagamento+self.patrocinador3_pagamento}')
            elif self.winner == 0:
                self.iemkatowice == 0
                self.saldo += 180000 + self.patrocinador1_pagamento + self.patrocinador2_pagamento + self.patrocinador3_pagamento
                messagebox.showinfo('Info',f'{self.equipe} vice campeão da IEM Katowice\nPosição: 2\nPrêmio: 180000\nBônus dos patrocinadores: {self.patrocinador1_pagamento+self.patrocinador2_pagamento+self.patrocinador3_pagamento}')

    def qualifieriemdallas(self):
        self.times_camp = [{"name": "9z", "score": self.novez},{"name": "Imperial", "score": self.imperial},{"name": "FURIA", "score": self.furia}]
        if self.dia == 55 and self.qualiiemdallas == 1:
            self.camp = 'Qualifier IEM Dallas\n-\nOpening round'
            self.adversario = random.choice(self.times_camp)
            self.overadversario = self.adversario["score"]
            self.nomeadversario = self.adversario["name"]
            self.tipo_partida = 'MD3'
            self.jogar_partida()
        elif self.dia == 56 and self.qualiiemdallas == 1:
            if self.winner == 1:
                self.upper = 1
                self.camp = 'Qualifier IEM Dallas\n-\nUpper final'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.times_camp.append(self.adversario)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.jogar_partida()
            elif self.winner == 0:
                self.upper = 0
                self.camp = 'Qualifier IEM Dallas\n-\nLower final'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.times_camp.append(self.adversario)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.jogar_partida()
        elif self.dia == 57 and self.qualiiemdallas == 1:
            if self.winner == 1 and self.upper == 1:
                messagebox.showinfo('Info','Qualifier IEM Dallas\n-\nGrand final\n\nDia 58')
            elif self.winner == 1 and self.upper == 0:
                self.camp = 'Qualifier IEM Dallas\n-\nConsolidation final'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.times_camp.append(self.adversario)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.jogar_partida()
            elif self.winner == 0 and self.upper == 1:
                self.camp = 'Qualifier IEM Dallas\n-\nConsolidation final'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.times_camp.append(self.adversario)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.jogar_partida()
            elif self.winner == 0 and self.upper == 0:
                messagebox.showinfo('Info',f'{self.equipe} eliminado do Qualifier IEM Dallas')
                self.qualiiemdallas = 0
                self.iemdallas = 0
                self.atualizar_overs()
        elif self.dia == 58 and self.qualiiemdallas == 1:
            if self.winner == 1:
                self.camp = 'Qualifier IEM Dallas\n-\nGrand final'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.times_camp.append(self.adversario)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.jogar_partida()
            elif self.winner == 0:
                messagebox.showinfo('Info',f'{self.equipe} eliminado do Qualifier IEM Dallas')
                self.qualiiemdallas = 0
                self.iemdallas = 0
                self.atualizar_overs()
        elif self.dia == 59 and self.qualiiemdallas == 1:
            if self.winner == 1:
                messagebox.showinfo('Info',f'{self.equipe} classificado para a IEM Dallas')
                self.qualiiemdallas = 0
                self.iemdallas = 1
                self.atualizar_overs()
            elif self.winner == 0:
                messagebox.showinfo('Info',f'{self.equipe} eliminado do Qualifier IEM Dallas')
                self.qualiiemdallas = 0
                self.iemdallas = 0
                self.atualizar_overs()

    def res_latam(self):
        self.times_camp = [{"name": "9z", "score": self.novez},{"name": "RED Canids", "score": self.redcanids},{"name": "Fluxo", "score": self.fluxo},{"name": "paiN", "score": self.pain},{"name": "Imperial", "score": self.imperial},{"name": "Legacy", "score": self.legacy},{"name": "BESTIA", "score": self.bestia}]
        if self.dia == 67 and self.reslatam == 1:
            self.camp = 'RES LATAM\n-\nQuarter-finals'
            self.adversario = random.choice(self.times_camp)
            self.overadversario = self.adversario["score"]
            self.nomeadversario = self.adversario["name"]
            self.tipo_partida = 'MD3'
            self.jogar_partida()
        elif self.dia == 68 and self.reslatam == 1:
            if self.winner == 1:
                self.camp = 'RES LATAM\n-\nSemi-finals'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.jogar_partida()
            elif self.winner == 0:
                messagebox.showinfo('Info',f'{self.equipe} eliminado da RES LATAM\nPosição: 5-8')
                self.reslatam = 0
                self.resworld = 0
                self.atualizar_overs()
        elif self.dia == 69 and self.reslatam == 1:
            if self.winner == 1:
                self.camp = 'RES LATAM\n-\nGrand final'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.jogar_partida()
            elif self.winner == 0:
                messagebox.showinfo('Info',f'{self.equipe} eliminado da RES LATAM\nPosição: 3-4\nPrêmio: 5000')
                self.saldo += 5000
                self.reslatam = 0
                self.resworld = 0
                self.atualizar_overs()
        elif self.dia == 70 and self.reslatam == 1:
            if self.winner == 1:
                messagebox.showinfo('Info',f'{self.equipe.upper()} CAMPEÃO DA RES LATAM!\nClassificado para a RES WORLD\nPosição: 1\nPrêmio: 25000')
                self.saldo += 25000
                self.reslatam = 0
                self.resworld = 1
                self.atualizar_overs()
            elif self.winner == 0:
                messagebox.showinfo('Info',f'{self.equipe} eliminado da RES LATAM\nClassificado para a RES WORLD\nPosição: 2\nPrêmio: 15000')
                self.saldo += 15000
                self.reslatam = 0
                self.resworld = 1
                self.atualizar_overs()

    def qualifierchallengerleague(self):
        self.times_camp = [{"name": "Sharks", "score": self.sharks},{"name": "BESTIA", "score": self.bestia},{"name": "Fluxo", "score": self.fluxo}]
        if self.dia == 77 and self.qualichallengerleague == 1:
            self.camp = 'Qualifier Challenger League\n-\nQuarter-finals'
            self.adversario = random.choice(self.times_camp)
            self.overadversario = self.adversario["score"]
            self.nomeadversario = self.adversario["name"]
            self.tipo_partida = 'MD3'
            self.jogar_partida()
        elif self.dia == 78 and self.qualichallengerleague == 1:
            if self.winner == 1:
                self.camp = 'Qualifier Challenger League\n-\nSemi-finals'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.times_camp.append(self.adversario)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.jogar_partida()
            elif self.winner == 0:
                messagebox.showinfo('Info',f'{self.equipe} eliminado do Qualifier Challenger LEAGUE')
                self.qualichallengerleague = 0
                self.challengerleague = 0
                self.atualizar_overs()
        elif self.dia == 79 and self.qualichallengerleague == 1:
            if self.winner == 1:
                messagebox.showinfo('Info',f'{self.equipe} classificado para a Challenger LEAGUE\n*Inscrição para a Challenger League proibe a inscrição para a PRO LEAGUE')
                self.qualichallengerleague = 0
                self.challengerleague = -1
                self.atualizar_overs()
            elif self.winner == 0:
                messagebox.showinfo('Info',f'{self.equipe} eliminado do Qualifier Challenger LEAGUE')
                self.qualichallengerleague = 0
                self.challengerleague = 0
                self.atualizar_overs()

    def yalla_compass(self):
        if self.yalla == 0:
            self.times_camp = [{"name": "The MongolZ", "score": self.themongolz},{"name": "NIP", "score": self.nip},{"name": "Astralis", "score": self.astralis},{"name": "HEROIC", "score": self.heroic},{"name": "Sashi", "score": self.sashi}]
            self.yalla = 1        
        if self.dia == 90 and self.yallacomppass == 1:
            self.camp = 'YaLLa Compass\n-\nGroup stage 1'
            self.adversario = random.choice(self.times_camp)
            self.overadversario = self.adversario["score"]
            self.nomeadversario = self.adversario["name"]
            self.tipo_partida = 'MD1'
            self.jogar_partida()
        elif self.dia == 91 and self.yallacomppass == 1:
            if self.winner == 1:
                self.vitorias += 1
                self.camp = 'YaLLa Compass\n-\nGroup stage 2'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD1'
                self.jogar_partida()
            elif self.winner == 0:
                self.camp = 'YaLLa Compass\n-\nGroup stage 2'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD1'
                self.jogar_partida()
        elif self.dia == 92 and self.yallacomppass == 1:
            if self.winner == 1:
                self.vitorias += 1
                self.camp = 'YaLLa Compass\n-\nGroup stage 3'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD1'
                self.jogar_partida()
            elif self.winner == 0:
                self.camp = 'YaLLa Compass\n-\nGroup stage 3'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD1'
                self.jogar_partida()
        elif self.dia == 93 and self.yallacomppass == 1:
            if self.winner == 1:
                self.vitorias += 1
                self.camp = 'YaLLa Compass\n-\nGroup stage 4'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD1'
                self.jogar_partida()
            elif self.winner == 0:
                self.camp = 'YaLLa Compass\n-\nGroup stage 4'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD1'
                self.jogar_partida()
        elif self.dia == 94 and self.yallacomppass == 1:
            if self.winner == 1:
                self.vitorias += 1
                self.camp = 'YaLLa Compass\n-\nGroup stage 5'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD1'
                self.jogar_partida()
            elif self.winner == 0:
                self.camp = 'YaLLa Compass\n-\nGroup stage 5'
                self.times_camp.remove(self.adversario)
                self.adversario2 = random.choice(self.times_camp)
                self.adversario = self.adversario2
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD1'
                self.jogar_partida()
        elif self.dia == 95 and self.yallacomppass == 1:
            if self.winner == 1:
                self.vitorias += 1
            if self.vitorias < 3:
                self.yallacomppass = 0
                if self.vitorias <= 1:
                    messagebox.showinfo('Info',f'{self.equipe} eliminado da YaLLa Compass\nPosição: 11-12\nPrêmio: 8000\nBônus dos patrocinadores: {self.patrocinador1_pagamento+self.patrocinador2_pagamento+self.patrocinador3_pagamento}')
                    self.saldo += 8000 + (self.patrocinador1_pagamento+self.patrocinador2_pagamento+self.patrocinador3_pagamento)
                elif self.vitorias == 2:
                    messagebox.showinfo('Info',f'{self.equipe} eliminado da YaLLa Compass\nPosição: 7-8\nPrêmio: 8000\nBônus dos patrocinadores: {self.patrocinador1_pagamento+self.patrocinador2_pagamento+self.patrocinador3_pagamento}')
                    self.saldo += 8000 + (self.patrocinador1_pagamento+self.patrocinador2_pagamento+self.patrocinador3_pagamento)
                self.vitorias = 0
                self.yalla = 0
            else:
                self.times_camp = [{"name": "BetBoom", "score": self.betboom},{"name": "Furia", "score": self.furia},{"name": "Fnatic", "score": self.fnatic}]
                if self.vitorias >= 4:
                    self.upper = 1
                    messagebox.showinfo('Info',f'{self.equipe} classificado para as semi-finals\nDia: 96')
                    self.adversario2 = ''
                else:
                    self.upper = 0
                    self.camp = 'YaLLa Compass\n-\nQuartes-finals'
                    self.adversario2 = random.choice(self.times_camp)
                    self.adversario = self.adversario2
                    self.overadversario = self.adversario["score"]
                    self.nomeadversario = self.adversario["name"]
                    self.tipo_partida = 'MD3'
                    self.jogar_partida()
        elif self.dia == 96 and self.yallacomppass == 1:
            if self.winner == 0 and self.upper == 0:
                self.yallacomppass = 0
                self.vitorias = 0
                self.yalla = 0
                messagebox.showinfo('Info',f'{self.equipe} eliminado da YaLLa Compass\nPosição: 5-6\nPrêmio: 20000\nBônus dos patrocinadores: {self.patrocinador1_pagamento+self.patrocinador2_pagamento+self.patrocinador3_pagamento}')
                self.saldo += 20000 + (self.patrocinador1_pagamento+self.patrocinador2_pagamento+self.patrocinador3_pagamento)
            else:
                self.times_camp = [{"name": "The MongolZ", "score": self.themongolz},{"name": "Astralis", "score": self.astralis},{"name": "NIP", "score": self.nip}]
                self.camp = 'YaLLa Compass\n-\nSemi-finals'
                self.adversario3 = random.choice(self.times_camp)
                self.adversario = self.adversario3
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD3'
                self.jogar_partida()
        elif self.dia == 97 and self.yallacomppass == 1:
            if self.winner == 0:
                self.yallacomppass = 0
                self.vitorias = 0
                messagebox.showinfo('Info',f'{self.equipe} eliminado da YaLLa Compass\nPosição: 3-4\nPrêmio: 28000\nBônus dos patrocinadores: {self.patrocinador1_pagamento+self.patrocinador2_pagamento+self.patrocinador3_pagamento}')
                self.saldo += 28000 + (self.patrocinador1_pagamento+self.patrocinador2_pagamento+self.patrocinador3_pagamento)
                self.yalla = 0
            elif self.winner == 1:
                self.times_camp = [{"name": "FURIA", "score": self.furia},{"name": "BetBoom", "score": self.betboom},{"name": "NIP", "score": self.nip}]
                self.camp = 'YaLLa Compass\n-\nGrand final'
                self.adversario = random.choice(self.times_camp)
                while self.adversario == self.adversario2 or self.adversario == self.adversario3:
                    self.times_camp.remove(self.adversario)
                    self.adversario = random.choice(self.times_camp)
                self.overadversario = self.adversario["score"]
                self.nomeadversario = self.adversario["name"]
                self.tipo_partida = 'MD5'
                self.jogar_partida()
        elif self.dia == 98 and self.yallacomppass == 1:
            if self.winner == 0:
                self.yallacomppass = 0
                self.vitorias = 0
                self.yalla = 0
                messagebox.showinfo('Info',f'{self.equipe} eliminado da YaLLa Compass\nPosição: 2\nPrêmio: 56000\nBônus dos patrocinadores: {self.patrocinador1_pagamento+self.patrocinador2_pagamento+self.patrocinador3_pagamento}')
                self.saldo += 56000 + (self.patrocinador1_pagamento+self.patrocinador2_pagamento+self.patrocinador3_pagamento)
            elif self.winner == 1:
                self.yallacomppass = 0
                self.vitorias = 0
                self.yalla = 0
                messagebox.showinfo('Info',f'{self.equipe.upper()} CAMPEÃO DA YaLLa Compass\nPosição: 1\nPrêmio: 200000\nBônus dos patrocinadores: {self.patrocinador1_pagamento+self.patrocinador2_pagamento+self.patrocinador3_pagamento}')
                self.saldo += 200000 + (self.patrocinador1_pagamento+self.patrocinador2_pagamento+self.patrocinador3_pagamento)        

    def jogar_partida(self):
        self.button_campeonatos.grid_forget()
        self.button_avancar2.grid_forget()
        self.button_treinamento.grid_forget()
        self.button_transferencias.grid_forget()
        self.label_saldo.grid_forget()
        self.label_dia.grid_forget()
        self.label_patrocinadores.grid_forget()
        self.frame_patrocinadores.grid_forget()
        self.frame_conquistas.grid_forget()
        self.frame_nomes.grid_forget()
        self.frame_overalls.grid_forget()
        self.frame_posicoes.grid_forget()
        self.frame_ranking.grid_forget()
        self.frame_rating.grid_forget()
        self.label_conquistas.grid_forget()
        self.label_rating.grid_forget()
        self.label_ranking.grid_forget()
        self.label_posicoes.grid_forget()
        self.label_nomes.grid_forget()
        self.label_overalls.grid_forget()
        self.num_mapa = 0
        self.mapas_equipe = 0
        self.mapas_adversario = 0
        self.pontos_adversariom1  = 0
        self.pontos_adversariom2 = 0
        self.pontos_adversariom3 = 0
        self.pontos_adversariom4 = 0
        self.pontos_adversariom5 = 0
        self.pontos_equipem1 = 0
        self.pontos_equipem2 = 0
        self.pontos_equipem3 = 0
        self.pontos_equipem4 = 0
        self.pontos_equipem5 = 0
        self.picks_bans()

    def picks_bans(self):
        self.mapas = ['Dust2','Mirage','Nuke','Anubis','Ancient','Vertigo','Inferno']
        if self.tipo_partida == 'MD3':
            self.remov1 = ''
            self.label_campeonato = Label(text=f'{self.camp}',font=('Roboto',18),bg='#222331',fg='white')
            self.label_campeonato.grid(column=0,row=0,pady=(24,24),padx=(24,24))
            self.frame_partida = Frame(bg='#1a1b26',height=250,width=350)
            self.frame_partida.grid(column=1,row=0,pady=(48,12),padx=(24,24))
            self.label_partida = Label(text=f'{self.equipe} VS {self.nomeadversario}\n\nTipo {self.tipo_partida}\n\nMapa 1:\n\nMapa 2:\n\nMapa 3:',font=('Roboto',18),bg='#1a1b26',fg='white')
            self.label_partida.grid(column=1,row=0,pady=(48,12),padx=(24,24))
            self.label_picksbans = Label(text=f'',font=('Roboto',18),bg='#222331',fg='white')
            self.label_picksbans.grid(column=2,row=0,pady=(48,12),padx=(24,24))
            self.label_pickorban = Label(text=f'Remova um mapa:',font=('Roboto',18),bg='#222331',fg='white')
            self.label_pickorban.grid(column=1,row=1,pady=(48,12),padx=(24,24))
            self.button_inferno = Button(text='INFERNO',font=('Roboto',18),bg='#1a1b26',fg='white',width=8,command=lambda: [self.picks_bans2('Inferno')])
            self.button_inferno.grid(column=1,row=2,pady=(12,12),padx=(24,24))
            self.button_anubis = Button(text='ANUBIS',font=('Roboto',18),bg='#1a1b26',fg='white',width=8,command=lambda: [self.picks_bans2('Anubis')])
            self.button_anubis.grid(column=1,row=3,pady=(12,12),padx=(24,24))
            self.button_mirage = Button(text='MIRAGE',font=('Roboto',18),bg='#1a1b26',fg='white',width=8,command=lambda: [self.picks_bans2('Mirage')])
            self.button_mirage.grid(column=1,row=4,pady=(12,12),padx=(24,24))
            self.button_ancient = Button(text='ANCIENT',font=('Roboto',18),bg='#1a1b26',fg='white',width=8,command=lambda: [self.picks_bans2('Ancient')])
            self.button_ancient.grid(column=1,row=5,pady=(12,12),padx=(24,24))
            self.button_nuke = Button(text='NUKE',font=('Roboto',18),bg='#1a1b26',fg='white',width=8,command=lambda: [self.picks_bans2('Nuke')])
            self.button_nuke.grid(column=2,row=2,pady=(12,12),padx=(24,24))
            self.button_dust2 = Button(text='DUST2',font=('Roboto',18),bg='#1a1b26',fg='white',width=8,command=lambda: [self.picks_bans2('Dust2')])
            self.button_dust2.grid(column=2,row=3,pady=(12,12),padx=(24,24))
            self.button_vertigo = Button(text='VERTIGO',font=('Roboto',18),bg='#1a1b26',fg='white',width=8,command=lambda: [self.picks_bans2('Vertigo')])
            self.button_vertigo.grid(column=2,row=4,pady=(12,12),padx=(24,24))
        elif self.tipo_partida == 'MD1':
            self.remov1 = ''
            self.label_campeonato = Label(text=f'{self.camp}',font=('Roboto',18),bg='#222331',fg='white')
            self.label_campeonato.grid(column=0,row=0,pady=(24,24),padx=(24,24))
            self.frame_partida = Frame(bg='#1a1b26',height=250,width=350)
            self.frame_partida.grid(column=1,row=0,pady=(48,12),padx=(24,24))
            self.label_partida = Label(text=f'{self.equipe} VS {self.nomeadversario}\n\nTipo {self.tipo_partida}\n\nMapa:',font=('Roboto',18),bg='#1a1b26',fg='white')
            self.label_partida.grid(column=1,row=0,pady=(48,12),padx=(24,24))
            self.label_picksbans = Label(text=f'',font=('Roboto',18),bg='#222331',fg='white')
            self.label_picksbans.grid(column=2,row=0,pady=(48,12),padx=(24,24))
            self.label_pickorban = Label(text=f'Remova um mapa:',font=('Roboto',18),bg='#222331',fg='white')
            self.label_pickorban.grid(column=1,row=1,pady=(48,12),padx=(24,24))
            self.button_inferno = Button(text='INFERNO',font=('Roboto',18),bg='#1a1b26',fg='white',width=8,command=lambda: [self.picks_bans2('Inferno')])
            self.button_inferno.grid(column=1,row=2,pady=(12,12),padx=(24,24))
            self.button_anubis = Button(text='ANUBIS',font=('Roboto',18),bg='#1a1b26',fg='white',width=8,command=lambda: [self.picks_bans2('Anubis')])
            self.button_anubis.grid(column=1,row=3,pady=(12,12),padx=(24,24))
            self.button_mirage = Button(text='MIRAGE',font=('Roboto',18),bg='#1a1b26',fg='white',width=8,command=lambda: [self.picks_bans2('Mirage')])
            self.button_mirage.grid(column=1,row=4,pady=(12,12),padx=(24,24))
            self.button_ancient = Button(text='ANCIENT',font=('Roboto',18),bg='#1a1b26',fg='white',width=8,command=lambda: [self.picks_bans2('Ancient')])
            self.button_ancient.grid(column=1,row=5,pady=(12,12),padx=(24,24))
            self.button_nuke = Button(text='NUKE',font=('Roboto',18),bg='#1a1b26',fg='white',width=8,command=lambda: [self.picks_bans2('Nuke')])
            self.button_nuke.grid(column=2,row=2,pady=(12,12),padx=(24,24))
            self.button_dust2 = Button(text='DUST2',font=('Roboto',18),bg='#1a1b26',fg='white',width=8,command=lambda: [self.picks_bans2('Dust2')])
            self.button_dust2.grid(column=2,row=3,pady=(12,12),padx=(24,24))
            self.button_vertigo = Button(text='VERTIGO',font=('Roboto',18),bg='#1a1b26',fg='white',width=8,command=lambda: [self.picks_bans2('Vertigo')])
            self.button_vertigo.grid(column=2,row=4,pady=(12,12),padx=(24,24))
        elif self.tipo_partida == 'MD5':
            self.remov1 = ''
            self.label_campeonato = Label(text=f'{self.camp}',font=('Roboto',18),bg='#222331',fg='white')
            self.label_campeonato.grid(column=0,row=0,pady=(24,24),padx=(24,24))
            self.frame_partida = Frame(bg='#1a1b26',height=250,width=350)
            self.frame_partida.grid(column=1,row=0,pady=(48,12),padx=(24,24))
            self.label_partida = Label(text=f'{self.equipe} VS {self.nomeadversario}\n\nTipo {self.tipo_partida}\nMapa 1:\nMapa 2:\nMapa 3:\nMapa 4:\nMapa 5:',font=('Roboto',18),bg='#1a1b26',fg='white')
            self.label_partida.grid(column=1,row=0,pady=(48,12),padx=(24,24))
            self.label_picksbans = Label(text=f'',font=('Roboto',18),bg='#222331',fg='white')
            self.label_picksbans.grid(column=2,row=0,pady=(48,12),padx=(24,24))
            self.label_pickorban = Label(text=f'Remova um mapa:',font=('Roboto',18),bg='#222331',fg='white')
            self.label_pickorban.grid(column=1,row=1,pady=(48,12),padx=(24,24))
            self.button_inferno = Button(text='INFERNO',font=('Roboto',18),bg='#1a1b26',fg='white',width=8,command=lambda: [self.picks_bans2('Inferno')])
            self.button_inferno.grid(column=1,row=2,pady=(12,12),padx=(24,24))
            self.button_anubis = Button(text='ANUBIS',font=('Roboto',18),bg='#1a1b26',fg='white',width=8,command=lambda: [self.picks_bans2('Anubis')])
            self.button_anubis.grid(column=1,row=3,pady=(12,12),padx=(24,24))
            self.button_mirage = Button(text='MIRAGE',font=('Roboto',18),bg='#1a1b26',fg='white',width=8,command=lambda: [self.picks_bans2('Mirage')])
            self.button_mirage.grid(column=1,row=4,pady=(12,12),padx=(24,24))
            self.button_ancient = Button(text='ANCIENT',font=('Roboto',18),bg='#1a1b26',fg='white',width=8,command=lambda: [self.picks_bans2('Ancient')])
            self.button_ancient.grid(column=1,row=5,pady=(12,12),padx=(24,24))
            self.button_nuke = Button(text='NUKE',font=('Roboto',18),bg='#1a1b26',fg='white',width=8,command=lambda: [self.picks_bans2('Nuke')])
            self.button_nuke.grid(column=2,row=2,pady=(12,12),padx=(24,24))
            self.button_dust2 = Button(text='DUST2',font=('Roboto',18),bg='#1a1b26',fg='white',width=8,command=lambda: [self.picks_bans2('Dust2')])
            self.button_dust2.grid(column=2,row=3,pady=(12,12),padx=(24,24))
            self.button_vertigo = Button(text='VERTIGO',font=('Roboto',18),bg='#1a1b26',fg='white',width=8,command=lambda: [self.picks_bans2('Vertigo')])
            self.button_vertigo.grid(column=2,row=4,pady=(12,12),padx=(24,24))

    def picks_bans2(self, mapa):
        if self.tipo_partida == 'MD3':
            self.remov1 = mapa
            self.mapas.remove(self.remov1)
            self.remov2 = random.choice(self.mapas)
            self.mapas.remove(self.remov2)
            self.label_picksbans.config(text=f'1. {self.equipe} removed {self.remov1}\n2. {self.nomeadversario} removed {self.remov2}')
            self.label_pickorban.config(text='Escolha um mapa')
            if self.remov1 == 'Inferno':
                self.button_inferno.grid_forget()
            elif self.remov1 == 'Nuke':
                self.button_nuke.grid_forget()
            elif self.remov1 == 'Mirage':
                self.button_mirage.grid_forget()
            elif self.remov1 == 'Ancient':
                self.button_ancient.grid_forget()
            elif self.remov1 == 'Vertigo':
                self.button_vertigo.grid_forget()
            elif self.remov1 == 'Dust2':
                self.button_dust2.grid_forget()
            elif self.remov1 == 'Anubis':
                self.button_anubis.grid_forget()
            if self.remov2 == 'Inferno':
                self.button_inferno.grid_forget()
            elif self.remov2 == 'Nuke':
                self.button_nuke.grid_forget()
            elif self.remov2 == 'Mirage':
                self.button_mirage.grid_forget()
            elif self.remov2 == 'Ancient':
                self.button_ancient.grid_forget()
            elif self.remov2 == 'Vertigo':
                self.button_vertigo.grid_forget()
            elif self.remov2 == 'Dust2':
                self.button_dust2.grid_forget()
            elif self.remov2 == 'Anubis':
                self.button_anubis.grid_forget()    
            self.button_anubis.config(command=lambda: [self.picks_bans3('Anubis')])
            self.button_nuke.config(command=lambda: [self.picks_bans3('Nuke')])
            self.button_vertigo.config(command=lambda: [self.picks_bans3('Vertigo')])
            self.button_inferno.config(command=lambda: [self.picks_bans3('Inferno')])
            self.button_dust2.config(command=lambda: [self.picks_bans3('Dust2')])
            self.button_ancient.config(command=lambda: [self.picks_bans3('Ancient')])
            self.button_mirage.config(command=lambda: [self.picks_bans3('Mirage')])
        elif self.tipo_partida == 'MD1':
            self.remov1 = mapa
            self.mapas.remove(self.remov1)
            self.remov2 = random.choice(self.mapas)
            self.mapas.remove(self.remov2)
            self.label_picksbans.config(text=f'1. {self.equipe} removed {self.remov1}\n2. {self.nomeadversario} removed {self.remov2}')
            if self.remov1 == 'Inferno':
                self.button_inferno.grid_forget()
            elif self.remov1 == 'Nuke':
                self.button_nuke.grid_forget()
            elif self.remov1 == 'Mirage':
                self.button_mirage.grid_forget()
            elif self.remov1 == 'Ancient':
                self.button_ancient.grid_forget()
            elif self.remov1 == 'Vertigo':
                self.button_vertigo.grid_forget()
            elif self.remov1 == 'Dust2':
                self.button_dust2.grid_forget()
            elif self.remov1 == 'Anubis':
                self.button_anubis.grid_forget()
            if self.remov2 == 'Inferno':
                self.button_inferno.grid_forget()
            elif self.remov2 == 'Nuke':
                self.button_nuke.grid_forget()
            elif self.remov2 == 'Mirage':
                self.button_mirage.grid_forget()
            elif self.remov2 == 'Ancient':
                self.button_ancient.grid_forget()
            elif self.remov2 == 'Vertigo':
                self.button_vertigo.grid_forget()
            elif self.remov2 == 'Dust2':
                self.button_dust2.grid_forget()
            elif self.remov2 == 'Anubis':
                self.button_anubis.grid_forget()    
            self.button_anubis.config(command=lambda: [self.picks_bans3('Anubis')])
            self.button_nuke.config(command=lambda: [self.picks_bans3('Nuke')])
            self.button_vertigo.config(command=lambda: [self.picks_bans3('Vertigo')])
            self.button_inferno.config(command=lambda: [self.picks_bans3('Inferno')])
            self.button_dust2.config(command=lambda: [self.picks_bans3('Dust2')])
            self.button_ancient.config(command=lambda: [self.picks_bans3('Ancient')])
            self.button_mirage.config(command=lambda: [self.picks_bans3('Mirage')])
        elif self.tipo_partida == 'MD5':
            self.remov1 = mapa
            self.mapas.remove(self.remov1)
            self.remov2 = random.choice(self.mapas)
            self.mapas.remove(self.remov2)
            self.label_picksbans.config(text=f'1. {self.equipe} removed {self.remov1}\n2. {self.nomeadversario} removed {self.remov2}')
            self.label_pickorban.config(text='Escolha um mapa')
            if self.remov1 == 'Inferno':
                self.button_inferno.grid_forget()
            elif self.remov1 == 'Nuke':
                self.button_nuke.grid_forget()
            elif self.remov1 == 'Mirage':
                self.button_mirage.grid_forget()
            elif self.remov1 == 'Ancient':
                self.button_ancient.grid_forget()
            elif self.remov1 == 'Vertigo':
                self.button_vertigo.grid_forget()
            elif self.remov1 == 'Dust2':
                self.button_dust2.grid_forget()
            elif self.remov1 == 'Anubis':
                self.button_anubis.grid_forget()
            if self.remov2 == 'Inferno':
                self.button_inferno.grid_forget()
            elif self.remov2 == 'Nuke':
                self.button_nuke.grid_forget()
            elif self.remov2 == 'Mirage':
                self.button_mirage.grid_forget()
            elif self.remov2 == 'Ancient':
                self.button_ancient.grid_forget()
            elif self.remov2 == 'Vertigo':
                self.button_vertigo.grid_forget()
            elif self.remov2 == 'Dust2':
                self.button_dust2.grid_forget()
            elif self.remov2 == 'Anubis':
                self.button_anubis.grid_forget()    
            self.button_anubis.config(command=lambda: [self.picks_bans3('Anubis')])
            self.button_nuke.config(command=lambda: [self.picks_bans3('Nuke')])
            self.button_vertigo.config(command=lambda: [self.picks_bans3('Vertigo')])
            self.button_inferno.config(command=lambda: [self.picks_bans3('Inferno')])
            self.button_dust2.config(command=lambda: [self.picks_bans3('Dust2')])
            self.button_ancient.config(command=lambda: [self.picks_bans3('Ancient')])
            self.button_mirage.config(command=lambda: [self.picks_bans3('Mirage')])

    def picks_bans3(self, mapa):
        if self.tipo_partida == 'MD3':
            self.pick1 = mapa
            self.mapas.remove(self.pick1)
            self.pick2 = random.choice(self.mapas)
            self.mapas.remove(self.pick2)
            self.label_partida.config(text=f'{self.equipe} VS {self.nomeadversario}\n\nTipo {self.tipo_partida}\n\nMapa 1: {self.pick1}\n\nMapa 2: {self.pick2}\n\nMapa 3:')
            self.label_picksbans.config(text=f'1. {self.equipe} removed {self.remov1}\n2. {self.nomeadversario} removed {self.remov2}\n3. {self.equipe} picked {self.pick1}\n4. {self.nomeadversario} picked {self.pick2}')
            self.label_pickorban.config(text='Remova um mapa')
            if self.pick1 == 'Inferno':
                self.button_inferno.grid_forget()
            elif self.pick1 == 'Nuke':
                self.button_nuke.grid_forget()
            elif self.pick1 == 'Mirage':
                self.button_mirage.grid_forget()
            elif self.pick1 == 'Ancient':
                self.button_ancient.grid_forget()
            elif self.pick1 == 'Vertigo':
                self.button_vertigo.grid_forget()
            elif self.pick1 == 'Dust2':
                self.button_dust2.grid_forget()
            elif self.pick1 == 'Anubis':
                self.button_anubis.grid_forget()
            if self.pick2 == 'Inferno':
                self.button_inferno.grid_forget()
            elif self.pick2 == 'Nuke':
                self.button_nuke.grid_forget()
            elif self.pick2 == 'Mirage':
                self.button_mirage.grid_forget()
            elif self.pick2 == 'Ancient':
                self.button_ancient.grid_forget()
            elif self.pick2 == 'Vertigo':
                self.button_vertigo.grid_forget()
            elif self.pick2 == 'Dust2':
                self.button_dust2.grid_forget()
            elif self.pick2 == 'Anubis':
                self.button_anubis.grid_forget()
            self.button_anubis.config(command=lambda: [self.picks_bans4('Anubis')])
            self.button_nuke.config(command=lambda: [self.picks_bans4('Nuke')])
            self.button_vertigo.config(command=lambda: [self.picks_bans4('Vertigo')])
            self.button_inferno.config(command=lambda: [self.picks_bans4('Inferno')])
            self.button_dust2.config(command=lambda: [self.picks_bans4('Dust2')])
            self.button_ancient.config(command=lambda: [self.picks_bans4('Ancient')])
            self.button_mirage.config(command=lambda: [self.picks_bans4('Mirage')])
        elif self.tipo_partida == 'MD1':
            self.pick1 = mapa
            self.mapas.remove(self.pick1)
            self.pick2 = random.choice(self.mapas)
            self.mapas.remove(self.pick2)
            self.label_picksbans.config(text=f'1. {self.equipe} removed {self.remov1}\n2. {self.nomeadversario} removed {self.remov2}\n3. {self.equipe} removed {self.pick1}\n4. {self.nomeadversario} removed {self.pick2}')
            self.label_pickorban.config(text='Remova um mapa')
            if self.pick1 == 'Inferno':
                self.button_inferno.grid_forget()
            elif self.pick1 == 'Nuke':
                self.button_nuke.grid_forget()
            elif self.pick1 == 'Mirage':
                self.button_mirage.grid_forget()
            elif self.pick1 == 'Ancient':
                self.button_ancient.grid_forget()
            elif self.pick1 == 'Vertigo':
                self.button_vertigo.grid_forget()
            elif self.pick1 == 'Dust2':
                self.button_dust2.grid_forget()
            elif self.pick1 == 'Anubis':
                self.button_anubis.grid_forget()
            if self.pick2 == 'Inferno':
                self.button_inferno.grid_forget()
            elif self.pick2 == 'Nuke':
                self.button_nuke.grid_forget()
            elif self.pick2 == 'Mirage':
                self.button_mirage.grid_forget()
            elif self.pick2 == 'Ancient':
                self.button_ancient.grid_forget()
            elif self.pick2 == 'Vertigo':
                self.button_vertigo.grid_forget()
            elif self.pick2 == 'Dust2':
                self.button_dust2.grid_forget()
            elif self.pick2 == 'Anubis':
                self.button_anubis.grid_forget()
            self.button_anubis.config(command=lambda: [self.picks_bans4('Anubis')])
            self.button_nuke.config(command=lambda: [self.picks_bans4('Nuke')])
            self.button_vertigo.config(command=lambda: [self.picks_bans4('Vertigo')])
            self.button_inferno.config(command=lambda: [self.picks_bans4('Inferno')])
            self.button_dust2.config(command=lambda: [self.picks_bans4('Dust2')])
            self.button_ancient.config(command=lambda: [self.picks_bans4('Ancient')])
            self.button_mirage.config(command=lambda: [self.picks_bans4('Mirage')])
        elif self.tipo_partida == 'MD5':
            self.pick1 = mapa
            self.mapas.remove(self.pick1)
            self.pick2 = random.choice(self.mapas)
            self.mapas.remove(self.pick2)
            self.label_partida.config(text=f'{self.equipe} VS {self.nomeadversario}\n\nTipo {self.tipo_partida}\nMapa 1: {self.pick1}\nMapa 2: {self.pick2}\nMapa 3:\nMapa 4:\nMapa 5:')
            self.label_picksbans.config(text=f'1. {self.equipe} removed {self.remov1}\n2. {self.nomeadversario} removed {self.remov2}\n3. {self.equipe} picked {self.pick1}\n4. {self.nomeadversario} picked {self.pick2}')
            if self.pick1 == 'Inferno':
                self.button_inferno.grid_forget()
            elif self.pick1 == 'Nuke':
                self.button_nuke.grid_forget()
            elif self.pick1 == 'Mirage':
                self.button_mirage.grid_forget()
            elif self.pick1 == 'Ancient':
                self.button_ancient.grid_forget()
            elif self.pick1 == 'Vertigo':
                self.button_vertigo.grid_forget()
            elif self.pick1 == 'Dust2':
                self.button_dust2.grid_forget()
            elif self.pick1 == 'Anubis':
                self.button_anubis.grid_forget()
            if self.pick2 == 'Inferno':
                self.button_inferno.grid_forget()
            elif self.pick2 == 'Nuke':
                self.button_nuke.grid_forget()
            elif self.pick2 == 'Mirage':
                self.button_mirage.grid_forget()
            elif self.pick2 == 'Ancient':
                self.button_ancient.grid_forget()
            elif self.pick2 == 'Vertigo':
                self.button_vertigo.grid_forget()
            elif self.pick2 == 'Dust2':
                self.button_dust2.grid_forget()
            elif self.pick2 == 'Anubis':
                self.button_anubis.grid_forget()
            self.button_anubis.config(command=lambda: [self.picks_bans4('Anubis')])
            self.button_nuke.config(command=lambda: [self.picks_bans4('Nuke')])
            self.button_vertigo.config(command=lambda: [self.picks_bans4('Vertigo')])
            self.button_inferno.config(command=lambda: [self.picks_bans4('Inferno')])
            self.button_dust2.config(command=lambda: [self.picks_bans4('Dust2')])
            self.button_ancient.config(command=lambda: [self.picks_bans4('Ancient')])
            self.button_mirage.config(command=lambda: [self.picks_bans4('Mirage')])


    def picks_bans4(self, mapa):
        if self.tipo_partida == 'MD3':
            self.remov3 = mapa
            self.mapas.remove(self.remov3)
            self.remov4 = random.choice(self.mapas)
            self.mapas.remove(self.remov4)
            self.pick3 = random.choice(self.mapas)
            self.label_partida.config(text=f'{self.equipe} VS {self.nomeadversario}\n\nTipo {self.tipo_partida}\n\nMapa 1: {self.pick1}\n\nMapa 2: {self.pick2}\n\nMapa 3: {self.pick3}')
            self.label_picksbans.config(text=f'1. {self.equipe} removed {self.remov1}\n2. {self.nomeadversario} removed {self.remov2}\n3. {self.equipe} picked {self.pick1}\n4. {self.nomeadversario} picked {self.pick2}\n5. {self.equipe} removed {self.remov3}\n6. {self.nomeadversario} removed {self.remov4}\n7. {self.pick3} was left over')
            self.button_ancient.grid_forget()
            self.button_nuke.grid_forget()
            self.button_mirage.grid_forget()
            self.button_anubis.grid_forget()
            self.button_dust2.grid_forget()
            self.button_vertigo.grid_forget()
            self.button_inferno.grid_forget()
            self.label_pickorban.grid_forget()
            self.button_jogar = Button(text='JOGAR',font=('Roboto',18),bg='#1a1b26',fg='#44feb8',width=8,command=self.partida)
            self.button_jogar.grid(column=1,row=1,pady=(48,12),padx=(24,24))
        elif self.tipo_partida == 'MD1':
            self.remov3 = mapa
            self.mapas.remove(self.remov3)
            self.remov4 = random.choice(self.mapas)
            self.mapas.remove(self.remov4)
            self.pick3 = random.choice(self.mapas)
            self.label_partida.config(text=f'{self.equipe} VS {self.nomeadversario}\n\nTipo {self.tipo_partida}\n\nMapa: {self.pick3}')
            self.label_picksbans.config(text=f'1. {self.equipe} removed {self.remov1}\n2. {self.nomeadversario} removed {self.remov2}\n3. {self.equipe} removed {self.pick1}\n4. {self.nomeadversario} removed {self.pick2}\n5. {self.equipe} removed {self.remov3}\n6. {self.nomeadversario} removed {self.remov4}\n7. {self.pick3} was left over')
            self.button_ancient.grid_forget()
            self.button_nuke.grid_forget()
            self.button_mirage.grid_forget()
            self.button_anubis.grid_forget()
            self.button_dust2.grid_forget()
            self.button_vertigo.grid_forget()
            self.button_inferno.grid_forget()
            self.label_pickorban.grid_forget()
            self.button_jogar = Button(text='JOGAR',font=('Roboto',18),bg='#1a1b26',fg='#44feb8',width=8,command=self.partida)
            self.button_jogar.grid(column=1,row=1,pady=(48,12),padx=(24,24))
        elif self.tipo_partida == 'MD5':
            self.remov3 = mapa
            self.mapas.remove(self.remov3)
            self.remov4 = random.choice(self.mapas)
            self.mapas.remove(self.remov4)
            self.pick3 = random.choice(self.mapas)
            self.label_partida.config(text=f'{self.equipe} VS {self.nomeadversario}\n\nTipo {self.tipo_partida}\nMapa 1: {self.pick1}\nMapa 2: {self.pick2}\nMapa 3: {self.remov3}\nMapa 4: {self.remov4}\nMapa 5: {self.pick3}')
            self.label_picksbans.config(text=f'1. {self.equipe} removed {self.remov1}\n2. {self.nomeadversario} removed {self.remov2}\n3. {self.equipe} picked {self.pick1}\n4. {self.nomeadversario} picked {self.pick2}\n5. {self.equipe} picked {self.remov3}\n6. {self.nomeadversario} picked {self.remov4}\n7. {self.pick3} was left over')
            self.button_ancient.grid_forget()
            self.button_nuke.grid_forget()
            self.button_mirage.grid_forget()
            self.button_anubis.grid_forget()
            self.button_dust2.grid_forget()
            self.button_vertigo.grid_forget()
            self.button_inferno.grid_forget()
            self.label_pickorban.grid_forget()
            self.button_jogar = Button(text='JOGAR',font=('Roboto',18),bg='#1a1b26',fg='#44feb8',width=8,command=self.partida)
            self.button_jogar.grid(column=1,row=1,pady=(48,12),padx=(24,24))


    def partida(self):
        self.button_jogar.grid_forget()
        self.label_picksbans.grid_forget()
        self.button_avancar_partida = Button(text='AVANÇAR',font=('Roboto',18),bg='#1a1b26',fg='#44feb8',width=8,command=self.partida_res)
        self.button_avancar_partida.grid(column=1,row=2,pady=(48,12),padx=(24,24))
        if self.tipo_partida == 'MD3':
            self.label_resultado = Label(text=f'{self.equipe} {self.mapas_equipe} - {self.mapas_adversario} {self.nomeadversario}\n\nMapa 1: {self.pontos_equipem1} - {self.pontos_adversariom1}\n\nMapa 2: {self.pontos_equipem2} - {self.pontos_adversariom2}\n\nMapa 3: {self.pontos_equipem3} - {self.pontos_adversariom3}',font=('Roboto',18),bg='#222331',fg='white')
            self.label_resultado.grid(column=1,row=1,pady=(48,12),padx=(24,24))
        elif self.tipo_partida == 'MD1':
            self.label_resultado = Label(text=f'{self.equipe} {self.mapas_equipe} - {self.mapas_adversario} {self.nomeadversario}\n\nMapa: {self.pontos_equipem1} - {self.pontos_adversariom1}',font=('Roboto',18),bg='#222331',fg='white')
            self.label_resultado.grid(column=1,row=1,pady=(48,12),padx=(24,24))
        elif self.tipo_partida == 'MD5':
            self.label_resultado = Label(text=f'{self.equipe} {self.mapas_equipe} - {self.mapas_adversario} {self.nomeadversario}\n\nMapa 1: {self.pontos_equipem1} - {self.pontos_adversariom1}\nMapa 2: {self.pontos_equipem2} - {self.pontos_adversariom2}\nMapa 3: {self.pontos_equipem3} - {self.pontos_adversariom3}\nMapa 4: {self.pontos_equipem4} - {self.pontos_adversariom4}\nMapa 5: {self.pontos_equipem5} - {self.pontos_adversariom5}',font=('Roboto',18),bg='#222331',fg='white')
            self.label_resultado.grid(column=1,row=1,pady=(48,12),padx=(24,24))

    def partida_res(self):
        if self.tipo_partida == 'MD3':
            self.num_mapa += 1
            self.chance = self.over_equipe - self.overadversario
            self.res = randint(1,100)
            if self.num_mapa == 1:
                if self.res < (50 + self.chance):
                    self.pontos_equipem1 = 13
                    self.pontos_adversariom1 = randint(0,11)
                    self.mapas_equipe += 1
                else:
                    self.pontos_adversariom1 = 13
                    self.pontos_equipem1 = randint(0,11)
                    self.mapas_adversario += 1
            elif self.num_mapa == 2:
                if self.res < (50 + self.chance):
                    self.pontos_equipem2 = 13
                    self.pontos_adversariom2 = randint(0,11)
                    self.mapas_equipe += 1
                else:
                    self.pontos_adversariom2 = 13
                    self.pontos_equipem2 = randint(0,11)
                    self.mapas_adversario += 1
                if self.mapas_equipe == 2:
                    self.winner = 1
                    self.button_avancar_partida.config(command=self.voltar_menu_part)
                elif self.mapas_adversario == 2:
                    self.winner = 0
                    self.button_avancar_partida.config(command=self.voltar_menu_part)
            elif self.num_mapa == 3 and self.mapas_equipe == 1 and self.mapas_adversario == 1:
                if self.res < (50 + self.chance):
                    self.pontos_equipem3 = 13
                    self.pontos_adversariom3 = randint(0,11)
                    self.mapas_equipe += 1
                    self.winner = 1
                else:
                    self.pontos_adversariom3 = 13
                    self.pontos_equipem3 = randint(0,11)
                    self.mapas_adversario += 1
                    self.winner = 0
                self.button_avancar_partida.config(command=self.voltar_menu_part)
            self.label_resultado.config(text=f'{self.equipe} {self.mapas_equipe} - {self.mapas_adversario} {self.nomeadversario}\n\nMapa 1: {self.pontos_equipem1} - {self.pontos_adversariom1}\n\nMapa 2: {self.pontos_equipem2} - {self.pontos_adversariom2}\n\nMapa 3: {self.pontos_equipem3} - {self.pontos_adversariom3}')

        elif self.tipo_partida == 'MD1':
            self.num_mapa += 1
            self.chance = self.over_equipe - self.overadversario
            self.res = randint(1,100)
            if self.num_mapa == 1:
                if self.res < (50 + self.chance):
                    self.pontos_equipem1 = 13
                    self.pontos_adversariom1 = randint(0,11)
                    self.mapas_equipe += 1
                    self.winner = 1
                else:
                    self.pontos_adversariom1 = 13
                    self.pontos_equipem1 = randint(0,11)
                    self.mapas_adversario += 1
                    self.winner = 0
                self.button_avancar_partida.config(command=self.voltar_menu_part)
            self.label_resultado.config(text=f'{self.equipe} {self.mapas_equipe} - {self.mapas_adversario} {self.nomeadversario}\n\nMapa: {self.pontos_equipem1} - {self.pontos_adversariom1}')

        elif self.tipo_partida == 'MD5':
            self.num_mapa += 1
            self.chance = self.over_equipe - self.overadversario
            self.res = randint(1,100)
            if self.num_mapa == 1:
                if self.res < (50 + self.chance):
                    self.pontos_equipem1 = 13
                    self.pontos_adversariom1 = randint(0,11)
                    self.mapas_equipe += 1
                else:
                    self.pontos_adversariom1 = 13
                    self.pontos_equipem1 = randint(0,11)
                    self.mapas_adversario += 1
            elif self.num_mapa == 2:
                if self.res < (50 + self.chance):
                    self.pontos_equipem2 = 13
                    self.pontos_adversariom2 = randint(0,11)
                    self.mapas_equipe += 1
                else:
                    self.pontos_adversariom2 = 13
                    self.pontos_equipem2 = randint(0,11)
                    self.mapas_adversario += 1
            elif self.num_mapa == 3:
                if self.res < (50 + self.chance):
                    self.pontos_equipem3 = 13
                    self.pontos_adversariom3 = randint(0,11)
                    self.mapas_equipe += 1
                    self.winner = 1
                else:
                    self.pontos_adversariom3 = 13
                    self.pontos_equipem3 = randint(0,11)
                    self.mapas_adversario += 1
                    self.winner = 0
                if self.mapas_equipe == 3:
                    self.winner = 1
                    self.button_avancar_partida.config(command=self.voltar_menu_part)
                    self.button_avancar_partida.config(command=self.voltar_menu_part)
                elif self.mapas_adversario == 3:
                    self.winner = 0
                    self.button_avancar_partida.config(command=self.voltar_menu_part)
                    self.button_avancar_partida.config(command=self.voltar_menu_part)
            elif self.num_mapa == 4:
                if self.res < (50 + self.chance):
                    self.pontos_equipem4 = 13
                    self.pontos_adversariom4 = randint(0,11)
                    self.mapas_equipe += 1
                    self.winner = 1
                else:
                    self.pontos_adversariom4 = 13
                    self.pontos_equipem4 = randint(0,11)
                    self.mapas_adversario += 1
                    self.winner = 0
                if self.mapas_equipe == 3:
                    self.winner = 1
                    self.button_avancar_partida.config(command=self.voltar_menu_part)
                    self.button_avancar_partida.config(command=self.voltar_menu_part)
                elif self.mapas_adversario == 3:
                    self.winner = 0
                    self.button_avancar_partida.config(command=self.voltar_menu_part)
                    self.button_avancar_partida.config(command=self.voltar_menu_part)
            elif self.num_mapa == 5:
                if self.res < (50 + self.chance):
                    self.pontos_equipem5 = 13
                    self.pontos_adversariom5 = randint(0,11)
                    self.mapas_equipe += 1
                    self.winner = 1
                else:
                    self.pontos_adversariom5 = 13
                    self.pontos_equipem5 = randint(0,11)
                    self.mapas_adversario += 1
                    self.winner = 0
                if self.mapas_equipe == 3:
                    self.winner = 1
                    self.button_avancar_partida.config(command=self.voltar_menu_part)
                    self.button_avancar_partida.config(command=self.voltar_menu_part)
                elif self.mapas_adversario == 3:
                    self.winner = 0
                    self.button_avancar_partida.config(command=self.voltar_menu_part)
                    self.button_avancar_partida.config(command=self.voltar_menu_part)
            self.label_resultado.config(text=f'{self.equipe} {self.mapas_equipe} - {self.mapas_adversario} {self.nomeadversario}\n\nMapa 1: {self.pontos_equipem1} - {self.pontos_adversariom1}\nMapa 2: {self.pontos_equipem2} - {self.pontos_adversariom2}\nMapa 3: {self.pontos_equipem3} - {self.pontos_adversariom3}\nMapa 4: {self.pontos_equipem4} - {self.pontos_adversariom4}\nMapa 5: {self.pontos_equipem5} - {self.pontos_adversariom5}')

    def voltar_menu_part(self):
        self.label_campeonato.grid_forget()
        self.label_resultado.grid_forget()
        self.frame_partida.grid_forget()
        self.label_partida.grid_forget()
        self.button_avancar_partida.grid_forget()
        self.menu()


if __name__ == "__main__":
    root = Tk()
    root.title("game")
    root.config(bg='#222331')
    root.geometry('1366x768')
    app = app(root)
    root.mainloop()