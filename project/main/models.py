from django.db import models
from django.core.validators import RegexValidator


class Vehicle(models.Model):
    class Meta:
        verbose_name = "транспортное средство"
        verbose_name_plural = "транспортные средства"
        ordering = ["id"]

    brand = models.CharField("марка", max_length=64, help_text="Марка автомобиля")
    model = models.CharField("модель", max_length=128, help_text="Модель автомобиля")
    color = models.CharField("цвет", max_length=64, help_text="Цвет автомобиля")
    registration_number = models.CharField(
        "регистрационный номер",
        max_length=16,
        help_text="Регистрационный номер автомобиля",
    )
    year_of_manufacture = models.PositiveIntegerField(
        "год выпуска", help_text="Год выпуска автомобиля"
    )
    vin = models.CharField(
        "VIN",
        max_length=17,
        unique=True,
        help_text="Идентификационный номер транспортного средства",
        validators=[
            RegexValidator(
                regex="^[0-9A-HJ-NPR-Z]{17}$",
                message="VIN должен иметь 17 символов, допустимы цифры и большие латинские буквы, кроме I, O, Q",
            )
        ],
    )
    vehicle_registration_number = models.CharField(
        "номер СТС", max_length=20, help_text="Номер СТС (свидетельства о регистрации)"
    )
    vehicle_registration_date = models.DateField(
        "дата СТС", help_text="Дата СТС (свидетельства о регистрации)"
    )

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year_of_manufacture})"
