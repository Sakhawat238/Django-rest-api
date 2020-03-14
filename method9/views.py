from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from Table.models import Subject, Student, Teacher
from method9.serializers import SubjectSerializer, StudentSerializer, TeacherSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'


    # Right now this StudentViewset+Router provides urls for students information only.
    # For example, http://localhost:8000/api/m9/students/1/ will provide a specific student's information.
    # Suppose we want an url http://localhost:8000/api/m9/students/1/teacher/ which will give that student's teacher information.
    # We can implement this by using rest_framework action decorator.
    @action(detail=True, methods=['GET'])
    def teacher(self, request, id=None):
        student = self.get_object()
        serializer = TeacherSerializer(student.teacher)
        return Response(serializer.data, status= status.HTTP_200_OK)


    # We can also use other methods and perform create, update, delete operations.