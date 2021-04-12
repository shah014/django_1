from django.urls import path
from .views import BookView
from .views import PersonView
from .views import PersonUpdateView
from .views import VehicleModelViewSet
from rest_framework.routers import DefaultRouter
from .views import VehicleView, VehicleUpdateView,\
    VehicleCreateView, VehicleDestroyView
from .views import VehicleListModelViewSet, registration_view, RegisterView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
# router.register('vehicle', VehicleModelViewSet, basename='vehicle')
router.register('vehicle', VehicleListModelViewSet, basename='vehicle')


urlpatterns = [

    path('book/', BookView.as_view(), name='book'),
    path('person/', PersonView.as_view()),
    path('person/<int:pk>/', PersonUpdateView.as_view()),
    path('vehicle/', VehicleView.as_view()),
    path('vehicle/<int:pk>/', VehicleUpdateView.as_view()),
    path('vehicle/<int:pk>/', VehicleCreateView.as_view()),
    path('vehicle/delete/<int:pk>/', VehicleDestroyView.as_view()),
    # path('vehicle/reup/<int:pk>/', VehicleRetrieveUpdateView.as_view()),
    # path('vehicle/redelt/<int:pk>/', VehicleRetrieveDestroyView.as_view()),
    path('register/', RegisterView.as_view(), name='request'),
    path('login/', obtain_auth_token, name='login')

]+router.urls
