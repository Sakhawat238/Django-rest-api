from Table.models import Subject
from method1.serializers import SubjectSerializer
from django.http import JsonResponse
import io
from rest_framework.parsers import JSONParser


def SubjectList(requset):
    subjects = Subject.objects.all()
    serializer = SubjectSerializer(subjects, many=True)
    return JsonResponse(serializer.data, safe=False)
    

def SubjectDetails(request,id):
    subject = Subject.objects.get(id=id)
    serializer = SubjectSerializer(subject)
    return JsonResponse(serializer.data, safe=False)


def SubjectCreate(request):
    stream = io.BytesIO(request.body)
    data = JSONParser().parse(stream)
    serializer = SubjectSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        subject = serializer.save() 
    return JsonResponse({'id':subject.id})


def SubjectUpdate(request, id):
    subject = Subject.objects.get(id=id)
    stream = io.BytesIO(request.body)
    data = JSONParser().parse(stream)
    serializer = SubjectSerializer(subject,data=data)
    if serializer.is_valid(raise_exception=True):
        subject = serializer.save() 
    return JsonResponse({'id':subject.id})