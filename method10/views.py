from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from method10.serializers import School, Subject, Teacher, Student, SchoolSerializer, SubjectSerializer, TeacherSerializer,StudentSerializer



class StudentNestedView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class TeacherNestedView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class SubjectApiview(APIView):
    def get(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SubjectDetailApiview(APIView):
    def get_object(self, id):   
        try:
            return Subject.objects.get(id=id)
        except Subject.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        subject = self.get_object(id)
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)

    def put(self, request, id):
        subject = self.get_object(id)
        serializer = SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        subject = self.get_object(id)
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)