from rest_framework import generics
from Table.models import Student
from method11.serializers import StudentSerializer

class StudentListAPIView(generics.ListAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    
class StudentRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = StudentSerializer
    queryset = Student.objects.all()