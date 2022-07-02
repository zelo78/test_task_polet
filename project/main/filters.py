from django_filters import rest_framework as filters

from main.models import Vehicle


class VehicleFilter(filters.FilterSet):
    brand = filters.CharFilter(field_name="brand", lookup_expr="iexact")
    model = filters.CharFilter(field_name="model", lookup_expr="iexact")

    class Meta:
        model = Vehicle
        fields = ["brand", "model"]
