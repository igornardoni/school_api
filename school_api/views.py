from rest_framework import viewsets
from school_api.models import Student, Course, Registration
from school_api.serializer import StudentSerializer, CourseSerializer, RegistrationSerializer


class StudentsViewSet(viewsets.ModelViewSet):
    """" Exibindo todos alunos e alunas """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """" Exibindo todos os cursos """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class RegistrationViewSet(viewsets.ModelViewSet):
    """Exibindo todas as matrículas"""
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


    
