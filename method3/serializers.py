from Table.models import Subject
from rest_framework import serializers

class SubjectSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name', 'code']