from django.db import models

class Room(models.Model):
    room_id=models.IntegerField(default=9999,unique=True,primary_key=True)
    room_name=models.CharField(max_length=50)
    room_level=models.IntegerField(blank=True)
    room_banner=models.CharField(max_length=50)

    def __str__(self):
        return self.room_name

class Lead(models.Model):
    name = models.CharField(max_length=100)
    lv = models.IntegerField(default=0)
    message = models.CharField(max_length=500)
    bnn = models.CharField(max_length=50, blank=True)
    bl = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    cid = models.CharField(max_length=50, unique=True)
    room_id=models.ForeignKey(Room,on_delete=models.DO_NOTHING,default=9999) ##外键映射必须是其他表的主键

