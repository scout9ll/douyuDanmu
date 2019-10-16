from .models import Lead,Room
from rest_framework import viewsets, permissions
from .serializer import LeadSerializer,RoomSerializer
from rest_framework import generics
from django_filters import rest_framework as filters


class LeadFilter(filters.FilterSet):
    class Meta:
        model = Lead
        fields = {
            'message': ['icontains'],
            'name': ['iexact'],
            "created_at": ['iexact', 'lte', 'gte']

        }


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()  # 根据lead中的所映射的对象


    filter_backends = (filters.DjangoFilterBackend,)
    serializer_class = LeadSerializer
    filterset_class = LeadFilter

class RoomFilter(filters.FilterSet):
    class Meta:
        model = Room
        fields = {
            'room_id': ['iexact'],
        }

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()  # 根据lead中的所映射的对象


    filter_backends = (filters.DjangoFilterBackend,)
    serializer_class = RoomSerializer
    filterset_class = RoomFilter
