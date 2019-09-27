from django.conf.urls import url
from ..views import AvatarGenerateView

urlpatterns = [
    url(r"^(?P<size>\d+)/(?P<name>\w+)/", AvatarGenerateView.as_view(), name="generator"),
]
