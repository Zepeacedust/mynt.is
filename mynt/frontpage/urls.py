from django.urls import path


from .views import index, hlekkir, tilgangur, umsokn, uppbod, saga, timeline

urlpatterns = [
    path("hlekkir", hlekkir.Hlekkir.as_view(), name="hlekkir"),
    path("", index.Index.as_view(), name="index"),
    path("tilgangur", tilgangur.Tilgangur.as_view(), name="tilgangur"),
    path("umsokn", umsokn.Umsokn.as_view(), name="umsokn"),
    path("uppbod", uppbod.Uppbod.as_view(), name="uppbod"),
    path("saga", saga.Saga.as_view(), name="saga"),
    path("timeline", timeline.Timeline.as_view(), name="timeline"),
]