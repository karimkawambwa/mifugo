import csv

from django.core.management import BaseCommand

from django.contrib.auth.models import User
from ...models import Kondo, Mbuzi, Ngombe, Shamba


class Command(BaseCommand):

    help = ""

    def handle(self, *args, **options):
        owner = User.objects.get(username="karim")

        Kondo.objects.all().delete()
        Mbuzi.objects.all().delete()
        Ngombe.objects.all().delete()
        Shamba.objects.all().delete()

        shamba, created = Shamba.objects.get_or_create(
            jina="Mngobwe Integrated Livestock Farm", jina_fupi="MIL", owner=owner
        )


        current_status = {
            "Active": "MZIMA",
            "Sold": "AMEUZWA",
            "Slaughtered": "AMECHINJWA",
            "Died": "AMEKUFA",
            "Dead": "AMEKUFA",
            "Missing": "AMEPOTEA"
        }

        with open("archive/cattle.csv", "r") as f:
            reader = csv.reader(f, delimiter=",")

            for i, line in enumerate(reader):
                print("line[{}] = {}".format(i, line))

                breeder, created = Shamba.objects.get_or_create(jina_fupi=line[2])

                Ngombe.objects.get_or_create(
                    tag=line[1],
                    shamba=shamba,
                    breeder=breeder,
                    jinsia=line[3].upper(),
                    breed=line[4].upper() if line[4] != "Ayshire" else "AYRSHIRE",
                    rangi=line[5],
                    initial_status="HAIJULIKANI",
                    current_status=current_status[line[6]],
                )

        with open("archive/goat.csv", "r") as f:
            reader = csv.reader(f, delimiter=",")
            for i, line in enumerate(reader):
                print("line[{}] = {}".format(i, line))

                breed = {"Boer Cross": "BOER", "Boer": "BOER", "Local": "OTHER"}

                breeder, created = Shamba.objects.get_or_create(jina_fupi=line[2])

                if line[4] == '':
                    continue

                Mbuzi.objects.get_or_create(
                    tag=line[1],
                    shamba=shamba,
                    breeder=breeder,
                    jinsia=line[3].upper(),
                    breed=breed[line[4]],
                    rangi=line[5],
                    initial_status="HAIJULIKANI",
                    current_status=current_status[line[6]],
                )

        with open("archive/sheep.csv", "r") as f:
            reader = csv.reader(f, delimiter=",")
            for i, line in enumerate(reader):
                print("line[{}] = {}".format(i, line))

                breeder, created = Shamba.objects.get_or_create(jina_fupi=line[2])

                Kondo.objects.get_or_create(
                    tag=line[1],
                    shamba=shamba,
                    breeder=breeder,
                    jinsia=line[3].upper(),
                    breed="BHP",
                    rangi=line[5],
                    initial_status="HAIJULIKANI",
                    current_status=current_status[line[6]],
                )

        print(shamba, owner)
