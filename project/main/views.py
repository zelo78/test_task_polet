from rest_framework import viewsets
from rest_framework import permissions

from main.serializers import VehicleSerializer
from main.models import Vehicle


class VehicleViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the Vehicles.
    """

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticated]
