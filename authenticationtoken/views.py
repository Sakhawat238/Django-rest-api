from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, mixins
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from method6.serializers import SubjectSerializer, Subject
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework.authtoken.models import Token


# GenrateToken fucntion generate token for all existing users
# signals.py will generate token for newly created user
# we can get token for an existing user by calling '/api-token-auth/' url; method: post; json fields: username, password
# For clients to authenticate, the token key should be included in the Authorization HTTP header. 
# The key should be prefixed by the string literal "Token", with whitespace separating the two strings. For example:
# Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b


def GenerateToken(request):
    for user in User.objects.all():
        Token.objects.get_or_create(user=user)
    return HttpResponse(status=200)


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def SubjectTokenAuthViewset(request):
    if request.method == 'GET':
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    if request.method == 'POST':
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubjectDetailTokenAuthGenericview(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    lookup_field = 'id'

    def get(self, request, id):
        return self.retrieve(request)

    def put(self, request, id):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request)
