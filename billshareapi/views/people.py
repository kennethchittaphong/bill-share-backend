from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from billshareapi.models import People, User, Bill

class PeopleView(ViewSet):
    
    def retrieve(self, request, pk):
        print("====================")
        print("retrieve")
        print("====================")
        people = People.objects.get(pk=pk)
        serializer = PeopleSerializer(people)
        return Response(serializer.data)
    
    def list(self, request):
        billId = self.request.query_params.get('billId')
        
        if billId:
            print("====================")
            print('get data')
            print("====================")
            peoples = People.objects.filter(bill_id=billId)
            serializer = PeopleSerializer(peoples, many=True)
            return Response(serializer.data)
        else:
            peoples = People.objects.all()
            serializer = PeopleSerializer(peoples, many=True)
            return Response(serializer.data)
        
        
    def create(self, request):

        # user = User.objects.get(uid=request.data["user"])
    
        people = People.objects.create(
            name = request.data["name"],
            due_date = request.data["due_date"],
            amount = request.data["amount"],
            status = request.data["status"],
            bill_id = request.data["bill_id"],
           # user = user
        )
        serializer = PeopleSerializer(people)
        return Response(serializer.data)
    
    def update(self, request, pk):
        print("**********************")
        print(pk)
        print("**********************")
        people = People.objects.get(pk=pk)
        data = request.data
        if data.get("name") is not None:
            people.name = request.data["name"]
        if data.get("due_date") is not None:
            people.due_date = request.data["due_date"]
        if data.get("total_amount") is not None:
            people.amount = request.data["total_amount"]
        if data.get("status") is not None:
            people.status = request.data["status"]
        if data.get("bill_id") is not None:
            people.bill_id = request.data["bill_id"]
        
        people.save()
    
        return Response(None, status=status.HTTP_204_NO_CONTENT) 
     
    def destroy(self, request, pk):
        people = People.objects.get(pk=pk)
        people.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)    

class PeopleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = People
        fields = ('id', 'name', 'due_date', 'amount', 'status', 'bill_id') 
        depth = 1