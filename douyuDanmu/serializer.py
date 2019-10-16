from rest_framework import serializers
from .models import Lead,Room


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'


'''
# rest framework以django.model为目标，来序列化(serialize)返回json数据，并反序列化post数据导入model中，故不操作数据库本身。

== models.objects.create(data)

'''
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'