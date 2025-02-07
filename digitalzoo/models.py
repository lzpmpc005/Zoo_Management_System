from django.db import models
from django.contrib import admin
from django.http import HttpResponse
from django.utils import timezone

class Animal(models.Model):
    name = models.CharField(max_length=100,blank=False,default='')
    description = models.CharField(max_length=1000,blank=False,default='')
    habitat = models.CharField(max_length=100)
    image = models.URLField(max_length=200,blank=True,default='')
    def __str__(self):
        return self.name


class Habitat(models.Model):
    name = models.CharField(max_length=100,blank=False,default='')
    description = models.CharField(max_length=1000,blank=False,default='')
    image = models.URLField(max_length=200,blank=True,default='')
    def __str__(self):
        return self.name

class Zookeeper(models.Model):
    name = models.CharField(max_length=100,blank=False,default='')
    responsibility = models.CharField(max_length=100,blank=False,default='')
    qualification = models.CharField(max_length=100,blank=False,default='')
    image = models.URLField(max_length=200, blank=True, default='')
    def __str__(self):
        return self.name

class Carelog(models.Model):
    animal = models.ForeignKey(Animal,on_delete=models.CASCADE)
    description = models.CharField(max_length=1000,blank=False,default='')
    caretaker = models.ForeignKey(Zookeeper,on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.animal.name



class Member(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        ('adult','adult'),
        ('child','child')
    ]
    TICKET_PERIOD_CHOICES = [
        ('day','day'),
        ('week','week'),
        ('month','month'),
        ('year','year')
    ]
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    ticket_period = models.CharField(max_length=10, choices=TICKET_PERIOD_CHOICES)
    ticket_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE_CHOICES)
    points = models.IntegerField(default=0)
    def __str__(self):
        return self.username
class Activity(models.Model):
    name = models.CharField(max_length=100,blank=False,default='')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.CharField(max_length=1000,blank=False,default='')
    habitat = models.ManyToManyField(Habitat,blank=True)
    animal = models.ManyToManyField(Animal,blank=True)
    member = models.ManyToManyField(Member,blank=True)
    def __str__(self):
        return self.name

class Tourschedule(models.Model):
     name = models.CharField(max_length=100,blank=False,default='')
     start_time = models.DateTimeField()
     end_time = models.DateTimeField()
     description = models.CharField(max_length=1000,blank=False,default='')
     habitat = models.ManyToManyField(Habitat,blank=True)
     member = models.ManyToManyField(Member,blank=True)

     def __str__(self):
         return self.name

     def check_habitat_status(self):
         # 获取当前时间
         current_time = timezone.now()

         # 初始化栖息地状态为"空闲"
         status = "avilable"
         end_time_remaining = None

         # 检查每个关联的栖息地
         for habitat in self.habitat.all():
             # 如果结束时间已过，则标记为"空闲"
             if self.end_time < current_time:
                 status = "available"
                 break
             # 如果当前时间在开始时间和结束时间之间，则标记为"繁忙"
             elif self.start_time <= current_time <= self.end_time:
                 status = "busy"
                 end_time_remaining = self.end_time - current_time
                 break

         return {"status": status, "end_time_remaining": end_time_remaining}

     def update_habitat_status(self):
         # 获取当前时间
         current_time = timezone.now()

         # 更新栖息地状态
         for habitat in self.habitat.all():
             # 根据当前时间和结束时间更新栖息地状态
             if self.end_time < current_time:
                 habitat.status = "available"
             elif self.start_time <= current_time <= self.end_time:
                 habitat.status = "busy"
             else:
                 habitat.status = "available"

             # 保存更新后的栖息地状态
             habitat.save()

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name','description','habitat','image')
    search_fields = ('name','description','habitat','image')

@admin.register(Habitat)
class HabitatAdmin(admin.ModelAdmin):
    list_display = ('name','description','image')
    search_fields = ('name','description','image')

@admin.register(Zookeeper)
class ZookeeperAdmin(admin.ModelAdmin):
    list_display = ('name','responsibility','qualification')
    search_fields = ('name','responsibility','qualification')

@admin.register(Carelog)
class CarelogAdmin(admin.ModelAdmin):
    list_display = ('animal','description','caretaker','date')
    search_fields = ('animal','description','caretaker','date')

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('username','password','full_name','email','ticket_period','ticket_type','points')
    search_fields = ('username','password','full_name','email','ticket_period','ticket_type','points')

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('name','start_time','end_time','description')
    search_fields = ('name','start_time','end_time','description')

@admin.register(Tourschedule)
class TourscheduleAdmin(admin.ModelAdmin):
     list_display = ('name','start_time','end_time','description')
     search_fields = ('name','start_time','end_time','description')











