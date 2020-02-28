from rest_framework import viewsets, mixins
from Table.models import Subject
from method8.serializers import SubjectSerializer

class SubjectViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer