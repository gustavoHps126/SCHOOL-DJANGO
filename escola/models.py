#As classes a seguir são os modelos que serão utilizados para as apis

#Após alterar o arquivo models sempre se lembrar de fazer as migrações com os comandos
    #python manage.py makemigrations  Para fazer a migração
    # e python manage.py migrate para confirmar
    
from django.db import models
class Estudante(models.Model):
    nome = models.CharField(max_length=100),
    email = models.EmailField(blank=False, max_length=150),
    cpf = models.CharField(max_length=11),
    dataNascimento = models.DateField(),
    celular = models.CharField(max_length=14)
    #Como a uma classe sempre precisa retornar algo é de boa pratica 
        #retornar algo, no caso abaixo o nome
    def __str__(self):
        return self.nome


class Curso(models.Model):
    #Tupla com as opções a disponivels para o campo "nivel", a letra
        #sozinha é o que vai ser armazenado já o valor ao lado é o
        #que vai ser equivalente a letra
    NIVEL = (
        ('B','Básico'),
        ('I','Intermendiário'),
        ('A','Avançado'),
    )

    codigo = model.CharField(max_length=10),
    descricao = model.CharField(max_length=100,blank=False),
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.codigo
