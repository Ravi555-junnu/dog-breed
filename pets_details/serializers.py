from rest_framework import serializers
from .models import Dog,Breed

class SerializerRecords(serializers.ModelSerializer):
    class Meta:
        model=Dog
        fields=['id','name','age','breed','gender','color','favoritefood','favoritetoy']
    
def value_1_5(value):
    if int(value)>6 or int(value)<1:
        raise serializers.ValidationError('Invalid value')
    return value

class SerializerDetails(serializers.ModelSerializer):
    type_of_breed=SerializerRecords(many=True,read_only=True)
    friendliness=serializers.CharField(validators=[value_1_5])
    trainability=serializers.CharField(validators=[value_1_5])
    sheddingamount=serializers.CharField(validators=[value_1_5])
    exerciseneeds=serializers.CharField(validators=[value_1_5])
    class Meta:
        model=Breed
        fields=['id','name','size','friendliness','trainability','sheddingamount','exerciseneeds','type_of_breed']