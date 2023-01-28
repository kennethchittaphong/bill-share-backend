from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from billshareapi.models import People, User

class PeopleView(ViewSet):
    
    def retrieve(self, request, pk):
        
        people = People.objects.get(pk=pk)
        serializer = PeopleSerializer(people)
        return Response(serializer.data)
    
    def list(self, request):
        
        peoples = People.objects.all()
        serializer = PeopleSerializer(peoples, many=True)
        return Response(serializer.data)
        
    def create(self, request):

        user = User.objects.get(uid=request.data["user"])
    
        people = People.objects.create(
            name = request.data["name"],
            due_date = request.data["due_date"],
            amount = request.data["amount"],
            status = request.data["status"],
            bill_id = request.data["bill_id"],
            user = user
        )
        serializer = PeopleSerializer(people)
        return Response(serializer.data)
    
    def update(self, request, pk):

        People = People.objects.get(pk=pk)
        
        People.name = request.data["name"],
        People.due_date = request.data["due_date"],
        People.amount = request.data["amount"],
        People.status = request.data["status"]
        People.bill_id = request.data["bill_id"]
        
        People.save()
    
        return Response(None, status=status.HTTP_204_NO_CONTENT) 
     
    def destroy(self, request, pk):
        People = People.objects.get(pk=pk)
        People.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)    

class PeopleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = People
        fields = ('id', 'name', 'due_date', 'amount', 'status', 'bill_id') 
        depth = 1