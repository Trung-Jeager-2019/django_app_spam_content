from django.urls import path
from .views import (
    home,
    predict
)

app_name = 'spams'

urlpatterns = [
    path("", home, name='home'),
    path("predict/", predict, name='predict')
]
