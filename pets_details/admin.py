from django.contrib import admin
from .models import Dog,Breed
# Register your models here.

@admin.register(Dog)
class AnimalsRecord(admin.ModelAdmin):
    list_display=['id','name','age','breed','gender','color','favoritefood','favoritetoy']

@admin.register(Breed)
class AnimalDetails(admin.ModelAdmin):
    list_display=['id','name','size','friendliness','trainability','sheddingamount','exerciseneeds']