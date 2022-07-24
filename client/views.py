from rest_framework import generics
from .serializers import ClientSerializer

from .models import Client


class ClientListView(generics.ListCreateAPIView):
    queryset= Client.objects.all()
    serializer_class = ClientSerializer
 



class ClientReterive(generics.RetrieveUpdateDestroyAPIView):
    queryset= Client.objects.all()
    serializer_class = ClientSerializer
  

        
        
