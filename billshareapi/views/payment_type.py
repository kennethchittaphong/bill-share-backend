from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from billshareapi.models import Payment_

class PaymentTypeView(ViewSet):

    def retrieve(self, request, pk):

        payment_type = Payment_Type.objects.get(pk=pk)
        serializer = PaymentTypeSerializer(payment_type)
        return Response(serializer.data)

    def list(self, request):

        payment_types = Payment_Type.objects.all()
        serializer = PaymentTypeSerializer(payment_types, many=True)
        return Response(serializer.data)

class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_Type
        fields = ('id', 'payment_type')