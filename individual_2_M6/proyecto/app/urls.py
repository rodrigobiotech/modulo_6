from django.urls import path

from app.views import vista_index

urlpatterns = [
    path('', vista_index, name='index'),

]