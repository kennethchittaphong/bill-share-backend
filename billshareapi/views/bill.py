from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from billshareapi.models import Bill, User, AuthUser


def isNum(data):
    try:
        int(data)
        return True
    except ValueError:
        return False
class BillView(ViewSet):
    
    
    
    def retrieve(self, request, pk):
        print('check pk ===============')
        print(pk)
        print('check pk ===============')
        checkNum = isNum(pk)
        if checkNum == True:
            bill = Bill.objects.filter(pk=pk)
        else:
            bill = Bill.objects.filter(uid=pk)
        serializer = BillSerializer(bill, many=True)
        return Response(serializer.data)
    
    def list(self, request):
        
        bills = Bill.objects.get()
        # uid_query = self.request.query_params.get('uid', None)
        serializer = BillSerializer(bills, many=True)
        return Response(serializer.data)
        
    def create(self, request):

        user = User.objects.get(uid=request.data["uid"])
    
        bill = Bill.objects.create(
            name = request.data["name"],
            due_date = request.data["due_date"],
            total_amount = request.data["total_amount"],
            split_amount = request.data["split_amount"],
            uid = request.data["uid"],
            user = user
        )
        serializer = BillSerializer(bill)
        return Response(serializer.data)
    
    def update(self, request, pk):

        bill = Bill.objects.get(pk=pk)
        data = request.data
        if data.get("name") is not None:
            bill.name = request.data["name"]
        if data.get("due_date") is not None:
            bill.due_date = request.data["due_date"]
        if data.get("total_amount") is not None:
            bill.total_amount = request.data["total_amount"]
        if data.get("split_amount") is not None:
            bill.split_amount = request.data["split_amount"]
        if data.get("status") is not None:
            bill.status = request.data["status"]
        
        bill.save()
    
        return Response(None, status=status.HTTP_204_NO_CONTENT) 
     
    def destroy(self, request, pk):
        bill = Bill.objects.get(pk=pk)
        bill.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)    

class BillSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bill
        fields = ('id', 'user', 'name', 'due_date', 'total_amount', 'split_amount', 'uid') 
        depth = 1