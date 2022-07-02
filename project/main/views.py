import csv
from tempfile import NamedTemporaryFile

from openpyxl import Workbook
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
        if download_query == "xlsx":
            return self.download_xlsx(request, *args, **kwargs)

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

    def download_xlsx(self, request, *args, **kwargs):
        wb = Workbook()
        ws = wb.active
        ws.title = "Vehicles"

        fieldnames = [field.name for field in Vehicle._meta.get_fields()]
        ws.append(fieldnames)
        values = self.filter_queryset(self.get_queryset()).values()
        for row in values:
            ws.append(list(row.values()))

        with NamedTemporaryFile() as tmp:
            wb.save(tmp.name)
            tmp.seek(0)
            stream = tmp.read()

        response = HttpResponse(
            stream,
            headers={
                "Content-Type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                "Content-Disposition": 'attachment; filename="vehicles_list.xlsx"',
            },
        )
        return response
