from django.urls import path
from .views import home
from .views import form1


urlpatterns = [
    path('', home, name='home'),
    path('form1/', form1, name='form1')
]
