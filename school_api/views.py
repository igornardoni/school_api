from rest_framework import viewsets, generics
from school_api.models import Student, Course, Registration
from school_api.serializer import (StudentSerializer, CourseSerializer, RegistrationSerializer,
                                   RegistrationListSerializerByStudent,
                                   RegistrationListSerializerByCourse)
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class StudentsViewSet(viewsets.ModelViewSet):
    """ Exibindo todos alunos e alunas """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CourseViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os cursos """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class RegistrationViewSet(viewsets.ModelViewSet):
    """Exibindo todas as matrículas"""
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class StudentRegistrationList(generics.ListAPIView):
    """Listando as matrículas de um aluno ou aluna"""
    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs['pk'])
        return queryset
    serializer_class = RegistrationListSerializerByStudent
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CourseRegistrationList(generics.ListAPIView):
    """Listando as matrículas de um curso"""
    def get_queryset(self):
        queryset = Registration.objects.filter(course_id=self.kwargs['pk'])
        return queryset
    serializer_class = RegistrationListSerializerByCourse
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


