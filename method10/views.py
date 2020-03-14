# from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from method10.serializers import School, Subject, Teacher, Student, SchoolSerializer, SubjectSerializer, TeacherSerializer,StudentSerializer


class StudentNestedViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'


class TeacherNestedViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_field = 'id'
