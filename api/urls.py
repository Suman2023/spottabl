from django.urls import path

from api.views import index,init

urlpatterns = [
    path('index/',index, name="index"),
    path('init/',init),

]
