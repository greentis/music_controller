from .models import Room
from rest_framework import serializers

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields=('id', 'code' , 'host', 
                'guest_controlling', 'votes_to_skip', 'created_at')