from rest_framework import serializers
from school_api.models import Student, Course, Registration

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']    # Different way, same result


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'                                        # Different way, same result


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        exclude = []                                              # Different way, same result


