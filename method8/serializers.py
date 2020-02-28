from rest_framework import serializers
from Table.models import Subject

class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'code', 'url']