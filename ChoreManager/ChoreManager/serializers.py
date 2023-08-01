from rest_framework import serializers
from .models import User, ChoreList, Chore

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ChoreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoreList
        fields = '__all__'

class ChoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chore
        fields = '__all__'
