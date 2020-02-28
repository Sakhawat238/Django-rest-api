from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from Table.models import Subject
from method7.serializers import SubjectSerializer
from django.shortcuts import get_object_or_404


# viewset + router is an easy approach to built api

class SubjectViewSet(viewsets.ViewSet):
    def list(self,request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def create(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        subject = get_object_or_404(Subject, pk=pk)
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)


    def update(self, request, pk=None):
        subject = get_object_or_404(Subject, pk=pk)
        serializer = SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        subject = get_object_or_404(Subject, pk=pk)
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)