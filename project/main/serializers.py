from django.contrib.auth.models import User
from rest_framework import serializers

from main.models import Vehicle


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ["url", "username", "email", "groups"]
