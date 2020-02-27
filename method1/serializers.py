from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from Table.models import Subject


class SubjectSerializer(serializers.Serializer):
    # declaring our serializer fields
    name = serializers.CharField(max_length=100, default='')
    code = serializers.CharField(max_length=10, default='')


    # field level validation; syntax: validate_<fieldname>
    def validate_name(self, value):
        if value.isdigit() :
            raise serializers.ValidationError("Subject name should not contain only digits.")
        return value

    def validate_code(self, value):
        if len(value) < 3 :
            raise serializers.ValidationError("Subject code should be minimum three characters long.")
        return value


    # object level validation
    def validate(self, data):
        if data['name'] == data['code']:
            raise serializers.ValidationError("Subject name and code cannot be same.")
        return data


    # these two methods are used to create new instance or update exisiting one
    def create(self, validated_data):
        return Subject.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.code = validated_data.get('code', instance.code)
        instance.save()
        return instance
