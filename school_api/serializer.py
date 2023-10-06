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


class RegistrationListSerializerByStudent(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.descricao')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Registration
        fields = ['course', 'periodo']

    @staticmethod
    def get_periodo(obj):
        return obj.get_periodo_display()


class RegistrationListSerializerByCourse(serializers.ModelSerializer):
    student_nome = serializers.ReadOnlyField(source='student.nome')

    class Meta:
        model = Registration
        fields = ['student_nome']





