from datetime import date

from rest_framework import serializers

from main.models import Vehicle


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"
        # extra_kwargs = {"vehicle_registration_date": {}}

    def validate_year_of_manufacture(self, value):
        if value > date.today().year:
            raise serializers.ValidationError("Год выпуска ТС в будущем")
        if value < 1900:
            raise serializers.ValidationError(
                "Год выпуска ТС не может быть меньше 1900"
            )
        return value

    def validate_vehicle_registration_date(self, value):
        if value > date.today():
            raise serializers.ValidationError(
                "Дата СТС (свидетельства о регистрации) в будущем"
            )
        return value

    def validate(self, data):
        if data["year_of_manufacture"] > data["vehicle_registration_date"].year:
            raise serializers.ValidationError(
                {
                    "vehicle_registration_date": "Дата свидетельства о регистрации не может быть раньше года выпуска ТС"
                }
            )
        return data
