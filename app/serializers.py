from rest_framework import serializers
from app.models import HNGProfile

class HNGProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = HNGProfile
        fields = '__all__'