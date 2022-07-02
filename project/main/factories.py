from datetime import date

import factory
import factory.fuzzy
from faker_vehicle import VehicleProvider

from main.models import Vehicle

factory.Faker.add_provider(VehicleProvider)


class VehicleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Vehicle

    class Params:
        car = factory.Faker("vehicle_object")

    brand = factory.LazyAttribute(lambda obj: obj.car["Make"])
    model = factory.LazyAttribute(lambda obj: obj.car["Model"])
    color = factory.Faker("color_name", locale="ru_RU")
    registration_number = factory.Faker("license_plate", locale="ru_RU")
    year_of_manufacture = factory.LazyAttribute(lambda obj: obj.car["Year"])
    vin = factory.fuzzy.FuzzyText(length=17, chars="0123456789ABCDEFGHJKLMNPRSTUVWXYZ")
    vehicle_registration_number = factory.fuzzy.FuzzyInteger(1000000000, 9999999999)
    vehicle_registration_date = factory.fuzzy.FuzzyDate(date(2008, 1, 1))
