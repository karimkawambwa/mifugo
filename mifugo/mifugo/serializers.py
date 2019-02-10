from rest_framework import serializers

from .models import Shamba, Ngombe


class ShambaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shamba
        fields = "__all__"

class NgombeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ngombe
        fields = "__all__"
