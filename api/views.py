from rest_framework import generics, mixins, viewsets, pagination

from .models import Shamba, Ngombe
from .serializers import ShambaSerializer, NgombeSerializer

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class ShambaView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Shamba.objects.all()
    serializer_class = ShambaSerializer


class NgombeView(generics.ListCreateAPIView):
    queryset = Ngombe.objects.all()
    serializer_class = NgombeSerializer