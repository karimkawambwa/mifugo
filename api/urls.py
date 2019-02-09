from django.conf.urls import url

from .views import ShambaView, NgombeView

urlpatterns = [
    url(r"shamba", ShambaView),
    url(r"ngombe", NgombeView.as_view())
]
