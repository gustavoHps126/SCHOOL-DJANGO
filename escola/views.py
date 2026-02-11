from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializar, MatriculaSerializer,ListaMatriculasCursoSerializer, ListaMatriculasEstudantesSerializer
from rest_framework import generics, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from escola.throttles import MatriculaAnonRateThrottle

class EstudanteViewsSet(viewsets.ModelViewSet):
    """
    Docstring for MatriculaViewSet
    -Endpoint para CRUD de estudantes
    
    Campos de ordenção:
    -nome(string):Permite ordenar os resultados por nome

    Campos de pesquisa:
    -nome(string):Permite a pesquisa pelo nome do aluno
    -cpf(string):Permite a pesquisa pelo cpf do aluno

    Parametros: 
    -pk(int):Identificador primario do objeto, deve ser um numero inteiro.
    -nome(String):Nome do aluno a ser procurado/cadastrado
    -email(string):Email do aluno a ser procurado/cadastrado
    -cpf(string):Cpf com - e . 
    -datadeNascimento(stringDate)Data de nascimento do aluno procurado/cadastrado
    -celular(string):Numero de telefone

    Metodos:
    -Get
    -Post
    -Put
    -Patch
    -Delete
    """
    queryset = Estudante.objects.all().order_by("id")
    serializer_class = EstudanteSerializer


class CursoViewsSet(viewsets.ModelViewSet):
    """
    Docstring for MatriculaViewSet
    -Endpoint para CRUD de cursos

    Metodos:
    -Get
    -Post
    -Put
    -Patch
    -Delete
    """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializar

class MatriculaViewSet(viewsets.ModelViewSet):
    """
    Docstring for MatriculaViewSet:
    Endpoind do CRUD de matriculas

    Metodos:
    -Get
    -Post

    Throttle Classes:
    -MatriculaAnonRateThrottle:Limite o numero de usos para usuarios não logados
    -UserRateThrottle:Limite o numero de usos para usuarios logados
    """
    queryset = Matricula.objects.all().order_by("id")
    serializer_class = MatriculaSerializer
    throttle_classes = [UserRateThrottle,MatriculaAnonRateThrottle]
    http_method_names = ["get", "post"]



class ListaMatriculaEstudante(generics.ListAPIView):
    """
    Docstring for ListaMatriculaEstudante:
    -Lista de matriculas por id de estudante

    Parametros:
    -pk(int):Identificador primario do objeto, deve ser um numero inteiro.

    Metodos:
    -Get
    """
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by("id")
        return queryset

    serializer_class = ListaMatriculasEstudantesSerializer

class ListaMatriculaCurso(generics.ListAPIView):
    """
    Docstring for ListaMatriculaCurso:
    -Lista de matriculas por id de estudante

    Parametros:
    -pk(int):Identificador primario do objeto, deve ser um numero inteiro.

    """
    def get_queryset(self):
        queryset = Matricula.objects.filter(curos_id=self.kwargs['pk']).order_by("id")
        return queryset

    serializer_class = ListaMatriculasCursoSerializer