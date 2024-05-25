Django rest full framework
 - pip install djangorestframework

App directory:
 - create model
 -  serializers.py 
   - from rest_framework import serializers
   - create using serializers.ModelSerializer this model
 - create view using from rest_framework import viewsets
 - create path 
   - from rest_framework import routers
   - path('', include(router.urls))
   - router = routers.SimpleRouter()
   - router.register('movieApp', MovieViewSet, basename='movieApp')
        