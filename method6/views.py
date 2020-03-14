from rest_framework import generics, mixins
from method6.serializers import SubjectSerializer, Subject


# Here we have used generic api view and model mixins
# The mixin classes provide the actions that are used to provide the basic view behavior. 
# Note that the mixin classes provide action methods rather than defining the handler methods, such as .get() and .post(), directly. 
# This allows for more flexible composition of behavior.

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
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request)


# The following methods are provided by the mixin classes, and provide easy overriding of the object save or deletion behavior.
# perform_create(self, serializer) - Called by CreateModelMixin when saving a new object instance.
# perform_update(self, serializer) - Called by UpdateModelMixin when saving an existing object instance.
# perform_destroy(self, instance) - Called by DestroyModelMixin when deleting an object instance.

# These hooks are particularly useful for setting attributes that are implicit in the request, 
# but are not part of the request data. For instance, you might set an attribute on the object based on the request user, or based on a URL keyword argument.
# def perform_create(self, serializer):
#     serializer.save(user=self.request.user)

# These override points are also particularly useful for adding behavior that occurs before or after saving an object, such as emailing a confirmation, or logging the update.
# def perform_update(self, serializer):
#     instance = serializer.save()
#     send_email_confirmation(user=self.request.user, modified=instance)

# You can also use these hooks to provide additional validation, by raising a ValidationError(). 
# This can be useful if you need some validation logic to apply at the point of database save. For example:

# def perform_create(self, serializer):
#     queryset = SignupRequest.objects.filter(user=self.request.user)
#     if queryset.exists():
#         raise ValidationError('You have already signed up')
#     serializer.save(user=self.request.user)