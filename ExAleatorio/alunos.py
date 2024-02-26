class Alunos:
    def __init__(self,nome,idade,media):
        self.nome = nome
        self.idade = idade
        self.media = media
    def __str__(self):
        return f'Nome: {self.nome}\nIdade: {self.idade}\nMedia: {self.media}'