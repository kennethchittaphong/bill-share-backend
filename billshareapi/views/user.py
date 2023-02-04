from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from billshareapi.models import User

class UserView(ViewSet):

    def retrieve(self, request, pk):
        
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        
        users = User.objects.all()
        uid_query = request.query_params.get('uid', None)
        if uid_query is not None:
            users = users.filter(uid=uid_query)
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data)

    def create(self, request):
        
        user = User.objects.create(
            uid = request.data["uid"]
      )
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk):
        
        user = User.objects.get(pk=pk)
        user.uid = request.data["uid"]
        user.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):

        user = User.objects.get(pk=pk)
        user.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
                  'uid',
                  'id')
        depth = 1