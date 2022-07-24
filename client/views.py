from rest_framework import generics
from .serializers import ClientSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Client


class ClientListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset= Client.objects.all()
    serializer_class = ClientSerializer
 



class ClientReterive(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset= Client.objects.all()
    serializer_class = ClientSerializer
  

        
        
