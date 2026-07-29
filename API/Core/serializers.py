from rest_framework  import  serializers
from .models import *

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'

class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class Voter_RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voter_Register
        fields = '__all__'

class Local_governmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local_government
        fields = '__all__'