from django.http import JsonResponse, HttpResponse
from method3.serializers import SubjectSeralizer, Subject
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def SubjectViewset(request):
    if request.method == 'GET':
        subjects = Subject.objects.all()
        serializer = SubjectSeralizer(subjects, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SubjectSeralizer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



@csrf_exempt
def SubjectDetailViewset(request, id):
    try:
        subject = Subject.objects.get(id=id)
    except Subject.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SubjectSeralizer(subject)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SubjectSeralizer(subject, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        subject.delete()
        return HttpResponse(status=204)