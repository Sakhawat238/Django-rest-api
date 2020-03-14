from django.shortcuts import get_object_or_404
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
        fields = ['id','name','age', 'school', 'subject', 'students']


    # Here we implemented create mtehod to perform complex opration.
    # While creating a teacher we will add subjects (many to many field)
    # We also create students and associate them with this teacher.
    # A request body will look like this.
    # {
    #     "name": "Joynal Abedin",
    #     "age": 35,
    #     "school": 1,
    #     "subject": [3,5],
    #     "students": [
    #           {
    #               "name": "Arman",
    #               "roll": 6
    #           }
    #       ]
    # }
    def create(self, validated_data):
        subjects = validated_data.pop('subject')
        students = validated_data.pop('students')
        teacher = Teacher.objects.create(**validated_data)
        for subject in subjects:
            teacher.subject.add(subject)
        teacher.save()
        for student in students:
            Student.objects.create(**student, teacher=teacher)
        return teacher


    # Here we update a teacher + his subjects
    # {
    #     "name": "Joynal Abedin",
    #     "age": 55,
    #     "school": 1,
    #     "subject": [2,6],
    #     "students": []
    # }
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.school = validated_data.get('school')
        instance.subject.clear()
        subjects = validated_data.pop('subject')
        for subject in subjects:
            instance.subject.add(subject)
        instance.save()
        return instance
