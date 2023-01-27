from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from billshareapi import Bill, User

class BillView(ViewSet):
    
    def retrieve(self, request, pk):
        
        bill = Bill.objects.get(pk=pk)
        serializer = BillSerializer(bill)
        return Response(serializer.data)
    
    def list(self, request):
        
        bills = Bill.objects.all()
        uid_query = request.query_params.get('uid', None)
        
    
    def create(self, request):

        user = User.objects.get(uid=request.data["user"])
    
        bill = Bill.objects.create(
            name = request.data["name"],
            user = user
        )
        serializer = BillSerializer(bill)
        return Response(serializer.data)

    def update(self, request, pk):

        bill = Bill.objects.get(pk=pk)
        
        
        bill.name = request.data["name"]
        bill.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)  

    def destroy(self, request, pk):
        bill = Bill.objects.get(pk=pk)
        bill.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)    

class BillSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bill
        fields = ('id', 'user', 'title',) 
        depth = 1