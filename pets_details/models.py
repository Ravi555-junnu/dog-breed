from django.db import models

# Create your models here.

class Breed(models.Model):
    name=models.CharField(max_length=20)
    size=models.CharField(max_length=20)
    friendliness=models.IntegerField()
    trainability=models.IntegerField()
    sheddingamount=models.IntegerField()
    exerciseneeds=models.IntegerField()

    def __str__(self):
        return self.name

class Dog(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    breed=models.ForeignKey(Breed,on_delete=models.CASCADE,related_name='type_of_breed')
    gender=models.CharField(max_length=20)
    color=models.CharField(max_length=10)
    favoritefood=models.CharField(max_length=20)
    favoritetoy=models.CharField(max_length=20)

    def __str__(self):
        return self.name