from rest_framework import serializers
from Table.models import Teacher, Subject, School, Student


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    school = serializers.SerializerMethodField()
    subjects = serializers.SerializerMethodField()
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'age', 'school','subjects']
    def get_school(self, obj):
        school_ser = SchoolSerializer(obj.school)
        return school_ser.data
    def get_subjects(self, obj):
        subject_ser = SubjectSerializer(obj.subject.all(), many=True)
        return subject_ser.data



class StudentSerializer(serializers.ModelSerializer):
    teacher = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'teacher']
    def get_teacher(self, obj):
        teacher_ser = TeacherSerializer(obj.teacher)
        return teacher_ser.data