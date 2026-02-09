from escola.models import Estudante, Curso, Matricula
from escola.serializers import EstudanteSerializer, CursoSerializar, MatriculaSerializer,ListaMatriculasCursoSerializer, ListaMatriculasEstudantesSerializer
from rest_framework import generics, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from escola.throttles import MatriculaAnonRateThrottle

class EstudanteViewsSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all().order_by("id")
    serializer_class = EstudanteSerializer


class CursoViewsSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializar

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all().order_by("id")
    serializer_class = MatriculaSerializer
    throttle_classes = [UserRateThrottle,MatriculaAnonRateThrottle]
    http_method_names = ["get", "post"]



class ListaMatriculaEstudante(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by("id")
        return queryset

    serializer_class = ListaMatriculasEstudantesSerializer

class ListaMatriculaCurso(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matricula.objects.filter(curos_id=self.kwargs['pk']).order_by("id")
        return queryset

    serializer_class = ListaMatriculasCursoSerializer