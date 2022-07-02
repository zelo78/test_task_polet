import csv
import io

from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import permissions

from main.serializers import VehicleSerializer
from main.models import Vehicle
from main.filters import VehicleFilter


class VehicleViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the Vehicles.
    """

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = VehicleFilter

    def list(self, request, *args, **kwargs):
        download_query = request.query_params.get("download")
        if download_query == "csv":
            return self.download_csv(request, *args, **kwargs)

        return super().list(request, *args, **kwargs)

    def download_csv(self, request, *args, **kwargs):
        response = HttpResponse(
            headers={
                "Content-Type": "text/csv",
                "Content-Disposition": 'attachment; filename="vehicles_list.csv"',
            }
        )
        fieldnames = [field.name for field in Vehicle._meta.get_fields()]
        writer = csv.DictWriter(response, fieldnames=fieldnames)
        writer.writeheader()
        values = self.filter_queryset(self.get_queryset()).values()
        for row in values:
            writer.writerow(row)

        return response
