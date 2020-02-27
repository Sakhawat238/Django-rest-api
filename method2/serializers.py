from rest_framework import serializers
from Table.models import School


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['name', 'address']
        # fields = '__all__'
        # exclude = ['name']
        # depth = 1


# using modelserializer we donot have to explicitly implement create and update method
# but if we want to perfrom complex operation or dealing with nested objects
# see official documentation https://www.django-rest-framework.org/api-guide/serializers/