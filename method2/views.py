from Table.models import School
from method2.serializers import SchoolSerializer
from django.http import JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


def SchoolList(requset):
    school = School.objects.all()
    serializer = SchoolSerializer(school, many=True)
    return JsonResponse(serializer.data, safe=False)
    

def SchoolDetails(request,id):
    school = School.objects.get(id=id)
    serializer = SchoolSerializer(school)
    return JsonResponse(serializer.data, safe=False)


# use csrf_exempt decorator to bypass csrf verification

@csrf_exempt
def SchoolCreate(request):
    stream = io.BytesIO(request.body)
    data = JSONParser().parse(stream)
    serializer = SchoolSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        school = serializer.save() 
    return JsonResponse({'id':school.id})


@csrf_exempt
def SchoolUpdate(request, id):
    school = School.objects.get(id=id)
    stream = io.BytesIO(request.body)
    data = JSONParser().parse(stream)
    serializer = SchoolSerializer(school,data=data)
    if serializer.is_valid(raise_exception=True):
        school = serializer.save() 
    return JsonResponse({'id':school.id})
