from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from subscription.api.serializer import SubscriptionSerializer
from subscription.models import Subscription

class SubscriptionView(GenericAPIView):
    queryset = Subscription.objects.all()
    serializer_class =SubscriptionSerializer

    def get(self, request):
        subscription = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscription, many = True)
        return Response(serializer.data, 200)
    
    def post(self, request):
        subscription = request.data 
        serializer = SubscriptionSerializer(data = subscription)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"Subscription successfully created!!"
                },200)
        
        else:
            return Response(serializer.errors, 422)
        

