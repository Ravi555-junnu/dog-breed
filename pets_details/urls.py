from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('dog',views.DogModelViewSet,basename="dog")
router.register('breed',views.BreedModelViewSet,basename="breed")
router.register('DogviewSet',views.DogViewSet,basename="dogV")
router.register('BreedviewSet',views.BreedViewSet,basename="breedV")

urlpatterns = [
    path('router/',include(router.urls)),
    path('dogs_api/',views.dogs_api),
    path('breed_api/',views.breed_api),
    path('DogAPIView/',views.DogAPIViewLC.as_view()),
    path('DogAPIView/<int:pk>/',views.DogAPIViewRDU.as_view()),
    path('BreedAPIView/',views.BreedAPIViewLC.as_view()),
    path('BreedAPIView/<int:pk>/',views.BreedAPIViewRDU.as_view()),
    path('',views.Deserialization.as_view()),
]
