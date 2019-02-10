import uuid

from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import User


class Shamba(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    jina = models.TextField(blank=True, db_index=True)
    jina_fupi = models.TextField(blank=True, db_index=True)

    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    def __str__(self):
        return "%s [ %s ]" % (self.jina, self.jina_fupi)


JINSIA = (("DUME", "Male"), ("JIKE", "Female"))

CURRENT_STATUS = (
    ("MZIMA", "Mzima"),
    ("AMEKUFA", "Amekufa"),
    ("AMEUUZWA", "Ameuzwa"),
    ("AMECHINJWA", "Amechinjwa"),
    ("HAIJULIKANI", "Haijulikani"),
    ("AMEPOTEA", "Amepotea")
)

INITIAL_STATUS = (
    ("AMENUNULIWA", "Amenunuliwa"),
    ("AMEZALIWA", "Amezaliwa"),
    ("HAIJULIKANI", "Haijulikani"),
)


class Myama(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    shamba = models.ForeignKey(Shamba, on_delete=models.CASCADE)

    breeder = models.ForeignKey(Shamba, on_delete=models.DO_NOTHING, related_name="breeder")

    jinsia = models.CharField(max_length=5, choices=JINSIA)
    tag = models.CharField(max_length=255, blank=True, db_index=True)

    amesejiliwa_serikalini = models.BooleanField(default=False)

    rangi = models.CharField(max_length=255, blank=True, db_index=True)

    initial_status = models.CharField(
        max_length=25, choices=INITIAL_STATUS, default="HAIJULIKANI"
    )
    initial_status_date = models.DateField(null=True, blank=True)

    current_status = models.CharField(
        max_length=25, choices=CURRENT_STATUS, default="HAIJULIKANI"
    )
    current_status_date = models.DateField(null=True, blank=True)


AINA_YA_NGOMBE = (
    ("ANKOLE", "Ankole"),
    ("AYRSHIRE", "Ayrshire"),
    ("JERSEY", "Jersey"),
    ("FRIESIAN", "Friesian"),
    ("OTHER", "Other"),
)


class Ngombe(Myama):
    breed = models.CharField(max_length=25, choices=AINA_YA_NGOMBE)

    baba = models.OneToOneField("Ngombe", on_delete=models.DO_NOTHING, related_name="ngombe_baba", null=True)
    mama = models.OneToOneField("Ngombe", on_delete=models.DO_NOTHING, related_name="ngombe_mama", null=True)


AINA_YA_MBUZI = (("BOER", "boer"), ("OTHER", "Other"))


class Mbuzi(Myama):
    breed = models.CharField(max_length=25, choices=AINA_YA_MBUZI)

    baba = models.OneToOneField("Mbuzi", on_delete=models.DO_NOTHING, related_name="mbuzi_baba", null=True)
    mama = models.OneToOneField("Mbuzi", on_delete=models.DO_NOTHING, related_name="mbuzi_mama", null=True)


AINA_YA_KONDO = (("BHP", "Black Head Persian"), ("OTHER", "Other"))


class Kondo(Myama):
    breed = models.CharField(max_length=25, choices=AINA_YA_KONDO)

    baba = models.OneToOneField("Kondo", on_delete=models.DO_NOTHING, related_name="kondo_baba", null=True)
    mama = models.OneToOneField("Kondo", on_delete=models.DO_NOTHING, related_name="kondo_mama", null=True)
