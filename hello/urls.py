from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='index'),
    path('greet/<str:name>', views.greet, name='greet'),
    path('tia_do_zap/<str:name>', views.tia_do_zap, name='tia_do_zap'),
]