##  ENDPOINT  referentes ao módulo "API"
from django.urls import path
from api import endpoints

urlpatterns = [
    path('',endpoints.getData),
    path('/<int:cod>', endpoints.getAPI)
]