class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome


    def __str__(self):
        return f'{self._nome} - {self.ano} : {self._likes} LIKES'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao


    def __str__(self):
       return f'{self._nome} - {self.ano} - {self.duracao}min : {self._likes} LIKES'
        

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temp : {self._likes} LIKES'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas


    def __getitem__(self, item):
        return self._programas[item]
    
    @property
    def listagem(self):
        return self._programas

    
    def __len__(self):
        return len(self._programas)
        
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2016, 3)


tmep.dar_likes()
demolidor.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()

vingadores.dar_likes()
vingadores.dar_likes()

atlanta.dar_likes()
atlanta.dar_likes()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]

playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'tamanho do playlist: {len(playlist_fim_de_semana)}')

len(playlist_fim_de_semana)

for programa in playlist_fim_de_semana:
    print(programa)

