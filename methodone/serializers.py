from rest_framework import serializers
from Table.models import Subject


class SubjectSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, default='')
    code = serializers.CharField(max_length=10, default='')

    def create(self, validated_data):
        return Subject.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)

# class SubjectSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Subject
#         fields = (
#             'name',
#             'code',
#             'url'
#         )