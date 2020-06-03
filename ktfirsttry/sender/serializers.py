from rest_framework import serializers
from .models import Snd

class SndSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snd
        fields = ('id', 'description', 'mailto', 'text', 'dtime', 'repeat')
        
class Snd_Serializer2(serializers.Serializer):
    description = serializers.CharField ()
    mailto = serializers.EmailField()
    text = serializers.CharField()
    dtime = serializers.DateTimeField()    
    repeat = serializers.CharField()
    
    def create(self, validated_data):
        return Snd.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.description = validated_data.get('description', instance.description)
        instance.mailto = validated_data.get('mailto', instance.mailto)
        instance.text = validated_data.get('text', instance.text)
        instance.dtime = validated_data.get('dtime', instance.dtime)
        instance.repeat = validated_data.get('repeat', instance.repeat)
        instance.save()
        return instance
    
  
    