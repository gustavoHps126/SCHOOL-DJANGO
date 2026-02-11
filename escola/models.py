#As classes a seguir são os modelos que serão utilizados para as apis

#Após alterar o arquivo models sempre se lembrar de fazer as migrações com os comandos
    #python manage.py makemigrations  Para fazer a migração
    # e python manage.py migrate para confirmar
    
from django.db import models
class Estudante(models.Model):
    nome = models.CharField(max_length = 100)
    email = models.EmailField(blank = False, max_length = 30)
    cpf = models.CharField(max_length = 11)
    dataNascimento = models.DateField(null=True, blank=True)
    celular = models.CharField(max_length = 14)
    #Como a uma classe sempre precisa retornar algo é de boa pratica 
        #retornar algo, no caso abaixo o nome
    def __str__(self):
        return self.nome

class Curso(models.Model):
    NIVEL = (
        ('B','Básico'),
        ('I','Intermediário'),
        ('A','Avançado'),
    ) 
    #Tupla com as opções a disponivels para o campo "nivel", a letra
        #sozinha é o que vai ser armazenado já o valor ao lado é o
        #que vai ser equivalente a letra
    codigo = models.CharField(max_length=10, null=True, blank=True)
    descricao = models.CharField(max_length = 100, blank =True)
    nivel = models.CharField(max_length = 1, choices = NIVEL, blank = False, null = False, default = 'B')

    def __str__(self):
        return self.codigo


class Matricula(models.Model):
    PERIODO = (
        ('M','Matutino'),
        ('V','Vespertino'),
        ('N','Noturno'),
    ) 

    estudante = models.ForeignKey(Estudante,on_delete= models.CASCADE)
    curso = models.ForeignKey(Curso,on_delete= models.CASCADE)
    periodo = models.CharField(max_length = 1, choices = PERIODO, blank = False, null = False, default = 'M')

