from rest_framework import generics, mixins
from method6.serializers import SubjectSerializer, Subject


#  here we have used generic api view and model mixins

class SubjectGenericview(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class SubjectDetailGenericview(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()
    lookup_field = 'id'

    def get(self, request, id):
        return self.retrieve(request)

    def put(self, request, id):
        return self.update(request)

    def delete(self, request, id):
        return self.destroy(request)