from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','email']
