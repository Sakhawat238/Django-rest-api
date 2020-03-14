from rest_framework import serializers
from Table.models  import School, Subject, Teacher, Student


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        # usually student serializer will provide one level of data
        # so it will return id for teacher field
        # but if we want to get teacher details we can specify depth = 1
        # if we further want to retrieve data we can increase depth value
        # note that, we do not need to define other serializer classes for that
        depth = 2 


class TeacherSerializer(serializers.ModelSerializer):
    # When we get all teachers list, we also want details of their students
    # So we declared a property 'students' in Teacher model
    # Then we used StudentSerializer to serialize students data
    # StudentSerializer must be defined beforehand.
    students = StudentSerializer(many=True)
    class Meta:
        model = Teacher
        fields = ['name','age', 'school', 'subject', 'students']