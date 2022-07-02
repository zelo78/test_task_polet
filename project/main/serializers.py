from rest_framework import serializers

from main.models import Vehicle


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"
