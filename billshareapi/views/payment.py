from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from billshareapi.models import Payment

class PaymentView(ViewSet):
    """Payment View"""
     
    def retrieve(self, request, pk):
        """Handle GET requests from single payment
        Returns:
            Response -- JSON serialized payment
        """
        print("====================")
        print("retrieve")
        print("====================")
        payment = Payment.objects.get(pk=pk)
        serializer = PaymentSerializer(payment)
        return Response(serializer.data)
        
    def list(self, request):
        """Handle GET requests to get all payments
        Returns:
            Response -- JSON serialized list of payments
        """
        billId = self.request.query_params.get('billId')
        
        if billId:
            print("====================")
            print('get data')
            print("====================")
            payments = Payment.objects.filter(bill_id=billId)
            serializer = PaymentSerializer(payments, many=True)
            return Response(serializer.data)
        else:
            payments = Payment.objects.all()
            serializer = PaymentSerializer(payments, many=True)
            return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations
        Returns
            Response -- JSON serialized post instance
        """
        payment = Payment.objects.create(
            
            label = request.data["label"],
            amount_paid = request.data["amount_paid"],
            date_paid = request.data["date_paid"],
            payment_type = request.data["payment_type"],
            bill_id = request.data["bill_id"],
            
        )
        
        serializer = PaymentSerializer(payment)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a payment
        Returns:
            Response -- Empty body with 204 status code
        """
        
        payment = Payment.objects.get(pk=pk)
        payment.label = request.data['label']
        payment.amount_paid = request.data['amount_paid']
        payment.date_paid = request.data['date_paid']
        payment.payment_type = request.data['payment_type']
        payment.bill_id = request.data['bill_id']
        
        payment.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
      
    def destroy(self, request, pk):
        payment = Payment.objects.get(pk=pk)
        payment.delete()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
class PaymentSerializer(serializers.ModelSerializer):
      """JSON serializer for payments"""
      
      class Meta:
          model = Payment
          fields = ('id', 'label', 'amount_paid', 'date_paid', 'payment_type', 'bill_id')
          depth = 1